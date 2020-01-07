# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import logging
import sqlite3


class SQLlitePipeline(object):


    def open_spider(self, spider):
        self.connection = sqlite3.connect("glasses.db")
        self.c = self.connection.cursor()
        try:
            self.c.execute('''
                CREATE TABLE best_sellers(
                    title TEXT,
                    url TEXT,
                    price TEXT
                )
            ''')
            self.connection.commit()
        except sqlite3.OperationalError:
            pass
                       

    def close_spider(self, spider):
        self.connection.close()

    def process_item(self, item, spider):
        self.c.execute('''
            INSERT INTO best_sellers (title,url,price) VALUES(?,?,?)


        ''', (
            item.get('title'),
            item.get('url'),
            item.get('price')
        ))
        self.connection.commit()
        return item
