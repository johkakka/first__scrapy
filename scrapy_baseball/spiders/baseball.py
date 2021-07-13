import scrapy


class BaseballSpider(scrapy.Spider):
    name = 'baseball'
    allowed_domains = ['baseball.yahoo.co.jp']
    start_urls = ['https://baseball.yahoo.co.jp/npb/game/2021000613/stats']

    def parse(self, response):
        result_list = []
        raws = response.css('tr.bb-statsTable__row')
        no = 0
        team = True

        for raw in raws:
            player = raw.css('td.bb-statsTable__data--player a::text').extract_first()

            if player is None:
                no = 0
                team = False
                continue

            result_list.append({
                'player': player,
                'no': no,
                'team': team
            })
            no += 1

        print(result_list)
