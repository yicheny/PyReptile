YET_REDIS_KEY = 'mzitu_yet_urls'

from PyReptile.common.redisDB import RedisClient
from PyReptile.mzitu.utils import get_page,save_images
from lxml import etree
import time,re,random

start_time = time.time()

class GetImgs():
    def __init__(self):
        self.db = RedisClient()
        self.urls = self.db.all('mzitu_urls')
        # print(len(self.db.all('mzitu_urls')))
        # self.urls = (i for i in self.db.all('mzitu_urls'))

    def get_imgs(self):
        # for url in [list(self.urls)[1]]:
        for url in self.urls:
            # print(url)
            self.create_item(url)

    #逻辑待优化——已抓取的页面应停止对其抓取，但是下一页的请求应该继续
    def create_item(self,url):
        # if (re.search('https://www.mzitu.com/\d+/\d+',url) and self.db.value_exists(YET_REDIS_KEY,url)):
        if (self.db.value_exists(YET_REDIS_KEY,url)):
            print('该页面已抓取...')
            return None

        res = get_page(url)
        if res:
            res = etree.HTML(res)
        else:
            return None

        tit = res.xpath('//h2[@class="main-title"]//text()')
        img = res.xpath('//div[@class="main-image"]//img/@src')
        if (isinstance(img,list) and img[0]):
            if (isinstance(tit,list) and tit[0]):
                tit = re.search('\w+',tit[0]).group()
                save_images(path=img[0], referer=url, tit=tit)  # 这里最好使用正则检验下
            else:
                save_images(path=img[0], referer=url, tit='标题缺失')
            self.db.add(YET_REDIS_KEY, url)
        else:
            return None

        next = res.xpath('//div[@class="pagenavi"]/a[last()]/@href')
        if (isinstance(next,list) and next[0]):
            next_url = re.search('https://www.mzitu.com/\d+/\d+', next[0])
            if next_url:
                time.sleep(random.uniform(0,1))
                self.create_item(next_url.group())
            else:
                return None
        else:
            return None

if __name__ == '__main__':
    imgs = GetImgs()
    imgs.get_imgs()

    end_time = time.time()
    print('运行时间:'+str(end_time - start_time))
