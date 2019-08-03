import requests
from requests.adapters import HTTPAdapter
from PyReptile.common.mongoDB import MongoClient

s = requests.Session()
s.mount('http://',HTTPAdapter(max_retries=5))
s.mount('https://',HTTPAdapter(max_retries=5))

base_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7'
}

# 发送请求
db = MongoClient(db_name='avmoo',table_name='avmoo_faild_urls')
def get_page(url,options={},type=None):
    headers = dict(base_headers, **options)
    print('正在抓取...', url)
    try:
        response = s.get(url,headers=headers,timeout=30)
        print('抓取结果', url, response.status_code)
        if response.status_code == 200:
            return response.text
    except Exception:
        if(type=='save'):
            db.add_one(url)
            print('抓取失败,已存入数据库', url)
        print('抓取失败',url)
        return None


# 针对re返回的值进行一些处理
class ReDispose():
    @staticmethod
    def search_v(value):
        if value:
            return value.group()
        return ""

    @staticmethod
    def finall_v(f_list):
        if len(f_list):
            return f_list[0]
        return ""

import re
if __name__ == '__main__':
    search_v = ReDispose.search_v
    print(search_v(re.search('\d+','123-123-123')))