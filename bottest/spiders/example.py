import scrapy


class SQLSpider(scrapy.Spider):
    name = 'sql'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com/']

    def parse(self, response):
        pass
