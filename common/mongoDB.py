MONGO_URI = 'localhost'
DB_NAME = 'avmoo'#数据库名
TABLE_NAME = 'avmoo_stars'#表名
DB_PORT = 27017

import pymongo

class MongoClient(object):
    def __init__(self,host='localhost', port=DB_PORT,db_name=DB_NAME,table_name=TABLE_NAME):
        self.db = pymongo.MongoClient(host=host,port=port)[db_name]
        self.table = self.db[table_name]

    def change_table(self,table):
        self.table = self.db[table]

    def add_one(self,obj):
        self.table.insert_one(obj)

    def find(self,condition):
        return self.table.find(condition)

    def find_one(self,condition):
        return self.table.find_one(condition)



mockData = {
    'name':'lihua',
    'age':28
}
mockData2 = {
    'name':'lihua',
    'age':319
}
if __name__ == '__main__':
    db = MongoClient()
    db.add_one(mockData)
    db.add_one(mockData2)
    print(db.find_one({'name':'huahuahua'}))
    res = db.find({'name':'huahuahua'})
    print(41,res)
    for i in res:
        print(43,i)