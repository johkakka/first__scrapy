import scrapy


class BaseballSpider(scrapy.Spider):
    name = 'baseball'
    allowed_domains = ['baseball.yahoo.co.jp']
    start_urls = ['https://baseball.yahoo.co.jp/npb/game/2021000214/score?index=0110100']

    def parse(self, response):

        pitcher = response.css('div#pit .nm a::text').extract_first()
        batter = response.css('div#batter .nm a::text').extract_first()

        print(pitcher+","+batter)
