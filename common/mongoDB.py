MONGO_URI = 'localhost'
DB_NAME = 'avmoo'  # 数据库名
TABLE_NAME = 'avmoo_stars'  # 表名
DB_PORT = 27017

import pymongo


class MongoClient(object):
    def __init__(self, host='localhost', port=DB_PORT, db_name=DB_NAME, table_name=TABLE_NAME):
        self.db = pymongo.MongoClient(host=host, port=port)[db_name]
        self.table = self.db[table_name]

    def change_table(self, table):
        self.table = self.db[table]

    def add_one(self, obj):
        self.table.insert_one(obj)

    def add_many(self, Arr):
        if(not len(Arr)): return None
        self.table.insert_many(Arr)

    def find(self, condition):
        return self.table.find(condition)

    def find_one(self, condition):
        return self.table.find_one(condition)

    def create_index(self, condition):
        return self.table.create_index(condition)

    def index_information(self):
        return self.table.index_information()

    def count(self):
        return self.table.count()

    def distinct(self,key):
        return self.table.distinct(key)

    def aggregate(self,pipeline):
        return self.table.aggregate(pipeline)

    # def list_indexes(self):
    #     return self.table.list_indexes()


mockData = {
    'name': 'lihua',
    'age': 28
}
mockData2 = {
    'name': 'lihua',
    'age': 319
}
mockData3 = [{
            'name': 'lj',
            'age': 234
        },
        {
            'name': 'df',
            'age':124
        }]
aggregateCond = [
    # {'$group':{'_id':None,'count':{'$sum':1}}}
    # {'$group':{'_id':'$cup','total':{'$sum':1}}}
    # {'$group':{'_id':'$age','total':{'$sum':1}}}
    # {'$group':{'_id':None,'total':{'$max':'$age'}}},
    # {'$group': {'_id': None, 'total': {'$min':'$age'}}}
]
if __name__ == '__main__':
    db = MongoClient(db_name='demo_db',table_name='demo_table')
    # db.add_many(mockData3)
    # db = MongoClient()
    # db.create_index('name')
    # print(db.count())
    # print(db.aggregate(aggregateCond).__dict__)
    # print(db.aggregate(aggregateCond)._CommandCursor__data)
    # print(db.distinct('name'))
    # db.add_one(mockData)
    # db.add_one(mockData2)
    # print(db.find_one({'name':'huahuahua'}))
    # res = db.find({'name':'huahuahua'})
    # print(41,res)
    # for i in res:
    #     print(43,i)
