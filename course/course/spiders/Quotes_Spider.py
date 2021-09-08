import scrapy
from ..items import CourseItem


class Quotes_Spider(scrapy.Spider):
    name = 'quotes'
    page_nom = 2
    start_urls = ['https://quotes.toscrape.com/page/1/']

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

        next_page = 'https://quotes.toscrape.com/page/'+str(Quotes_Spider.page_nom)+'/'

        if Quotes_Spider.page_nom < 11:
            Quotes_Spider.page_nom += 1
            response.follow(next_page, callback=self.parse)