import scrapy


class Quotes_Spider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response, **kwargs):
        all_div = response.xpath('//div[@class="quote"]')
        for quotes in all_div:
            text = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tags = quotes.css('.tag::text').extract()

            yield {
                'text': text,
                'author': author,
                'tag': tags
            }