# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from jsonschema import validate, ValidationError
from scrapy.exceptions import DropItem
import sqlite3


class NoticesscraperPipeline:
    json_schema = {
        "definitions": {},
        "type": "object",
        "required": [
            "notice_date",
            "notice_number",
            "tender_name",
            "procedure_state",
            "contract_type",
            "procedure_type",
            "estimated_value"
        ],
        "properties": {
            "notice_date": {"type": "string"},
            "notice_number": {"type": "string"},
            "tender_name": {"type": "string"},
            "procedure_state": {"type": "string"},
            "contract_type": {"type": "string"},
            "procedure_type": {"type": "string"},
            "estimated_value": {"type": "number"}
        }
    }

    def __init__(self):
        self.con = sqlite3.connect('notices.db')
        self.cur = self.con.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS notices(
        notice_number TEXT PRIMARY KEY,
        notice_date TEXT,
        tender_name TEXT,
        procedure_state TEXT,
        contract_type TEXT,
        procedure_type TEXT,
        estimated_value REAL
        )""")

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        data_dict = adapter.asdict()

        try:
            validate(instance=data_dict, schema=self.json_schema)

        except ValidationError as e:
            raise DropItem(e)
        self.cur.execute(
            """INSERT OR IGNORE INTO notices VALUES(?,?,?,?,?,?,?)""",
            (item['notice_number'], item['notice_date'], item['tender_name'],
             item['procedure_state'], item['contract_type'], item['procedure_type'],
             item['estimated_value']))
        self.con.commit()
        return item
