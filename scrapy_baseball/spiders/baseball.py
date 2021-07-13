import scrapy


class BaseballSpider(scrapy.Spider):
    name = 'baseball'
    allowed_domains = ['baseball.yahoo.co.jp']
    start_urls = ['https://baseball.yahoo.co.jp/npb/game/2021000613/stats']

    def parse(self, response):
        raws = response.css('tr.bb-statsTable__row')
        no = 0
        team = False

        top_batters = []
        btm_batters = []

        for raw in raws:
            player = raw.css('td.bb-statsTable__data--player a::text').extract_first()
            res = [0]*9
            battings_raw = raw.css('td.bb-statsTable__data--inning')
            for i in range(len(battings_raw)):
                r = battings_raw[i].css('div.bb-statsTable__dataDetail').extract_first()
                if r is not None:
                    h = battings_raw[i].css('div.bb-statsTable__dataDetail--hits').extract_first()
                    if h is not None:
                        res[i] = 1
                    else:
                        res[i] = -1

            if player is None:
                no = 0
                team = not team
                continue

            if team:
                top_batters.append({
                    'player': player,
                    'no': no,
                    'batting': res
                })
            else:
                btm_batters.append({
                    'player': player,
                    'no': no,
                    'batting': res
                })
            no += 1
        #
        # print(top_batters)
        # print(btm_batters)

        top_pitchers = []
        btm_pitchers = []
        tables = response.css('table.bb-scoreTable')
        team = True
        for table in tables:
            raws = table.css('tr.bb-scoreTable__row')
            no = 0

            for raw in raws:
                player = raw.css('td.bb-scoreTable__data--player a::text').extract_first()
                ip = raw.css('td.bb-scoreTable__data--score p::text').extract()[1]
                inning = int(float(ip))
                out = inning*3 + int(float(ip)*10 - inning*10)

                if team:
                    top_pitchers.append({
                        'player': player,
                        'no': no,
                        'ip': ip,
                        'out': out
                    })
                else:
                    btm_pitchers.append({
                        'player': player,
                        'no': no,
                        'ip': ip,
                        'out': out
                    })
                no += 1

            team = not team

