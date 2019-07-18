import scrapy
from scrapy.selector import Selector
from scrapy_app.items import GoogleResultItem
from datetime import datetime

class GoogleSearchSpider(scrapy.Spider):
    name = 'googlesearch'
    allowed_domains = ['google.com']

    def __init__(self, keywords=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.keywords = keywords
        url = 'https://www.google.com.ua/search?q={}'.format(keywords)
        self.start_urls = [url]

    def parse(self, response):
        keywords = self.keywords
        title = response.xpath('//div[@class="BNeawe vvjwJb AP7Wnd"]/text()').extract()
        link = response.xpath('//div[@class="BNeawe UPmit AP7Wnd"]/text()').extract()  
        yield GoogleResultItem(title=title, link=link, keywords=keywords)

        # next_page = ''
        #     if next_page is not None:
        #         yield scrapy.Request(next_page, callback=self.parse)

            