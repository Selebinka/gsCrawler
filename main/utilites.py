from scrapy.crawler import CrawlerProcess
# from scrapy_app.scrapy_app.spiders.googlesearch import GoogleSearchSpider

def crawl_spider(keywords=None, num=None):
    process = CrawlerProcess()
    process.crawl(GoogleSearchSpider, keywords=keywords, num=num)
    process.start()
