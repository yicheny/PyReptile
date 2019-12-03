from PyReptile.echartIssues.utils import get_page
from pyquery import PyQuery as pq
import re

startNum = 11773
endNum = 11773
commonUrl = 'https://github.com/apache/incubator-echarts/issues/'

def spider(issuseNum):
    while issuseNum <= endNum :
        url = commonUrl + str(issuseNum)
        request(url)
        issuseNum = issuseNum+1
    return print('结束',issuseNum)

def request(url):
    res = pq(get_page(url))
    issuesObj = {
        'title':res('span.js-issue-title').text(),
        'state':res('span.State').text(),
        'version':versionFor(res)
    }
    print(issuesObj)

def versionFor(res):
    version = re.search('<h3>Version</h3>\s<p>.+</p>',str(res))
    if version:
        return pq(version.group())('p').text()
    return None

if __name__ == '__main__':
    spider(startNum)

