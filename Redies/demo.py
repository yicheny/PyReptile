from redis import  StrictRedis

redis = StrictRedis(host='localhost',port=6379,db=1,password=None)

# 字符串操作
print(redis.set('name','ylf'))
print(redis.get('name'))

# 有序集合操作
redis.zincrby('group',100,'bob')
print(redis.zcard('group'))
print(redis.zrank('group','bob'))
redis.zadd('group',{'bob':400,'mike':300})
