import json
import math

import scrapy
from ..items import NoticesscraperItem
from scrapy.loader import ItemLoader


class NoticesSpider(scrapy.Spider):
    name = 'notices'
    start_urls = ['http://www.e-licitatie.ro/pub/notices/contract-notices/list/2/1']

    payload = "{\"sysNoticeTypeIds\":[2],\"sortProperties\":[],\"pageSize\":5,\"hasUnansweredQuestions\":false," \
              "\"startPublicationDate\":\"2022-04-10T23:00:00.000Z\"," \
              "\"startTenderReceiptDeadline\":\"2022-04-11T14:01:36.740Z\",\"sysProcedureStateId\":2,\"pageIndex\":0," \
              "\"endPublicationDate\":\"2022-04-10T23:00:00.000Z\"} "
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en, ro;q=0.9,bg;q=0.8',
        'Authorization': 'Bearer null',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        'Cookie': 'isCompact=true; culture=en-US; _HttpSessionID=195DF33A49924EF0BD029F95B765B093; '
                  'sysNoticeTypeIds=null; _ga=GA1.2.1153643515.1649321409; '
                  '_HttpSessionID=7C730EB259414CAAB6E88D8789683777',
        'Culture': 'en-US',
        'HttpSessionID': 'null',
        'Origin': 'http://www.e-licitatie.ro',
        'Pragma': 'no-cache',
        'Referer': 'http://www.e-licitatie.ro/pub/notices/contract-notices/list/2/1',
        'RefreshToken': 'null',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29',
        'X-KL-Ajax-Request': 'Ajax_Request'
    }

    first_part_payload, second_part_payload = payload.split('pageIndex":0')

    def start_requests(self):
        request = scrapy.Request(url='http://www.e-licitatie.ro/api-pub/NoticeCommon/GetCNoticeList',
                                 method='POST',
                                 headers=self.headers,
                                 body=self.payload,
                                 callback=self.parse,
                                 dont_filter=True)
        yield request

    def parse(self, response):
        data = json.loads(response.text)['items']
        items = json.loads(response.text)['total']
        total_pages = math.ceil(items / len(data))
        for page in range(total_pages):
            current_page = f'pageIndex":{page}'
            new_payload = self.first_part_payload + current_page + self.second_part_payload
            yield scrapy.Request(url='http://www.e-licitatie.ro/api-pub/NoticeCommon/GetCNoticeList',
                                 method='POST',
                                 headers=self.headers,
                                 body=new_payload,
                                 callback=self.parse_item,
                                 dont_filter=True)

    def parse_item(self, response):
        data = json.loads(response.text)['items']

        for item in data:
            l = ItemLoader(item=NoticesscraperItem(), )

            l.add_value('notice_date', item['noticeStateDate'])
            l.add_value('notice_number', item['noticeNo'])
            l.add_value('tender_name', item['contractTitle'])
            l.add_value('procedure_state', item['sysProcedureState']['text'])
            l.add_value('contract_type', item['sysContractAssigmentType']['text'])
            l.add_value('procedure_type', item['sysProcedureType']['text'])
            l.add_value('estimated_value', item['estimatedValueRon'])

            yield l.load_item()

            # piece['date'] = item['noticeStateDate']
            # piece['notice_number'] = item['noticeNo']
            # piece['tender_name'] = item['contractTitle']
            # piece['procedure_state'] = item['sysProcedureState']['text']
            # piece['contract_type'] = item['sysContractAssigmentType']['text']
            # piece['procedure_type'] = item['sysProcedureType']['text']
            # piece['estimated_value'] = item['estimatedValueRon']

            # yield piece
