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
            res = [False]*9
            battings_raw = raw.css('td.bb-statsTable__data--inning')
            for i in range(len(battings_raw)):
                r = battings_raw[i].css('div.bb-statsTable__dataDetail').extract_first()
                if r is not None:
                    res[i] = True
            print(res)


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

        pitcher_list = []
        tables = response.css('table.bb-scoreTable')
        team = True
        for table in tables:
            raws = table.css('tr.bb-scoreTable__row')
            no = 0

            for raw in raws:
                player = raw.css('td.bb-scoreTable__data--player a::text').extract_first()
                ip = raw.css('td.bb-scoreTable__data--score p::text').extract()[1]

                pitcher_list.append({
                    'player': player,
                    'no': no,
                    'team': team,
                    'ip': ip
                })
                no += 1

            no = 0
            team = False

        print(pitcher_list)
