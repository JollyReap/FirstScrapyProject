import scrapy
from ..items import CourseItem


class Quotes_Spider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response, **kwargs):
        items = CourseItem()
        all_div = response.xpath('//div[@class="quote"]')
        for quotes in all_div:
            text = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tags = quotes.css('.tag::text').extract()
            items['title'] = text
            items['author'] = author
            items['tag'] = tags

            yield items

        next_page = response.xpath('//li[@class="next"]/a/@href').get()

        if next_page is not None:
            response.follow(next_page, callback=self.parse)