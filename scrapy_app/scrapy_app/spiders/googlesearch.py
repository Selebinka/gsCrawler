import scrapy
from scrapy.selector import Selector
from scrapy_app.items import GoogleResultItem

class GoogleSearchSpider(scrapy.Spider):
    name = 'googlesearch'
    allowed_domains = ['google.com']

    def __init__(self, keywords=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.keywords = keywords
        url = 'https://www.google.com.ua/search?q={}'.format(keywords)
        self.start_urls = [url]

    def parse(self, response):
        item = GoogleResultItem()
        title = response.xpath('//div[@class="BNeawe vvjwJb AP7Wnd"]/text()').extract()
        link = response.xpath('//div[@class="BNeawe UPmit AP7Wnd"]/text()').extract()
        return GoogleResultItem(title=title, link=link)


            