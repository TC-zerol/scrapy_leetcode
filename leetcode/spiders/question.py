# -*- coding: utf-8 -*-
import scrapy


class QuestionSpider(scrapy.Spider):
    name = 'question'
    allowed_domains = ['leetcode-cn.com']
    start_urls = ['http://leetcode-cn.com/']

    def parse(self, response):
        pass
