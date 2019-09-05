# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3

class MovieScrapyPipeline(object):

    def __init__(self):
        self.conn = sqlite3.connect('data.db')
        self.client = self.conn.cursor()
        self.client.execute('''CREATE TABLE IF NOT EXISTS movies
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, serial_number INTEGER, movie_name text, auth text, show_year text, 
                      country text, key_words text, rating_num real, evaluate_num real, describe text)''')

    def process_item(self, item, spider):
        self.client.execute(
            "INSERT INTO movies (serial_number,movie_name,auth,show_year,country,key_words,rating_num,evaluate_num,describe) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (
                item['serial_number'],
                item['movie_name'],
                item['auth'],
                item['show_year'],
                item['country'],
                item['key_words'],
                item['rating_num'],
                item['evaluate_num'],
                item['describe']
            )
        )
        self.conn.commit()
        return item
