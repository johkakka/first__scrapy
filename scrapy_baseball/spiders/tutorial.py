import scrapy

class TutorialSpider(scrapy.Spider):
    name = 'tutorial'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/page/1/']

    def parse(self, response):
        result_list = []
        div_quotes = response.css('div.quote')
        for div_quote in div_quotes:
            span_text = div_quote.css('span.text::text').extract_first()
            quote = span_text.strip()
            author = div_quote.css('small.author::text').extract_first().strip()

            result_list.append({
                'quote': quote,
                'author': author
            })

        print(result_list)