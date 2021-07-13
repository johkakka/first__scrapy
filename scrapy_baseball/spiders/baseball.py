import scrapy

from scrapy_baseball.items import ScrapyBaseballItem


class BaseballSpider(scrapy.Spider):
    name = 'baseball'
    allowed_domains = ['baseball.yahoo.co.jp']
    start_urls = ['https://baseball.yahoo.co.jp/npb/game/2021000214/score?index=0110100']

    def start_requests(self):
        for i in range(100, 300):
            yield scrapy.Request('https://baseball.yahoo.co.jp/npb/game/2021000'+str(i)+'/score?index=0110100',
                                 callback=self.parse)

    def parse(self, response):
        result = []
        pitcher = response.css('div#pit .nm a::text').extract_first()
        batter = response.css('div#batter .nm a::text').extract_first()
        if pitcher is not None and batter is not None:
            yield ScrapyBaseballItem(pitcher = pitcher,
                                     batter = batter)

        link = response.css('a#btn_next::attr(href)').extract_first()
        if link is None:
            return result

        link = response.urljoin(link)
        yield scrapy.Request(link, callback=self.parse)

