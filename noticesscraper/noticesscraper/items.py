# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from itemloaders.processors import TakeFirst, MapCompose


def format_date(date):
    data = date.split('T')[0]
    year, month, day = data.split('-')
    return f'{day}.{month}.{year}'


# def decode_chars(value):
#     return (value.encode('utf-8')).decode('utf-8')


# def format_to_second_decimal(value):
#     return format(value, '.2f')

class NoticesscraperItem(scrapy.Item):
    notice_date = scrapy.Field(input_processor=MapCompose(format_date), output_processor=TakeFirst())
    notice_number = scrapy.Field(input_processor=MapCompose(), output_processor=TakeFirst())
    tender_name = scrapy.Field(input_processor=MapCompose(), output_processor=TakeFirst())
    procedure_state = scrapy.Field(input_processor=MapCompose(), output_processor=TakeFirst())
    contract_type = scrapy.Field(input_processor=MapCompose(), output_processor=TakeFirst())
    procedure_type = scrapy.Field(input_processor=MapCompose(), output_processor=TakeFirst())
    estimated_value = scrapy.Field(input_processor=MapCompose(), output_processor=TakeFirst())
