# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import MeizituItem

class AbleSpider(scrapy.Spider):
    name = "able"
    allowed_domains = ["www.meizitu.com"]
    start_urls = [
        "http://www.meizitu.com"
    ]

    def parse(self, response):
        main_content = response.css('div#maincontent');

        for sel in response.css('div.postmeta'):
            pass

        for sel in response.css('div.postContent'):
            item = MeizituItem()
            item['title'] = sel.css('div#picture').xpath('.//a/@title').extract()
            item['link'] = sel.css('div#picture').xpath('.//a/@href').extract()
            item['desc'] = 'haha'
            item['img'] = sel.css('div#picture').xpath('.//a/img/@src').extract()
            yield item
