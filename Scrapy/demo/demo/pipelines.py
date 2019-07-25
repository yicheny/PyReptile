# 项目管道，当Item生成后，会在Pipeline进行处理,常用操作如下：
# 将爬取结果保存到数据库
# 清理HTML数据
# 验证爬取数据，检查爬取字段
# 查重并丢弃重复内容

from scrapy.exceptions import DropItem

class DemoPipeline(object):
    def __init__(self):
        self.limit = 50

    def process_item(self, item, spider):
        if item['text']:
            if len(item['text']) > self.limit:
                item['text'] = item['text'][0:self.limit].rstrip() + '...'
            return item
        else:
            return DropItem('Missing Text')
