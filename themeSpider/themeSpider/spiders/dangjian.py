# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup


class DangjianSpider(scrapy.Spider):
    name = 'dangjian'
    allowed_domains = ['dangjian.people.com.cn']
    start_urls = ['http://www.dangjian.people.com.cn/']

    def parse(self, response):
        pass
