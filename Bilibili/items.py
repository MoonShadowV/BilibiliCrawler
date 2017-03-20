# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BilibiliItem(scrapy.Item):
    aid = scrapy.Field()
    view = scrapy.Field()
    danmaku = scrapy.Field()
    reply = scrapy.Field()
    favorite = scrapy.Field()
    coin = scrapy.Field()

    #视频页面
    title = scrapy.Field()
    intro = scrapy.Field()

    label_1 = scrapy.Field()
    label_2 = scrapy.Field()
    label_3 = scrapy.Field()
    label_4 = scrapy.Field()
    label_5 = scrapy.Field()
    label_6 = scrapy.Field()
    label_7 = scrapy.Field()
    label_8 = scrapy.Field()
    label_9 = scrapy.Field()
    label_10 = scrapy.Field()
    pass
