import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from PyReptile.Scrapy.demo4_crawlSpider.demo4_crawlSpider.items import IMGItem
import json

class MzituSpider(CrawlSpider):
    name = 'mzitu'
    allowed_domains = ['www.mzitu.com']
    start_urls = ['https://www.mzitu.com/']

    rules = (
        Rule(LinkExtractor(allow='https://www\.mzitu\.com/\.*',restrict_xpaths='//ul[@id="pins"]//li//span'), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths='//nav[@class="navigation pagination"]//a[contains(.,"下一页»")]')),
    )

    def parse_item(self, response):
        item = IMGItem()
        item['title'] = response.xpath('//h2[@class="main-title"]/text()').extract_first()
        item['url'] = response.url
        item['datetime'] = response.xpath('//div[@class="main-meta"]/span/text()').re_first('\d+-\d+-\d+\s\d+:\d+')
        item['source'] = response.xpath('//div[@class="main-image"]//img/@src').extract_first()
        item['website'] = '妹子图网'
        yield item

