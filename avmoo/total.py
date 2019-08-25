# 用于统计各种数据
import time
from PyReptile.common.mongoDB import MongoClient
from PyReptile.avmoo.setting import DB_NAME,TABLE_NAME

class DataTotal():
    def __init__(self):
        self.db = MongoClient(db_name=DB_NAME, table_name=TABLE_NAME)
        self.db2 = MongoClient(db_name=DB_NAME, table_name='avmoo_cavalry_movies')
        self.db3 = MongoClient(db_name=DB_NAME, table_name='avmoo_infantry_movies')
        self.infos = self.db.find({})
        # self.save_movies()

    def save_movies(self):
        for i in enumerate(self.infos):
            item = list(i)[1]
            self.db2.add_many(item['cavalry_movies'])
            self.db3.add_many(item['infantry_movies'])

if __name__ == '__main__':
    start_time = time.time()

    data = DataTotal()
    print('演员数目',data.db.count())
    # print('演员列表',data.db.distinct('name'))
    print('骑兵影片数目',data.db2.count())
    print('步兵影片数目',data.db3.count())
    print('影片总数目',data.db2.count() + data.db3.count())

    end_time = time.time()
    print('执行时间：' + str(end_time-start_time))
