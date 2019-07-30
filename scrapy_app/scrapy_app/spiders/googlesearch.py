import scrapy
from scrapy.selector import Selector
from scrapy_app.items import GoogleResultItem
from datetime import datetime
from scrapy.crawler import CrawlerProcess
from time import sleep

class GoogleSearchSpider(scrapy.Spider):
    name = 'googlesearch'
    allowed_domains = ['google.com']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.keywords = kwargs.get('keywords')
        self.num = int(kwargs.get('value'))
        self.page_num = 10
        self.positionID = 0
        self.count = 1
        # url = 'https://www.google.com.ua/search?q=odessa&ei=EoxAXaG2IoiHwPAP3s-P-Ag&start=90'
        url = 'https://www.google.com.ua/search?q={}'.format(self.keywords)
        self.start_urls = [url]

    def parse(self, response):
        with open(f'parse_{self.positionID}.html', 'wb') as file:
            file.write(response.body)
        keywords = self.keywords
        # positionID = /self.positionID
        title = response.xpath('//div[@class="BNeawe vvjwJb AP7Wnd"]/text()').extract()
        link = response.xpath('//div[@class="BNeawe UPmit AP7Wnd"]/text()').extract()
        for t, l in zip(title, link):
            li = l.split(" ")[0]
            if li[:8] != 'https://':
                li = 'https://'+li
            self.positionID += 1
            self.keywords = self.positionID
            if self.count <= self.num:
                print(self.count)
                self.count += 1
                yield GoogleResultItem(positionID=self.positionID, title=t, link=li, keywords=keywords) 

        page_link = response.xpath('//a/@href').extract()[-5]
        print(page_link)
        sleep(5)
        if page_link:
            page_link = 'https://www.google.com.ua' + page_link[:-7] + '{}'.format(self.page_num) + '&sa=N&ved='
            print(page_link)
            self.page_num += 10
            # yield scrapy.Request(page_link)
            return scrapy.Request(page_link)
