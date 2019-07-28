from PyReptile.proxypool.setting import REDIS_PORT,DB
REDIS_HOST = '127.0.0.1'
REDIS_PASSWORD = None
REDIS_KEY = 'proxies'
MAX_SCORE = 100
MIN_SCORE = 0
INITIAL_SCORE = 10

import redis
from random import choice
from utils import PoolEmptyError

class RedisClient(object):
    def __init__(self,host=REDIS_HOST,port=REDIS_PORT,password=REDIS_PASSWORD,db=DB):
        self.db = redis.StrictRedis(host=host,port=port,password=password,decode_responses=True,db=db)

    def add(self,proxy,score=INITIAL_SCORE):
        self.db.zadd(REDIS_KEY,{proxy:score})

    def random(self):#优先选择最高分，如果不存在则随机选取
        result = self.db.zrangebyscore(REDIS_KEY,MAX_SCORE,MAX_SCORE)
        if len(result):
            return choice(result)
        else:
            result = self.db.zrangebyscore(REDIS_KEY,MIN_SCORE,MAX_SCORE)
            if(len(result)):
                return choice(result)
            else:
                raise PoolEmptyError

    def decrease(self,proxy):
        score = self.db.zscore(REDIS_KEY,proxy)
        if score>MIN_SCORE:
            return self.db.zincrby(REDIS_KEY,-1,proxy)
        else:
            return self.db.zrem(REDIS_KEY,proxy)

    def existe(self,proxy):
        return not self.db.zscore(REDIS_KEY,proxy) == None

    def set_max(self,proxy):
        return self.db.zadd(REDIS_KEY,{proxy:MAX_SCORE})

    def rem(self,proxy):
        self.db.zrem(REDIS_KEY,proxy)

    def count(self):
        return self.db.zcard(REDIS_KEY)

    def all(self):
        return self.db.zrangebyscore(REDIS_KEY,MIN_SCORE,MAX_SCORE)


# if __name__ == '__main__':
#     db = RedisClient()
    # db.set_max('ylf')
    # db.add('ylf',20)
    # db.add('ljf',30)
    # db.add('wyf',50)
    # db.add('mzw',40)
    # db.add('rl',100)
    # db.rem('rl')
    # print(db.all())
    # print(db.random())
    # print(db.existe('hhh'))
    # print(db.existe('ylf'))
    # print(db.decrease('ylf'))
