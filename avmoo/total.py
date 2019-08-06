# 用于统计各种数据
import time
from PyReptile.common.mongoDB import MongoClient
from PyReptile.avmoo.setting import DB_NAME,TABLE_NAME

class DataTotal():
    def __init__(self):
        self.db = MongoClient(db_name=DB_NAME, table_name=TABLE_NAME)
        infos = self.db.find({})  # 获取数据库信息
        self.stars = [] # 定义演员池
        self.cavalry_movies = []  # 定义骑兵影片池
        self.infantry_movies = []  # 定义步兵影片池
        for i, o in enumerate(infos):
            self.stars.append(o)
            self.cavalry_movies.extend(o['cavalry_movies'])
            self.infantry_movies.extend(o['infantry_movies'])

if __name__ == '__main__':
    start_time = time.time()

    data = DataTotal()
    print('演员数目',len(data.stars))
    print('骑兵影片数目',len(data.cavalry_movies))
    print('步兵影片数目',len(data.infantry_movies))

    end_time = time.time()
    print('执行时间：' + str(end_time-start_time))
