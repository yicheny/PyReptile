MYSQL_HOST = 'localhost'
MYSQL_DATABASE = 'demo'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'qazxsw'

TABLE_NAME = 'images'
INIT_KEYS = 'id,url,title,thumb'
# INIT_VALUES = '%s,%s,%s,%s'
DATA_VALUES = ['2b15246110568c23b2bc732c1723caf6', 'https://p0.ssl.qhimgs1.com/t01c8b7b000cdb7b044.jpg', '高山牧场,沃州,瑞士,欧洲', 'https://p0.ssl.qhimgs1.com/sdr/238__/t01c8b7b000cdb7b044.jpg']

import pymysql
class MySql(object):
    def __init__(self,host=MYSQL_HOST,user=MYSQL_USER,passwd=MYSQL_PASSWORD,db=MYSQL_DATABASE,port=MYSQL_PORT):
        self.client = pymysql.connect(host=host, user=user, passwd=passwd, db=db, port=port, charset='utf8')
        self.cursor = self.client.cursor()

    def create_table(self,table_name=TABLE_NAME):
        sql = 'CREATE TABLE %s (id varchar(255),url varchar(255),title varchar(255),thumb varchar(255))' % (table_name)
        self.cursor.execute(sql)

    def drop_table(self,table_name=TABLE_NAME):
        sql = 'DROP TABLE %s' % (table_name)
        self.cursor.execute(sql)

    def insert(self,table_name=TABLE_NAME,keys=INIT_KEYS,values=INIT_VALUES):
        sql = 'INSERT INTO %s (%s) VALUES ("A","B","C","D")' % (table_name,keys)
        # sql = 'INSERT INTO %s VALUES (%s)' % (table_name,keys)
        print(sql)
        self.cursor.execute(sql)
        self.client.commit()


if __name__ == '__main__':
    client = MySql()
    client.create_table()
    # client.drop_table()
    # client.insert()