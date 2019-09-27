# -*- coding: utf-8 -*-
import scrapy
import re
from data_scrapy.items import RarejobDailyNewsScrapyItem


class RarejobDailyNewsSpiderSpider(scrapy.Spider):
    name = 'rarejob_daily_news_spider'
    allowed_domains = ['www.rarejob.com/dna']
    start_urls = ['https://www.rarejob.com/dna/']
    custom_settings = {
        'ITEM_PIPELINES': {
            'data_scrapy.pipelines.RtbSquareScrapyPipeline': 300,
        }
    }

    def __init__(self, date=None, *args, **kwargs):
        super(RarejobDailyNewsSpiderSpider, self).__init__(*args, **kwargs)
        self.date = date
        if self.date:
            self.start_urls = ['https://www.rarejob.com/dna/%s' % self.date]

    def parse(self, response):
        if self.date:
            article_page_url = 'https://www.rarejob.com' + response.xpath("//article//header/h3/a/@href").extract()[0]
            yield scrapy.Request(article_page_url, callback=self.parse_article, dont_filter=True)
        else:
            article_url_list = response.xpath("//div[@id='inner-content']//article//header//*[self::h1 or self::h3]//a/@href")
            for item in article_url_list:
                article_page_url = 'https://www.rarejob.com' + item.extract()
                yield scrapy.Request(article_page_url, callback=self.parse_article, dont_filter=True)

            next_page = response.xpath("//nav[@class='pagination']//ul[@class='page-numbers']//li//span//following::li[1]//a/@href").extract_first()
            yield scrapy.Request(next_page, callback=self.parse, dont_filter=True)

    def parse_article(self, response):
        words_list = response.xpath("//div[@class='inner_box umw_box']//ol/li")
        for word_item in words_list:
            news_item = RarejobDailyNewsScrapyItem()
            news_item['title'] = response.xpath("//article//header/h1/text()").extract_first()
            news_item['article_url'] = response.request.url
            news_item['category'] = response.xpath("//article//header//p[@class='article-header']/a/text()").extract_first()
            news_item['unlocking_word'] = word_item.xpath("./span/em/text()").extract_first()
            news_item['meaning'] = word_item.xpath("./span/text()").extract()[1]
            dr = re.compile(r'<[^>]+>', re.S)
            news_item['example'] = dr.sub('', word_item.xpath("./span/p").extract()[0].replace('\xa0', ' '))

            if self.date:
                news_item['release_year'] = self.date.split('/')[0]
                news_item['release_month'] = self.date.split('/')[1]
                news_item['release_day'] = self.date.split('/')[2]
            else:
                news_item['release_year'] = response.request.url.split('/')[4]
                news_item['release_month'] = response.request.url.split('/')[5]
                news_item['release_day'] = response.request.url.split('/')[6]
            yield news_item

