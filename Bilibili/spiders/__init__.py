# Bilibili Crawler    Author:ShadowMoon
# -*- coding: utf-8 -*-


import scrapy
import json
from Bilibili.items import BilibiliItem

class BilibiliSpider(scrapy.Spider):
    name = "Bilibili"

    def start_requests(self):
        for i in range(1020000, 2020000):
            url = 'http://api.bilibili.com/archive_stat/stat?aid=' + str(i)
            yield scrapy.Request(url)

    def parse(self, response):
        js = json.loads(response.body)
        if js.has_key('data'):
            info = js['data']
            if info['view'] >= 10000 and info['view'] != 0 and info['danmaku'] > 10 and info['coin'] > 10:
                item = BilibiliItem()
                aid = str(response)[51:-1]
                item['aid'] = aid 
                item['view'] = info['view']
                item['danmaku'] = info['danmaku']
                item['reply'] = info['reply']
                item['favorite'] = info['favorite']
                item['coin'] = info['coin']
                url = 'http://www.bilibili.com/video/av'+str(aid)
                yield scrapy.Request(url,meta={'item':item},callback=self.parse2)
            else:
                print "View is lower than 10000,pass!"
        else:
            print "There is no data!"



    def parse2(self,response):
        judge =response.xpath("//div[@class='main-inner']")
        if judge == []:#判断视频页面是否还存在
            pass
        else:
            try:
                item = response.meta['item']
                title = response.xpath('//div[@class = "v-title"]/h1/text()').extract()
                item['title'] = str(title[0].encode('utf-8')).replace(',',' ')
                intro = response.xpath("//div[@class='intro']/div/text()").extract()
                item['intro'] = str(intro[0].encode('utf-8')).replace(',',' ')
                i = 0  # 标识量
                tags = response.xpath('//div[@class="v_info"]/div[1]/ul//li/a/text()').extract()
                for tag in tags:
                    if i < 10:
                        i += 1
                        m = 'label_' + str(i)
                        item[m] = tag
                    else:
                        pass
                yield item
            except:
                print "Can't crawl,trying to fix it!"















