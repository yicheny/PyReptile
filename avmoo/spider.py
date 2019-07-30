from PyReptile.avmoo.setting import START_URL,COMMON_URL
from PyReptile.common.utils import get_page
from PyReptile.common.db import RedisClient
from pyquery import PyQuery as pq

class AvmooSpider():
    def __init__(self):
        self.db = RedisClient(db=7)

    #  从演员列表进入演员详情页
    def star_details(self,url=START_URL):
        # res = get_page(url)
        # if res:
        #     res = pq(res)
        # else:
        #     print('演员列表页出错',url)
        #     return None
        #
        # stars = res('#waterfall div.item') #获取到演员列表
        # for star in stars:
        #     star = pq(star) #注意，这里一开始遍历出来的是原生HTML对象,所以需要使用pq转换
        #     # print(star)
        #     star_portrait = star('div.photo-frame img').attr('src') #头像
        #     star_name = star('div.photo-info span').text() #姓名
        #     star_url = star('a.avatar-box').attr('href') # 演员详情链接
        #     # print(star_portrait,star_name,star_url)
        #     self.movie_details(star_url)
        #
        # next = res('ul.pagination a[name="nextpage"]').attr('href')
        # if next:
        #     url = COMMON_URL + next
        #     print(url)
        #     # return None
        #     return self.star_details(url)
        # else:
        #     print('爬取完成')
        #     return None

        self.movie_details('https://avmoo.asia/cn/star/5b8f99e09fb0f75a')

    # 进入影片详情页爬取——骑兵
    def movie_details(self,url):
        res = get_page(url)
        if res:
            res = pq(res)
        else:
            print('演员详情页错误',url)
            return None

        infantry = res('#waterfall div.item div.avatar-box div.photo-info a')
        if infantry:
            url = pq(infantry).attr('href')
            self.infantry_details(url)

        return None

    # 进入演员详情页爬取——步兵
    def infantry_details(self,url):
        print('步兵详情')

    def run(self):
        self.star_details()

if __name__ == '__main__':
    spider = AvmooSpider()
    spider.run()