from PyReptile.echartIssues.utils import get_page
from PyReptile.echartIssues.setting import DB_NAME,TABLE_NAME
from PyReptile.common.mongoDB import MongoClient
from pyquery import PyQuery as pq
import re

startNum = 11774
endNum = 11789
commonUrl = 'https://github.com/apache/incubator-echarts/issues/'

db = MongoClient(db_name=DB_NAME,table_name=TABLE_NAME)

def spider(issuseNum):
    while issuseNum <= endNum :
        url = commonUrl + str(issuseNum)
        request(url)
        issuseNum = issuseNum+1
    return print('结束',issuseNum)

def request(url):
    res = get_page(url)
    if not res: return print('跳过此错误页',url)

    res = pq(res)
    issuesObj = {
        'url':url,
        'title':res('span.js-issue-title').text(),
        'state':res('span.State').text(),
        'version':versionFor(res)
    }
    # print(issuesObj)
    db.add_one(issuesObj)

def versionFor(res):
    version = re.search('<h3>Version</h3>\s<p>.+</p>',str(res))
    if version:
        return pq(version.group())('p').text()
    return None

if __name__ == '__main__':
    spider(startNum)

