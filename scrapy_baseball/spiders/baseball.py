import scrapy
import re

class BaseballSpider(scrapy.Spider):
    name = 'baseball'
    allowed_domains = ['baseball.yahoo.co.jp']
    start_urls = ['https://baseball.yahoo.co.jp/npb/game/2021000214/stats']

    def parse(self, response):
        result_list = []

        print(result_list)
