import scrapy
from  PyReptile.Scrapy.demo.demo.items import DemoItem

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, res):
        quotes = res.css('.quote') # scrapy内置了css选择器、xPath选择器
        for quotes in quotes:
            item = DemoItem()
            item['text'] = quotes.css('.text::text').extract_first()
            item['author'] = quotes.css('.author::text').extract_first()
            item['tags'] = quotes.css('.tags .tag::text').extract()
            yield item

        next = res.css('.pager .next a::attr("href")').extract_first()
        url = res.urljoin(next) #urljoin方法可以将相对url构造为绝对url
        yield scrapy.Request(url=url,callback=self.parse)