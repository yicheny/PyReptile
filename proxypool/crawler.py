from utils import get_page
from pyquery import PyQuery as pq

class ProxyMetaclass(type):
    def __new__(cls, name, bases, attrs):
        count = 0
        attrs['__CrawlFunc__'] = []
        for k,v in attrs.items():
            if 'crawl_' in k:
                attrs['__CrawlFunc__'].append(k)
                count += 1
        attrs['__CrawlFuncCount__'] = count
        return type.__new__(cls,name,bases,attrs)

class Crawler(object, metaclass=ProxyMetaclass):
    def get_proxies(self, callback):
        proxies = []
        for proxy in eval("self.{}()".format(callback)):
            print('成功获取到代理',proxy)
            proxies.append(proxy)
        return proxies

    def crawl_89ip(self, page_count=20):
        start_url = 'http://www.89ip.cn/index_{}.html'
        urls = [start_url.format(page) for page in range(1,page_count+1)]
        for url in urls:
            print('Crawling',url)
            html = get_page(url)
            if html:
                doc = pq(html)
                trs = doc('.layui-table tbody tr').items()
                for tr in trs:
                    ip = tr.find('td:nth-child(1)').text()
                    port = tr.find('td:nth-child(2)').text()
                    yield ':'.join([ip,port])

if __name__ == '__main__':
    crawl = Crawler()
    # x = crawl.crawl_89ip(1)
    # print(next(x))
    # print(next(x))
