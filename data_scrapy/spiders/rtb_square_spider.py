# -*- coding: utf-8 -*-
import scrapy
from data_scrapy.items import RtbSquareScrapyItem

class RtbSquareSpiderSpider(scrapy.Spider):
    name = 'rtb_square_spider'
    allowed_domains = ['rtbsquare.ciao.jp']
    start_urls = ['http://rtbsquare.ciao.jp/?cat=5']
    custom_settings = {
        'ITEM_PIPELINES': {
            'data_scrapy.pipelines.RtbSquareScrapyPipeline': 300,
        }
    }

    def parse(self, response):
        get_next_page = True
        domestic_news_list = response.xpath("//div[@id='content']//div[@class='col8']")
        for news in domestic_news_list:
            news_item = RtbSquareScrapyItem()
            news_item['title'] = news.xpath(".//h2/a/text()").extract_first()
            release_date = news.xpath(".//li/text()").extract_first().split('/')
            news_item['release_year'] = int(release_date[0])
            news_item['release_month'] = int(release_date[1])
            news_item['release_day'] = int(release_date[2])
            news_item['key_words'] = "/".join(news.xpath(".//ul[@class='post-categories']/a/text()").extract())
            if int(release_date[0]) < 2016:
                get_next_page = False
                break
            else:
                yield news_item
        next_page = response.xpath("//div[@class='pagination']/a[@class='next page-numbers']/@href").extract()
        if next_page and get_next_page:
            netxt_page_url = next_page[0]
            yield scrapy.Request("http://rtbsquare.ciao.jp/" + netxt_page_url, callback=self.parse)
