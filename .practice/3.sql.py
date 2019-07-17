import pymysql


def connect_db():
    print('连接到mySql服务器...')
    db = pymysql.connect(host='localhost', user='root', passwd='qazxsw', db='demo', port=3306, charset='utf8')
    # 参数详解
    '''
    host: ip地址
    user: 用户名（本地可填root）
    passwd: 密码
    db: 数据库名
    port: 端口
    charset: 编码方式（需要和数据库一致）
    '''
    return db


def create_table(db):
    # 获取操作游标
    cursor = db.cursor()

    # 如果存在表Demo则删除
    cursor.execute('DROP TABLE Demo')

    # 创建表Demo
    sql = '''
        CREATE TABLE Demo
          (
          Id int,
          LastName varchar(255),
          FirstName varchar(255),
          Address varchar(255),
          City varchar(255)
          )
    '''
    cursor.execute(sql)

def insert_db(db):
    cursor = db.cursor()

    sql = '''
        INSERT INTO Demo VALUES 
        ()
    '''

def main():
    db = connect_db()
    create_table(db)


if __name__ == '__main__':
    main()
