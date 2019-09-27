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


class RtbSquareScrapyPipeline(object):
    def __init__(self):
        self.conn = sqlite3.connect('data.db')
        self.client = self.conn.cursor()
        self.client.execute('''CREATE TABLE IF NOT EXISTS rtb_square_news
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, title text, 
                      release_year INTEGER, release_month INTEGER, release_day INTEGER, key_words text)''')

    def process_item(self, item, spider):
        self.client.execute(
            "INSERT INTO rtb_square_news (title, release_year, release_month, release_day,key_words) VALUES (?, ?, ?, ?, ?)", (
                item['title'],
                item['release_year'],
                item['release_month'],
                item['release_day'],
                item['key_words']
            )
        )
        self.conn.commit()
        return item


class RtbSquareScrapyPipeline(object):
    def __init__(self):
        self.conn = sqlite3.connect('rarejob_news_data.db')
        self.client = self.conn.cursor()
        self.client.execute('''CREATE TABLE IF NOT EXISTS rarejob_news
                         (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                         title text, 
                         release_year INTEGER, release_month INTEGER, release_day INTEGER, 
                         unlocking_word text, meaning text, example text, article_url text, category text)''')

    def process_item(self, item, spider):
        self.client.execute(
            "INSERT INTO rarejob_news (title, release_year, release_month, release_day,"
            "unlocking_word, meaning, example, article_url, category) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
                item['title'],
                item['release_year'],
                item['release_month'],
                item['release_day'],
                item['unlocking_word'],
                item['meaning'],
                item['example'],
                item['article_url'],
                item['category']
            )
        )
        self.conn.commit()
        return item
