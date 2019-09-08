# -*- coding: utf-8 -*-
import scrapy


class NetkeibaSpider(scrapy.Spider):
    name = 'netkeiba'
    allowed_domains = ['netkeiba.com']
    start_urls = ['http://netkeiba.com/']

    def parse(self, response):
        pass
