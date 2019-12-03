from pyquery import PyQuery as pq
from PyReptile.echartIssues.utils import get_page

url = 'https://github.com/apache/incubator-echarts/issues/1'

def demo():
    res = pq(get_page(url))
    tags = res('div.Box a.link-gray-dark')
    tags = list(tags)
    hrefs = map(lambda tag:pq(tag).attr('href'),tags)
    print(list(hrefs))

if __name__ == '__main__':
    demo()
