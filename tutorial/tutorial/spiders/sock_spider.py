# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import XiaoHuaItem
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request

'''

   <div class="interestline"><span>本周更新：<b>11</b>&nbsp;&nbsp;&nbsp;&nbsp;总共图片：1974</span>你可能感兴趣的类型：<a href="http://www.4493.com/star/heisi/" target="_blank">黑丝美女系列</a>
<a href="http://www.4493.com/star/changtui/" target="_blank">长腿美女系列</a>
<a href="http://www.4493.com/star/beautyleg/" target="_blank">beautyleg系列</a>
<a href="http://www.4493.com/star/meitui/" target="_blank">美腿美女系列</a>
<a href="http://www.4493.com/top/siwa.html" target="_blank">丝袜美女排行榜</a></div>
   <div class="piclist">
   <ul class="clearfix">
   <li>
    <a href="http://www.4493.com/siwameitui/50128/1.htm" target="_blank">
        <img src="http://img.1985t.com/uploads/previews/2015/10/0-nOvKfp.jpg" alt="温雅气质女郎丝袜旗袍性感写真" />
        <span>温雅气质女郎丝袜旗袍性感写真</span></a>
    <b class="b1">2015-10-31</b><b class="b2">2</b>
   </li>

   <li><a href="http://www.4493.com/siwameitui/50075/1.htm" target="_blank"><img src="http://img.1985t.com/uploads/previews/2015/10/0-jMq6cQ.jpg" alt="复古式旗袍气质美女美腿暴露" /><span>复古式旗袍气质美女美腿暴露</span></a><b class="b1">2015-10-30</b><b class="b2">21</b></li><li><a href="http://www.4493.com/siwameitui/50041/1.htm" target="_blank"><img src="http://img.1985t.com/uploads/previews/2015/10/0-sKrFob.jpg" alt="黑丝袜美腿少女私房展现极好身材" /><span>黑丝袜美腿少女私房展现极好身材</span></a><b class="b1">2015-10-29</b><b class="b2">64</b></li><li><a href="http://www.4493.com/siwameitui/50039/1.htm" target="_blank"><img src="http://img.1985t.com/uploads/previews/2015/10/0-0RJMPP.jpg" alt="护士美女私房大秀美腿性感诱人" /><span>护士美女私房大秀美腿性感诱人</span></a><b class="b1">2015-10-29</b><b class="b2">35</b></li><li><a href="http://www.4493.com/siwameitui/50034/1.htm" target="_blank"><img src="http://img.1985t.com/uploads/previews/2015/10/0-uRMA7t.jpg" alt="高跟旗袍美女私房大秀美腿自信满满" /><span>高跟旗袍美女私房大秀美腿自信满满</span></a><b class="b1">2015-10-29</b><b class="b2">18</b></li><li><a href="http://www.4493.com/siwameitui/49942/1.htm" target="_blank"><img src="http://img.1985t.com/uploads/previews/2015/10/0-jzfUHk.jpg" alt="温雅气质女郎丝袜旗袍性感写真" /><span>温雅气质女郎丝袜旗袍性感写真</span></a><b class="b1">2015-10-29</b><b class="b2">14</b></li><li><a href="http://www.4493.com/siwameitui/49818/1.htm" target="_blank"><img src="http://img.1985t.com/uploads/previews/2015/10/0-d2AvqU.jpg" alt="美女制服网袜蕾丝写真合集" /><span>美女制服网袜蕾丝写真合集</span></a><b class="b1">2015-10-27</b><b class="b2">24</b></li><li><a href="http://www.4493.com/siwameitui/49816/1.htm" target="_blank"><img src="http://img.1985t.com/uploads/previews/2015/10/0-n54TdF.jpg" alt="制服美眉闺房里丝袜美腿自拍" /><span>制服美眉闺房里丝袜美腿自拍</span></a><b class="b1">2015-10-27</b><b class="b2">13</b></li><li><a href="http://www.4493.com/siwameitui/49813/1.htm" target="_blank"><img src="http://img.1985t.com/uploads/previews/2015/10/0-qLXj7X.jpg" alt="韩国气质车模黑色短裙优雅迷人" /><span>韩国气质车模黑色短裙优雅迷人</span></a><b class="b1">2015-10-27</b><b class="b2">14</b></li><li><a href="http://www.4493.com/siwameitui/49738/1.htm" target="_blank"><img src="http://img.1985t.com/uploads/previews/2015/10/0-ZSLER7.jpg" alt="性感细腰美女秀出各种美腿姿势" /><span>性感细腰美女秀出各种美腿姿势</span></a><b class="b1">2015-10-26</b><b class="b2">32</b></li><li><a href="http://www.4493.com/siwameitui/49670/1.htm" target="_blank"><img src="http://img.1985t.com/uploads/previews/2015/10/0-vxPdvq.jpg" alt="麻辣教师上演制服丝袜诱惑" /><span>麻辣教师上演制服丝袜诱惑</span></a><b class="b1">2015-10-26</b><b class="b2">37</b></li><li><a href="http://www.4493.com/siwameitui/49606/1.htm" target="_blank"><img src="http://img.1985t.com/uploads/previews/2015/10/0-eHElJs.jpg" alt="beautyleg气质腿模丝袜写真" /><span>beautyleg气质腿模丝袜写真</span></a><b class="b1">2015-10-24</b><b class="b2">58</b></li><li><a href="http://www.4493.com/siwameitui/49567/1.htm" target="_blank"><img src="http://img.1985t.com/uploads/previews/2015/10/0-TWQXE4.jpg" alt="透视装美眉网袜勾人心魂" /><span>透视装美眉网袜勾人心魂</span></a><b class="b1">2015-10-24</b><b class="b2">91</b></li><li><a href="http://www.4493.com/siwameitui/49492/1.htm" target="_blank"><img src="http://img.1985t.com/uploads/previews/2015/10/0-5x0Ntf.jpg" alt="私房美眉情趣睡衣的魅惑" /><span>私房美眉情趣睡衣的魅惑</span></a><b class="b1">2015-10-23</b><b class="b2">55</b></li><li><a href="http://www.4493.com/siwameitui/49356/1.htm" target="_blank"><img src="http://img.1985t.com/uploads/previews/2015/10/0-lOwlNu.jpg" alt="beautyleg气质黑丝旗袍美女写真" /><span>beautyleg气质黑丝旗袍美女写真</span></a><b class="b1">2015-10-22</b><b class="b2">51</b></li><li><a href="http://www.4493.com/siwameitui/49345/1.htm" target="_blank"><img src="http://img.1985t.com/uploads/previews/2015/10/0-jBDzPa.jpg" alt="森系俏皮女仆衣橱内娇羞迷人" /><span>森系俏皮女仆衣橱内娇羞迷人</span></a><b class="b1">2015-10-22</b><b class="b2">27</b></li><li><a href="http://www.4493.com/siwameitui/49278/1.htm" target="_blank"><img src="http://img.1985t.com/uploads/previews/2015/10/0-yR3Gxj.jpg" alt="推女郎网袜私房写真火辣性感" /><span>推女郎网袜私房写真火辣性感</span></a><b class="b1">2015-10-21</b><b class="b2">35</b></li><li><a href="http://www.4493.com/siwameitui/49255/1.htm" target="_blank"><img src="http://img.1985t.com/uploads/previews/2015/10/0-ELTTLW.jpg" alt="美女护士Miso制服丝袜诱惑写真" /><span>美女护士Miso制服丝袜诱惑写真</span></a><b class="b1">2015-10-21</b><b class="b2">57</b></li><li><a href="http://www.4493.com/siwameitui/49250/1.htm" target="_blank"><img src="http://img.1985t.com/uploads/previews/2015/10/0-MKtrKg.jpg" alt="绝色美女黑白格子紧身裙美腿丝袜" /><span>绝色美女黑白格子紧身裙美腿丝袜</span></a><b class="b1">2015-10-21</b><b class="b2">25</b></li><li><a href="http://www.4493.com/siwameitui/49249/1.htm" target="_blank"><img src="http://img.1985t.com/uploads/previews/2015/10/0-qouilf.jpg" alt="丝袜女郎cos青春学生装诱惑制服写真" /><span>丝袜女郎cos青春学生装诱惑制服写真</span></a><b class="b1">2015-10-21</b><b class="b2">17</b></li><li><a href="http://www.4493.com/siwameitui/49152/1.htm" target="_blank"><img src="http://img.1985t.com/uploads/previews/2015/10/0-46GcLl.jpg" alt="嫩模子子木制服丝袜高跟性感写真" /><span>嫩模子子木制服丝袜高跟性感写真</span></a><b class="b1">2015-10-20</b><b class="b2">20</b></li><li><a href="http://www.4493.com/siwameitui/49103/1.htm" target="_blank"><img src="http://img.1985t.com/uploads/previews/2015/10/0-MSHwb9.jpg" alt="蓝色高跟制服美女私房秀出丝袜美腿" /><span>蓝色高跟制服美女私房秀出丝袜美腿</span></a><b class="b1">2015-10-19</b><b class="b2">126</b></li><li><a href="http://www.4493.com/siwameitui/49094/1.htm" target="_blank"><img src="http://img.1985t.com/uploads/previews/2015/10/0-MULsfC.jpg" alt="白色蕾丝丝袜的丰满妹子小私房" /><span>白色蕾丝丝袜的丰满妹子小私房</span></a><b class="b1">2015-10-19</b><b class="b2">90</b></li><li><a href="http://www.4493.com/siwameitui/49052/1.htm" target="_blank"><img src="http://img.1985t.com/uploads/previews/2015/10/0-rTIhGl.jpg" alt="清新小美女私房丝袜写真" /><span>清新小美女私房丝袜写真</span></a><b class="b1">2015-10-19</b><b class="b2">0</b></li><li><a href="http://www.4493.com/siwameitui/49019/1.htm" target="_blank"><img src="http://img.1985t.com/uploads/previews/2015/10/0-vakAeE.jpg" alt="绝美气质模特丝袜写真很抢眼" /><span>绝美气质模特丝袜写真很抢眼</span></a><b class="b1">2015-10-17</b><b class="b2">0</b></li><li><a href="http://www.4493.com/siwameitui/48981/1.htm" target="_blank"><img src="http://img.1985t.com/uploads/previews/2015/10/0-LU4Uc2.jpg" alt="性感美女空姐丝袜美腿制服诱惑" /><span>性感美女空姐丝袜美腿制服诱惑</span></a><b class="b1">2015-10-17</b><b class="b2">32</b></li><li><a href="http://www.4493.com/siwameitui/48978/1.htm" target="_blank"><img src="http://img.1985t.com/uploads/previews/2015/10/0-nms0OZ.jpg" alt="性感少妇黑丝高跟私房沙发诱惑写真" /><span>性感少妇黑丝高跟私房沙发诱惑写真</span></a><b class="b1">2015-10-17</b><b class="b2">27</b></li><li><a href="http://www.4493.com/siwameitui/48885/1.htm" target="_blank"><img src="http://img.1985t.com/uploads/previews/2015/10/0-f9459p.jpg" alt="beautyleg气质美人儿丝袜写真" /><span>beautyleg气质美人儿丝袜写真</span></a><b class="b1">2015-10-16</b><b class="b2">37</b></li><li><a href="http://www.4493.com/siwameitui/48880/1.htm" target="_blank"><img src="http://img.1985t.com/uploads/previews/2015/10/0-DzBteh.jpg" alt="性感女郎情趣内衣上演迷人魅惑" /><span>性感女郎情趣内衣上演迷人魅惑</span></a><b class="b1">2015-10-16</b><b class="b2">34</b></li><li><a href="http://www.4493.com/siwameitui/48824/1.htm" target="_blank"><img src="http://img.1985t.com/uploads/previews/2015/10/0-JBIYbp.jpg" alt="beautyleg清纯腿模制服写真" /><span>beautyleg清纯腿模制服写真</span></a><b class="b1">2015-10-15</b><b class="b2">32</b></li></ul>
    <div class="page"><a href="./">上一页</a> <a class="current">1</a><a href="index-2.htm">2</a><a href="index-3.htm">3</a><a href="index-4.htm">4</a><a href="index-5.htm">5</a><a href="index-6.htm">6</a><a href="index-7.htm">7</a><a href="index-8.htm">8</a><a href="index-9.htm">9</a><a href="index-10.htm">10</a> <a href="index-2.htm">下一页</a></div>
    <!-- 广告位：4493_SG_660*85 -->
'''
class SockSpider(scrapy.Spider):
    name = "socks"   #siwameitui
    allowed_domains = ["www.4493.com", "img.1985t.com"]
    start_urls = [
        "http://www.4493.com/xingganmote/",
        "http://www.4493.com/siwameitui/",
        "http://www.4493.com/weimeixiezhen/",
        "http://www.4493.com/wangluomeinv/",
        "http://www.4493.com/gaoqingmeinv/",
        "http://www.4493.com/motemeinv/",
        "http://www.4493.com/tiyumeinv/",
        "http://www.4493.com/dongmanmeinv/",
    ]


    def parse(self, response):
        print response.url

        for sel in response.xpath('//div[@class="piclist"]/ul/li'):
            item = XiaoHuaItem()
            item['name'] = sel.xpath('.//a/span/text()').extract()
            item['rank'] = sel.xpath('.//b/text()').extract()
            item['school'] = ['']
            img_link = sel.xpath('.//a/img/@src').extract()[0]
            if img_link.startswith('http://'):
                item['image_urls'] = [img_link]
            else:
                item['image_urls'] = [response.urljoin(img_link)]
            yield item

            sub_url = sel.xpath('.//a/@href').extract()[0]

            yield Request(response.urljoin(sub_url), callback=self.parse_sub)

        '''
        <div class="page">
            <a href="index-9.htm">上一页</a>
            <a href="index-7.htm">7</a>
            <a href="index-8.htm">8</a>
            ...
            <a href="index-11.htm">下一页</a>
        </div>
        '''
        pagelist = response.xpath('//div[@class="page"]/a/@href')
        next_page = pagelist[-1].extract()
        print response.urljoin(next_page)
        yield Request(response.urljoin(next_page), callback=self.parse)


    '''
    http://www.4493.com/siwameitui/50167/9.htm

    <div class="picsbox picsboxcenter"><p>
    <img src="http://img.1985t.com/uploads/attaches/2015/11/50167-KUtr4K.jpg" alt="性感美女黑丝妩媚动人9" onload="btnaddress(1);" /></p>
    <a href="8.htm" class="pre">上一篇</a><a href="javascript:gotourl('9.htm');" class="next">下一篇</a>
        <script type="text/javascript">var randomnumber1=Math.floor(Math.random()*100000);document.write('<iframe id="meituiframe" name="meituiframe" style="display:none; border:0px; margin:0px auto; padding:0px; width:900px; height:544px; _height:564px;" src="/akcms_item.php?id=26959&itemid=50167&randomnumber='+randomnumber1+'" onload="btnfunc();"  frameborder="0" scrolling="no"></iframe>') ; </script>
        <script>function gotourl(url){var allnum=$('#allnum').text();var nownum=$('#nownum').text();if(nownum==allnum){$('.picsbox p').css('display','none');$('#meituiframe').css('display','block');$('.pre').add('.next').css('display','none');}else{window.location=url;}};function btnaddress(){var conheight = $('.picsboxcenter').height();var btntop	= conheight/2 - 31;$('.pre').add('.next').css('top',btntop);};function btnfunc(){$('#meituiframe').contents().find('.lastClose').click(function(){$('.picsbox p').css('display','block');$('#meituiframe').css('display','none');var conheight = $('.picsboxcenter').height();var btntop  = conheight/2 - 31;$('.pre').add('.next').css({'top':btntop,'display':'block'});});$('#meituiframe').contents().find('#replayPic').attr('href','/siwameitui/50167/1.htm');$('#meituiframe').contents().find('#enterPicSite').attr('href','/siwameitui/');};</script>
        <!-- 广告位：4493_SG_850*20 -->
<div class="adv96090" style="margin-top:10px;text-align: center;"><script type="text/javascript">BAIDU_CLB_fillSlot("680310");</script></div>
        </div>
        <div class="page"><a href="8.htm">上一篇</a>
        <a href="6.htm">6</a><a href="7.htm">7</a><a href="8.htm">8</a><a class="current">9</a>
        <a href="javascript:gotourl('9.htm');" id="nextpage">下一篇</a></div>
		<div class="picbottomline"><p class="pleft"><span>Tags:<a href="http://www.4493.com/tag/%BA%DA%CB%BF/" target="_blank">黑丝</a><a href="http://www.4493.com/tag/%E5%FC%C3%C4/" target="_blank">妩媚</a><a href="http://www.4493.com/tag/%C4%DA%D2%C2/" target="_blank">内衣</a></span></p><p class="pright"><span class="look"><i class="icon-eyes"></i><script type="text/javascript" src="/ajax_getnum.php?filed=pageview&id=50167"></script>+</span><span class="zan"><a href="javascript:like('50167');"><i class="icon-good"></i><b id="likes"><script type="text/javascript" src="/ajax_getnum.php?filed=likes&id=50167"></script></b>+ 赞</a></span></p></div>
    </div>
    '''
    def parse_sub(self, response):
        print response.url

        img_link = response.xpath('//div[@class="picsbox picsboxcenter"]/p/img/@src')
        item = XiaoHuaItem()
        item['image_urls'] = img_link.extract()
        item['name'] ='sb'
        item['rank'] = 'sb'
        item['school'] = 'sb'
        yield item

        sub_url = response.xpath('//a[@id="nextpage"]/@href').re(r'javascript:gotourl\(\'(.*?)\'\)')[0]
        yield Request(response.urljoin(sub_url), callback=self.parse_sub)


