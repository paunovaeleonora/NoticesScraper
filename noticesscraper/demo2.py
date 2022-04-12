import json
import math

import requests


def get_next_page(page_index):
    page_index += 1
    return page_index


def get_payload(index):
    return payload_start + f":{index}" + '}'


def get_all_pages(response):
    data = json.loads(response.text)
    items_per_page = len(data['items'])
    all_items = data['total']
    return math.ceil(all_items / items_per_page)


url = "http://www.e-licitatie.ro/api-pub/NoticeCommon/GetCNoticeList/"
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9,bg;q=0.8',
    'Authorization': 'Bearer null',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    'Cookie': 'isCompact=true; culture=en-US; _HttpSessionID=195DF33A49924EF0BD029F95B765B093; sysNoticeTypeIds=null; '
              '_ga=GA1.2.1153643515.1649321409; _HttpSessionID=7C730EB259414CAAB6E88D8789683777',
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

payload_start = "{\"sysNoticeTypeIds\":[2],\"sortProperties\":[],\"pageSize\":5,\"hasUnansweredQuestions\":false," \
                "\"startPublicationDate\":\"2022-04-08T23:00:00.000Z\"," \
                "\"startTenderReceiptDeadline\":\"2022-04-08T23:00:00.000Z\",\"sysProcedureStateId\":2," \
                "\"pageIndex\""

page_index = 0
payload = get_payload(page_index)
response = requests.request("POST", url, headers=headers, data=payload)
pages = get_all_pages(response)

items = []
for x in range(1):
    payload = get_payload(page_index)

    response = requests.request("POST", url, headers=headers, data=payload)
    print(
        type(response.json())
    )
    print(type(response))
    for item in json.loads(response.text)['items']:
        items.append(item)
    print(x)
    page_index = get_next_page(page_index)
print(f'All Items {len(items)}')
