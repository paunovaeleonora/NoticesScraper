import json

import scrapy


class NoticesSpider(scrapy.Spider):
    name = 'notices'
    start_urls = ['http://www.e-licitatie.ro/pub/notices/contract-notices/list/2/1']

    search_url = 'http://www.e-licitatie.ro/api-pub/NoticeCommon/GetCNoticeList'
    headers = {
        'Accept': 'application/json',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,bg;q=0.8',
        'Authorization': 'Bearer null',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Length': '232',
        'Content-Type': 'application/json;charset=UTF-8',
        'Culture': 'en-US',
        'Host': 'www.e-licitatie.ro',
        'HttpSessionID': 'null',
        'Origin': 'http://www.e-licitatie.ro',
        'Pragma': 'no-cache',
        'Referer': 'http://www.e-licitatie.ro/pub/notices/contract-notices/list/2/1',
        'RefreshToken': 'null',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29',
        'X-KL-Ajax-Request': 'Ajax_Request',
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=self.search_url,
                                 method='post',
                                 headers=self.headers,
                                 callback=self.parse,
                                 dont_filter=True)

    def parse(self, response):
        raw_data = response.body  # string
        data = json.loads(raw_data)  # json object

        for item in data:
            yield {'date': item['noticeStateDate'],
                   'notice_number': item['noticeNo'],
                   'tender_name': item['contractTitle'],
                   'procedure_state': item['sysProcedureState']['text'],
                   'contract_type': item['sysContractAssigmentType']['text'],
                   'procedure_type': item['sysProcedureType']['text'],
                   'estimated_value': item['estimatedValueRon'], }
