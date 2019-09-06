# -*- coding: utf-8 -*-
import scrapy
import re
from movie_scrapy.items import MovieScrapyItem


class DoubanSpiderSpider(scrapy.Spider):
    name = 'douban_spider'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/top250']
    custom_settings = {
        'ITEM_PIPELINES': {
            'movie_scrapy.pipelines.MovieScrapyPipeline': 300,
        }
    }

    def parse(self, response):
        movies = response.xpath("//div[@class='article']//ol[@class='grid_view']/li")
        for movie in movies:
            movie_item = MovieScrapyItem()
            movie_item['serial_number'] = movie.xpath(".//div[@class='item']//em/text()").extract_first()
            movie_item['movie_name'] = movie.xpath(".//div[@class='info']//div[@class='hd']/a/span[1]/text()").extract_first()
            intro_contents = movie.xpath(".//div[@class='info']//div[@class='bd']/p[1]/text()").extract()
            movie_item['auth'] = intro_contents[0].split()[1]
            content_s = ""
            for item in intro_contents[1].split():
                if item != '/':
                    content_s += " "+item
                else:
                    content_s += item
            movie_item['show_year'] = content_s.split('/')[0]
            movie_item['country'] = content_s.split('/')[1]
            movie_item['key_words'] = content_s.split('/')[2]
            movie_item['rating_num'] = movie.xpath(".//span[@class='rating_num']/text()").extract_first()
            evaluate_num = movie.xpath(".//div[@class='star']/span[4]/text()").extract_first()
            movie_item['evaluate_num'] = int(re.findall('\d+', evaluate_num)[0])
            movie_item['describe'] = movie.xpath(".//div[@class='bd']/p[@class='quote']/span/text()").extract_first()
            yield movie_item
        next_page = response.xpath("//span[@class='next']/link/@href").extract()
        if next_page:
            netxt_page_url = next_page[0]
            yield scrapy.Request("http://movie.douban.com/top250" + netxt_page_url, callback = self.parse)
