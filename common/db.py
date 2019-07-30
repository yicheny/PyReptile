# 关于DB的一些操作
REDIS_PORT = 6379
DB = 6 # 6-mzitu 7-avmoo
REDIS_HOST = '127.0.0.1'
REDIS_PASSWORD = None
REDIS_KEY = 'default'

import redis

class RedisClient(object):
    def __init__(self,host=REDIS_HOST,port=REDIS_PORT,password=REDIS_PASSWORD,db=DB):
        self.db = redis.StrictRedis(host=host,port=port,password=password,decode_responses=True,db=db)

    #添加单个值
    def add(self,key=REDIS_KEY,value=''):
        self.db.sadd(key, value)

    #添加多个值
    def add_many(self,key=REDIS_KEY,list=[]):
        for i in list:
            self.add(key,i)

    #查询值是否在指定键中——键不存在时同样返回false
    def value_exists(self,key,name):
        return self.db.sismember(key,name)

    #获取指定集合中的所有值
    def all(self,name):
        return self.db.smembers(name)

if __name__ == '__main__':
    redis = RedisClient()
    # redis.add_many('mzitu_yet_urls',[1])
    # redis.exists('mzitu_yet_urls')
    # redis.value_exists('mzitu_yet_urls','https://www.mzitu.com/31201')
    # redis.all('mzitu_urls')
