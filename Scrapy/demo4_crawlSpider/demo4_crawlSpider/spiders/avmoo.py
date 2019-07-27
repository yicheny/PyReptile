import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class AvmooSpider(CrawlSpider):
    name = 'avmoo'
    allowed_domains = ['avmoo.asia/cn']
    start_urls = ['http://avmoo.asia/cn/actresses']

    rules = (
        Rule(LinkExtractor(allow='https://avmoo.asia/cn/star/.*',restrict_xpaths='//div[@id="waterfall"]//div[@class="item"]'), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths='//div[@class="pagination"//a[contains(.,"下一页")]'))
    )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
