import scrapy
import re

from scrapy_baseball.items import ScrapyBaseballItem


class BaseballSpider(scrapy.Spider):
    name = 'baseball'
    allowed_domains = ['baseball.yahoo.co.jp']
    start_urls = ['https://baseball.yahoo.co.jp/npb/game/2021000214/score?index=0110100']

    # -1:err 0:打数に含まれない 1:凡打 2:安打
    def get_result_code(self, batting_result):
        if batting_result is None:
            return -1
        elif re.compile("盗塁|ボール|空振り|見逃し").search(batting_result) and\
                not re.compile("三振").search(batting_result):
            return -1
        elif re.compile("犠打失|犠飛失|犠野").search(batting_result):
            return 1
        elif re.compile("安打|塁打").search(batting_result):
            return 2
        elif re.compile("四|死球|犠|妨|敬遠").search(batting_result):
            return 0
        else:
            return 1

    def start_requests(self):
        for i in range(100, 628):
            yield scrapy.Request('https://baseball.yahoo.co.jp/npb/game/2021000' + str(i) + '/score?index=0110100',
                                 callback=self.parse)

    def parse(self, response):
        pitcher = response.css('div#pit .nm a::text').extract_first()
        batter = response.css('div#batter .nm a::text').extract_first()
        batting_result = response.css('div#result span::text').extract_first()
        result = self.get_result_code(batting_result)

        print(batting_result, result)

        if pitcher is not None and batter is not None and result != -1:
            yield ScrapyBaseballItem(pitcher=pitcher,
                                     batter=batter,
                                     result=result)

        link = response.css('a#btn_next::attr(href)').extract_first()
        if link is None:
            return

        link = response.urljoin(link)
        yield scrapy.Request(link, callback=self.parse)

