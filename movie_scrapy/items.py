# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    serial_number = scrapy.Field()
    movie_name = scrapy.Field()
    auth = scrapy.Field()
    show_year = scrapy.Field()
    country = scrapy.Field()
    key_words = scrapy.Field()
    rating_num = scrapy.Field()
    evaluate_num = scrapy.Field()
    describe = scrapy.Field()


class RtbSquareScrapyItem(scrapy.Item):
    title = scrapy.Field()
    release_year = scrapy.Field()
    release_month = scrapy.Field()
    release_day = scrapy.Field()
    key_words = scrapy.Field()
