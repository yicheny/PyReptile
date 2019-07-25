MONGO_URI = 'localhost'
MONGO_DB = 'images360'

DB_NAME = 'images'
IMAGE_OBJ = {'id': '2b15246110568c23b2bc732c1723caf6',
 'thumb': 'https://p0.ssl.qhimgs1.com/sdr/238__/t01c8b7b000cdb7b044.jpg',
 'title': '高山牧场,沃州,瑞士,欧洲',
 'url': 'https://p0.ssl.qhimgs1.com/t01c8b7b000cdb7b044.jpg'}

import pymongo

# 通过MongoDB保存数据
class MongoDB(object):
    def __init__(self):
        self.client = pymongo.MongoClient(host='localhost', port=27017)
        self.db = self.client[DB_NAME]

    def print_res(self):
        res = self.db['cctv6'].insert(IMAGE_OBJ)
        print(res)

if __name__ == '__main__':
    client = MongoDB()
    client.print_res()



