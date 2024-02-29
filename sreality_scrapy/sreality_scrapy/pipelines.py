import psycopg2
import sys

# setting path
import os
sys.path.append("/app")
sys.path.append("/workspace")
print(os.getcwd())
from db_handler import DbHandler

class PostgresPipeline(object):
    def __init__(self):
        self.db = None

    def open_spider(self, spider):
        # Connect to the database
        self.db = DbHandler()
        self.db.create_ads_table()
        
    def close_spider(self, spider):
        # Close the database connection
        self.db.close()

    def process_item(self, item, spider):
        # Insert item into database
        self.db.insert_ad(item)
        return item
                