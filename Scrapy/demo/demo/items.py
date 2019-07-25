# Item是保存爬取数据的容器——使用方法和dict类似，多了一些保护机制
import scrapy

class DemoItem(scrapy.Item):
    text = scrapy.Field() # 定义类型为scrapy.Field
    author = scrapy.Field()
    tags = scrapy.Field()
