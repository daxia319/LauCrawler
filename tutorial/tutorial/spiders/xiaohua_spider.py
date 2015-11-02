# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import XiaoHuaItem
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request

def printhxs(hxs):
    for i in hxs:
        print i.encode('utf-8')

'''
    <div class="item_t">
<div class="top-title">TOP1</div>
            <div class="img">
                <a href="/p-1-64.html"  target="_blank"><img width="210"  alt="南京航空航天大学校花陈都灵" src="http://www.xiaohuar.com/d/file/20140811101923185.jpg" /></a>
                <span class="price">陈都灵</span>
                <div class="btns">
                    <a href="http://www.xiaohuar.com/" class="img_album_btn">大学校花</a>
                </div>
            </div>
            <div class="title"><span><a href="/p-1-64.html"  target="_blank">南京航空航天大学校花陈都灵</a></span></div>
        </div>
'''
class XiaohuaSpider(scrapy.Spider):
    name = "xiaohuar"
    allowed_domains = ["www.xiaohuar.com"]
    start_urls = [
        "http://www.xiaohuar.com/2014.html",
        "http://www.xiaohuar.com/2013.html",
        "http://www.xiaohuar.com/hua",
    ]


    def parse(self, response):
        for sel in response.xpath('//div[@class="item_t"]'):
            item = XiaoHuaItem()
            sub_sel = sel.xpath('.//div[@class="img"]')
            item['name'] = sub_sel.xpath('.//span/text()').extract()
            printhxs(item['name'])
            item['rank'] = sel.xpath('.//div[@class="top-title"]/text()').extract()
            item['school'] = sub_sel.xpath('.//a/img/@alt').extract()
            img_link = sub_sel.xpath('.//a/img/@src').extract()[0]
            if img_link.startswith('http://'):
                item['image_urls'] = [img_link]
            else:
                item['image_urls'] = [response.urljoin(img_link)]
            yield item

            detail_link = sub_sel.xpath('.//a/@href').extract()[0]
            yield Request(response.urljoin(detail_link), callback=self.parse_sub)

    '''
    她 的 相 册
    thumbnail.jpg
    '''
    def parse_sub(self, response):
        for sel in response.xpath('//div[@class="post_entry"]/ul[@class="photo_ul"]/li[@class="photoli"]/div'):
            item = XiaoHuaItem()
            item['name']='hehe'
            item['rank']='hehe'
            item['school']='hehe'
            img_link = sel.xpath('.//a/img/@src').extract()[0]
            item['image_urls'] = [response.urljoin(img_link)]
            yield item

            detail_link = sel.xpath('.//a/@href').extract()[0]
            yield Request(detail_link, callback = self.parse_sub_big)

    '''
        <div class="ad-nav">
            <div class="pic_img_gallery ad-thumbs">
                <ul class="ad-thumb-list" style="width: 22297px;">
               <li><div class="inner"><a href="/d/file/20151102/988cf06c2ec7b80a3ac0acbc35945d98.jpg" class=""><img src="/d/file/20151102/small988cf06c2ec7b80a3ac0acbc35945d981446429698.jpg" title="" alt="" width="105" height="118" class="image0"></a></div></li><li><div class="inner"><a href="/d/file/20151102/164bf0bc7f12580798745ccf22742085.jpg" class=""><img src="/d/file/20151102/small164bf0bc7f12580798745ccf227420851446429699.jpg" title="" alt="" width="105" height="118" class="image0"></a></div></li><li><div class="inner"><a href="/d/file/20151102/c53bf63c30048787d1a739588478d619.jpg" class=""><img src="/d/file/20151102/smallc53bf63c30048787d1a739588478d6191446429701.jpg" title="" alt="" width="105" height="118" class="image0"></a></div></li><li><div class="inner"><a href="/d/file/20151102/9cdef6be4a87c8cf04ac253b572cf510.jpg" class=""><img src="/d/file/20151102/small9cdef6be4a87c8cf04ac253b572cf5101446429702.jpg" title="" alt="" width="105" height="118" class="image0"></a></div></li><li><div class="inner"><a href="/d/file/20151102/3db05de6de544536a63d118305325f23.jpg" class=""><img src="/d/file/20151102/small3db05de6de544536a63d118305325f231446429704.jpg" title="" alt="" width="105" height="118" class="image0"></a></div></li><li><div class="inner"><a href="/d/file/20151102/a18f42bae4bb0ab75f78eddaa2318154.jpg" class=""><img src="/d/file/20151102/smalla18f42bae4bb0ab75f78eddaa23181541446429706.jpg" title="" alt="" width="105" height="118" class="image0"></a></div></li><li><div class="inner"><a href="/d/file/20151102/efa1a020190b62c568af1457f40cd212.jpg" class=""><img src="/d/file/20151102/smallefa1a020190b62c568af1457f40cd2121446429708.jpg" title="" alt="" width="105" height="118" class="image0"></a></div></li><li><div class="inner"><a href="/d/file/20151102/6d8c3e82c7c590cf89b6a62d576715ec.jpg" class=""><img src="/d/file/20151102/small6d8c3e82c7c590cf89b6a62d576715ec1446429710.jpg" title="" alt="" width="105" height="118" class="image0"></a></div></li><li><div class="inner"><a href="/d/file/20151102/c43e4d37e7e93a7cff2644b0f88ab2f3.jpg" class=""><img src="/d/file/20151102/smallc43e4d37e7e93a7cff2644b0f88ab2f31446429713.jpg" title="" alt="" width="105" height="118" class="image0"></a></div></li>                                </ul>
            </div>
            <div class="pic_barL">
                <a class="ad-back"></a>
            </div>
            <div class="pic_barR">
                <a class="ad-forward"></a>
            </div>
            <div class="clear">
            </div>
        </div>
    '''
    def parse_sub_big(self, response):
        for sel in response.xpath('//ul[@class="ad-thumb-list"]/li/div'):
            item = XiaoHuaItem()
            item['name']='h2'
            item['rank']='h2'
            item['school']='h2'
            img_link = sel.xpath('.//a/@href').extract()[0]
            item['image_urls'] = [response.urljoin(img_link)]
            yield item