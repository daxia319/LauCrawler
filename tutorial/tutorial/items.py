# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class DmozItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()

class MeizituItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()
    img = scrapy.Field()

class XiaoHuaItem(scrapy.Item):
    name = scrapy.Field()
    rank = scrapy.Field()
    school = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
