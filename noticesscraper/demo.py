# import json
# import math
#
# import requests
#
#
# def get_first_response(url, payload, headers):
#     payload += ':0' + '}'
#     return requests.request('POST', url, headers=headers, data=payload)
#
#
# def get_pages(response):
#     data = response.json()
#     pages = math.ceil(data['total'] / len(data['items']))
#     return pages
#
#
# def get_next_payload(page, payload):
#     next_page_payload = payload + f":{page}" + '}'
#     return next_page_payload
#
#
# url = "http://www.e-licitatie.ro/api-pub/NoticeCommon/GetCNoticeList/"
#
# payload = "{\"sysNoticeTypeIds\":[2],\"sortProperties\":[],\"pageSize\":1152,\"hasUnansweredQuestions\":false," \
#           "\"startPublicationDate\":\"2022-03-09T13:26:51.275Z\"," \
#           "\"startTenderReceiptDeadline\":\"2022-04-08T12:26:51.275Z\",\"sysProcedureStateId\":2,\"pageIndex\""
#
# headers = {
#     'Accept': 'application/json, text/plain, */*',
#     'Accept-Language': 'en-US,en;q=0.9,bg;q=0.8',
#     'Authorization': 'Bearer null',
#     'Cache-Control': 'no-cache',
#     'Connection': 'keep-alive',
#     'Content-Type': 'application/json;charset=UTF-8',
#     'Cookie': 'isCompact=true; culture=en-US; _HttpSessionID=195DF33A49924EF0BD029F95B765B093; sysNoticeTypeIds=null; '
#               '_ga=GA1.2.1153643515.1649321409; _HttpSessionID=7C730EB259414CAAB6E88D8789683777',
#     'Culture': 'en-US',
#     'HttpSessionID': 'null',
#     'Origin': 'http://www.e-licitatie.ro',
#     'Pragma': 'no-cache',
#     'Referer': 'http://www.e-licitatie.ro/pub/notices/contract-notices/list/2/1',
#     'RefreshToken': 'null',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                   'Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29',
#     'X-KL-Ajax-Request': 'Ajax_Request'
# }
#
# response = get_first_response(url, payload, headers)
# pages = get_pages(response)
#
# data = response.json()['items']
# for i in data:
#     print(i)
#
#
# from jsonschema.validators import validate
#
# json_schema = {
#         "type": "object",
#         "required": [
#             "date",
#             "notice_number",
#             "tender_name",
#             "procedure_state",
#             "contract_type",
#             "procedure_type",
#             "estimated_value"
#         ],
#         "properties": {
#             "date": {
#                 "type": "string",
#                 "default": "",
#                 "examples": ["2022-03-24T13:00:39+02:00"],
#                 "pattern": "^.*$"
#             },
#             "notice_number": {
#
#                 "type": "string",
#                 "default": "",
#                 "examples": [
#                     "CN1040684"
#                 ],
#                 "pattern": "^.*$"
#             },
#             "tender_name": {
#
#                 "type": "string",
#                 "default": "",
#                 "examples": [
#                     "Elaborare documentatii tehnico-economice pentru proiectul “Îmbunătățirea nivelului de trafic al DJ 156A și DJ 208G pentru accesul la rețeaua TEN-T” respectiv: studii de teren, expertiza tehnica, DALI, PT, asistenta tehnică din partea proiectantului"
#                 ],
#                 "pattern": "^.*$"
#             },
#             "procedure_state": {
#                 "type": "string",
#                 "default": "",
#                 "examples": [
#                     "In desfasurare"
#                 ],
#                 "pattern": "^.*$"
#             },
#             "contract_type": {
#
#                 "type": "string",
#                 "default": "",
#                 "examples": [
#                     "Contract de achizitii publice"
#                 ],
#                 "pattern": "^.*$"
#             },
#             "procedure_type": {
#
#                 "type": "string",
#                 "default": "",
#                 "examples": [
#                     "Licitatie deschisa"
#                 ],
#                 "pattern": "^.*$"
#             },
#             "estimated_value": {
#
#                 "type": "number",
#                 "examples": [
#                     4182846.2
#                 ],
#                 "default": 0.0
#             }
#         }
#     }
#
# valid_json = {"date": "2022-03-24T13:00:39+02:00", "notice_number": "CN1040684", "tender_name": "Elaborare documentatii tehnico-economice pentru proiectul \u201c\u00cembun\u0103t\u0103\u021birea nivelului de trafic al DJ 156A \u0219i DJ 208G pentru accesul la re\u021beaua TEN-T\u201d respectiv: studii de teren, expertiza tehnica, DALI, PT, asistenta tehnic\u0103 din partea proiectantului", "procedure_state": "In desfasurare", "contract_type": "Contract de achizitii publice", "procedure_type": "Licitatie deschisa", "estimated_value": 4182846.2},
# invalid_json = {"date": 3, "notice_number": "CN1040684", "tender_name": "Elaborare documentatii tehnico-economice pentru proiectul \u201c\u00cembun\u0103t\u0103\u021birea nivelului de trafic al DJ 156A \u0219i DJ 208G pentru accesul la re\u021beaua TEN-T\u201d respectiv: studii de teren, expertiza tehnica, DALI, PT, asistenta tehnic\u0103 din partea proiectantului", "procedure_state": "In desfasurare", "contract_type": "Contract de achizitii publice", "procedure_type": "Licitatie deschisa", "estimated_value": 4182846.2},
#
# if validate(valid_json, json_schema):
#     print('valid')
# else:
#     print('invalid')
import datetime

from jsonschema import validate, ValidationError, SchemaError

# schema = {
#     "type": "object",
#     "properties": {
#         "name": {"type": "string"},
#         "age": {"type": "number"}
#     },
#     "required": ["age", "name"]
#
# }

# validJson = {"name": "Eggs", "age": 10}
# invalidJson = {"name": "Eggs", "age": "string"}
json_schema = {
    "definitions": {},
    "type": "object",
    "required": [
        "date",
        "notice_number",
        "tender_name",
        "procedure_state",
        "contract_type",
        "procedure_type",
        "estimated_value"
    ],
    "properties": {
        "date": {
            "type": "string",
        },
        "notice_number": {

            "type": "string",

        },
        "tender_name": {

            "type": "string",
            "default": "",

        },
        "procedure_state": {

            "type": "string",

        },
        "contract_type": {

            "type": "string"

        },
        "procedure_type": {

            "type": "string",

        },
        "estimated_value": {

            "type": "array",

        }
    }
}
b = {"date": "2022-03-24T13:00:39+02:00",
     "notice_number": "CN1040684",
     "tender_name": "Elaborare documentatii tehnico-economice pentru proiectul "
                    "\u201c\u00cembun\u0103t\u0103\u021birea nivelului de trafic al DJ 156A \u0219i DJ 208G pentru "
                    "accesul la re\u021beaua TEN-T\u201d respectiv: studii de teren, expertiza tehnica, DALI, PT, "
                    "asistenta tehnic\u0103 din partea proiectantului",
     "procedure_state": "In desfasurare",
     "contract_type": "Contract de achizitii publice",
     "procedure_type": "Licitatie deschisa",
     "estimated_value": 4182846.2
     }

# try:
#     validate(b, json_schema)
#     print('it is valid')
#
# except SchemaError as e:
#     print("There is an error with the schema")
#
# except ValidationError as e:
#     print(e)


# solve romanian charachers
# message = "Elaborare documentatii tehnico-economice pentru proiectul \u201c\u00cembun\u0103t\u0103\u021birea nivelului de trafic al DJ 156A \u0219i DJ 208G pentru accesul la re\u021beaua TEN-T\u201d respectiv: studii de teren, expertiza tehnica, DALI, PT, asistenta tehnic\u0103 din partea proiectantului"
# new = message.encode('utf-8')
# print(new)
# print(new.decode('utf-8'))
# new_1 = 'Elaborare documentatii tehnico-economice pentru proiectul'
# print(new_1.encode('utf-8'))

# myFloat = 23.0000000000000000000000000
# print(format(myFloat, '.2f'))


payload = "{\"sysNoticeTypeIds\":[2],\"sortProperties\":[],\"pageSize\":5,\"hasUnansweredQuestions\":false," \
          "\"startPublicationDate\":\"2022-04-10T23:00:00.000Z\"," \
          "\"startTenderReceiptDeadline\":\"2022-04-11T14:01:36.740Z\",\"sysProcedureStateId\":2,\"pageIndex\":0," \
          "\"endPublicationDate\":\"2022-04-10T23:00:00.000Z\"}"

first_part_payload, second_part_payload = payload.split('pageIndex":0')

print(first_part_payload)
print('-------------------------')
print(second_part_payload)
#
# def create_payload_to_work_with():
#     sysNoticeTypeIds = "\"{\"sysNoticeTypeIds\":[2],"
#     sortProperties = "\"sortProperties\":[],"
#     page_size = "\"pageSize\":5,"
#     hasUnansweredQuestions = "\"hasUnansweredQuestions\":false,"
#     startPublicationDate = "\"startPublicationDate\":\"2022-04-10T23:00:00.000Z\","
#     startTenderReceiptDeadline = "\"startTenderReceiptDeadline\":\"2022-04-11T14:01:36.740Z\","
#     sysProcedureStateId = "\"sysProcedureStateId\":2,"
#     pageIndex = "\"pageIndex\":0,"
#     endPublicationDate = "\"endPublicationDate\":\"2022-04-10T23:00:00.000Z\"}"
#     pass
#
# a = 'Achiziționarea de "Servicii de consultanță în domeniul inovării" în cadrul proiectului tehnologic inovativ de CDI (cercetare, dezvoltare și inovare), cofinanțat din Fondul European de Dezvoltare Regională prin Programul Operațional Competitivitate 2014-2020'

