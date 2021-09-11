import scrapy
from ..items import AmazonItem

class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    page_num = 75
    start_urls = ['https://www.amazon.com/s?i=stripbooks&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&page=1&']
    static_num = 2

    def parse(self, response, **kwargs):
        all_divs = response.xpath('//div[@class="s-result-item"]').extract()
        items = AmazonItem()
        num_links = response.css('.a-disabled+ .a-disabled::text').extract()
        _str = "".join(num_links)
        result = int(_str)

        title = response.css('.a-color-base.a-text-normal::text').extract()
        price = response.css('.a-spacing-top-small .a-price span span::text').extract()
        author = response.css('.a-color-secondary .a-row .a-size-base+ .a-size-base::text').extract()
        image_link = response.css('.s-image::text').extract()
        items['title'] = title
        items['price'] = price
        items['author'] = author
        items['image_url'] = image_link

        yield items

        next_page = 'https://www.amazon.com/s?i=stripbooks&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&page=' + str(AmazonSpider.static_num) + '&'

        if AmazonSpider.static_num <= result:
            AmazonSpider.static_num += 1
            yield response.follow(next_page, callback=self.parse)
