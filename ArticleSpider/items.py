# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ArticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class CnblogsArticleItem(scrapy.Item):
    title = scrapy.Field()
    create_date = scrapy.Field()
    url = scrapy.Field()
    author = scrapy.Field()
    url_object_id = scrapy.Field()
