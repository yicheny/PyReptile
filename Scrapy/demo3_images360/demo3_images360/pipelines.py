# # 通过MongoDB保存数据
# import pymongo
#
# class MongoPipeline(object):
#     def __init__(self,mongo_host,mongo_port,mongo_db):#执行顺序2
#         self.mongo_host = mongo_host
#         self.mongo_port = mongo_port
#         self.mongo_db = mongo_db
#
#     @classmethod
#     def from_crawler(cls,crawler): #执行顺序1
#         return cls(
#             mongo_host=crawler.settings.get('MONGO_HOST'),
#             mongo_db=crawler.settings.get('MONGO_DB'),
#             mongo_port=crawler.settings.get('MONGO_PORT')
#         )
#
#     def open_spider(self,spider): #执行顺序3
#         self.client = pymongo.MongoClient(host=self.mongo_host,port=self.mongo_port)
#         self.db = self.client[self.mongo_db]
#
#     def process_item(self,item,spider): #执行顺序4
#         self.db[item.collection].insert(dict(item))
#         return item
#
#     def close_spider(self,spider): #执行顺序5
#         self.client.close()

# 通过MySql保存
'''
注意，这里必须先创建数据和表，否则无法存储
- 新建数据库: CREATE  DATABASE  images360  DEFAULT  CHARACTER  SET  utf8  COLLATE  utf8_general  ci 
- 新建表:CREATE  TABLE  images  (id  VARCHAR(255)  PRIMARY  KEY,  url  VARCHAR(255)  NULL  ,  title VARCHAR(255)  NULL  , thumb  VARCHAR(255)  NULL) 
'''

import pymysql

class MysqlPipeline():
    def __init__(self,host,db,user,passwd,port):
        self.host = host
        self.db = db
        self.user = user
        self.passwd = passwd
        self.port = port

    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            host = crawler.settings.get('MYSQL_HOST'),
            db = crawler.settings.get('MYSQL_DATABASE'),
            user = crawler.settings.get('MYSQL_USER'),
            passwd = crawler.settings.get('MYSQL_PASSWORD'),
            port = crawler.settings.get('MYSQL_PORT')
        )

    def open_spider(self,spider):
        self.db = pymysql.connect(self.host,self.user,self.passwd,self.db,charset='utf8',port=self.port)
        self.cursor = self.db.cursor()

    def close_spider(self,spider):
        self.db.close()

    def process_item(self,item,spider):
        data = dict(item)
        keys = ','.join(data.keys())
        values = ','.join(['%s'] * len(data))

        sql = 'insert into %s (%s) values (%s)' % (item.table,keys,values)
        self.cursor.execute(sql,tuple(data.values()))
        self.db.commit()
        return item


# from scrapy import Request
# from scrapy.exceptions import DropItem
# from scrapy.pipelines.images import ImagesPipeline
#
# class ImagePipeline(ImagesPipeline):
#     def file_path(self,request,response=None,info=None):
#         url = request.url
#         file_name = url.split('/')[-1]
#         return file_name
#
#     def item_completed(self, results, item, info):
#         image_paths = [x['path'] for ok, x in results if ok]
#         if not image_paths:
#             raise DropItem('Image Download Failed')
#         return item
#
#     def get_media_requests(self, item, info):
#         yield Request(item['url'])


