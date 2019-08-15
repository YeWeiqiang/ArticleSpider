# -*- coding: utf-8 -*-
import datetime

import scrapy
from scrapy.http import Request
from urllib import parse

from ArticleSpider.items import CnblogsArticleItem, ArticleItemLoader
from ArticleSpider.utils.common import get_md5
from scrapy.loader import ItemLoader


class CnblogsSpider(scrapy.Spider):
    name = 'cnblogs'
    allowed_domains = ['www.cnblogs.com']
    start_urls = ['https://www.cnblogs.com/']

    def parse(self, response):
        post_urls = response.css('#post_list .post_item_body h3 a::attr(href)').extract()
        for post_url in post_urls:
            yield Request(url=post_url, callback=self.parse_detail)
            print(post_url)

        # pager_top > div > a:nth-child(12)
        # paging_block > div > a:nth-child(14)

        # 爬取下一页
        # next_url = response.css('#paging_block .pager a:last-child::attr(href)').extract_first()
        # if next_url:
        #     yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse)

    def parse_detail(selfs, response):
        article_item = CnblogsArticleItem()

        # title = response.css("#cb_post_title_url::text").extract()[0]
        # create_date = response.css('#post-date::text').extract()[0]
        # author = response.css('.postDesc a::text').extract()[0]
        # # 动态生成的，暂时爬取不了
        # view_count = response.css('#post_view_count::text').extract()[0]
        # comment_count = response.css('#post_comment_count::text').extract()[0]
        #
        # article_item["title"] = title
        # article_item["url"] = response.url
        # try:
        #     create_date = datetime.datetime.strptime(create_date, "%Y/%m/%d").date()
        # except Exception as e:
        #     create_date = datetime.datetime.now().date()
        # article_item["create_date"] = create_date
        # article_item["author"] = author
        # article_item["url_object_id"] = get_md5(response.url)

        # 通过item loader加载item
        item_loader = ArticleItemLoader(item=CnblogsArticleItem(), response=response)
        item_loader.add_css("title", '#cb_post_title_url::text')
        item_loader.add_css('create_date', '#post-date::text')
        item_loader.add_css('author', '.postDesc a::text')
        item_loader.add_value('url', response.url)

        article_item = item_loader.load_item()

        yield article_item
