from PyReptile.mzitu.setting import START_URL
from PyReptile.mzitu.utils import get_page
from PyReptile.common.db import RedisClient
import time,random
from lxml import etree

start_time = time.time()

class Urls():
    def __init__(self):
        self.urls = []

    # 首页是按时间更新链接的，优化思路如下：
    # 爬取页面链接，如果链接不存在数据中则添加到数据库，如果已存在则停止程序
    def get_urls(self,url=START_URL):
        result = etree.HTML(get_page(url))
        url_list = result.xpath('//ul[@id="pins"]//a/@href')
        self.urls.extend(url_list)
        next = result.xpath('//div[@class="nav-links"]/a[@class="next page-numbers"]/@href')
        if isinstance(next,list) and next[0]:
            time.sleep(random.uniform(0.3,1))
            self.get_urls(next[0])
        return self.urls

if __name__ == "__main__":
    redis = RedisClient()
    urls = Urls()
    urls_list = urls.get_urls()
    redis.add_many('mzitu_urls',urls_list)

    end_time = time.time()
    print(end_time - start_time)