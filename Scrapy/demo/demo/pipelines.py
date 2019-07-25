# 项目管道，当Item生成后，会在Pipeline进行处理,常用操作如下：

class DemoPipeline(object):
    def process_item(self, item, spider):
        return item
