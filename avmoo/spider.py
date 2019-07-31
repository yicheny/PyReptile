from PyReptile.avmoo.setting import START_URL,COMMON_URL
from PyReptile.common.utils import get_page,ReDispose
from PyReptile.common.db import RedisClient
from pyquery import PyQuery as pq
import re

search_v = ReDispose.search_v
finall_v = ReDispose.finall_v

class AvmooSpider():
    def __init__(self):
        self.db = RedisClient(db=7)

    #  从演员列表进入演员详情页
    def star_home(self,url=START_URL):
        # res = get_page(url)
        # if not res:
        #     print('演员列表页出错')
        #     return None
        # res = pq(res)
        #
        # stars = res('#waterfall div.item') #获取到演员列表
        # for star in stars:
        #     star = pq(star) #注意，这里一开始遍历出来的是原生HTML对象,所以需要使用pq转换
        #     # print(star)
        #     star_portrait = star('div.photo-frame img').attr('src') #头像
        #     star_name = star('div.photo-info span').text() #姓名
        #     star_url = star('a.avatar-box').attr('href') # 演员详情链接
        #     # print(star_portrait,star_name,star_url)
        #     self.star_details(star_url,star_name)
        #
        # next = res('ul.pagination a[name="nextpage"]').attr('href')
        # if next:
        #     url = COMMON_URL + next
        #     print(url)
        #     # return None
        #     return self.star_home(url)
        # else:
        #     print('爬取完成')
        #     return None

        self.star_details('https://avmoo.asia/cn/star/26532bc87b4ce1d1')

    # 进入影片详情页爬取——综合
    def star_details(self,url,name=''):
        # res = get_page(url)
        # if not res:
        #     print('骑兵影片详情页出错')
        #     return None
        # res = pq(res)

        # avatar_box = pq(res('#waterfall div.item div.avatar-box div.photo-info'))
        # if avatar_box:
        #     avatar_box_text = avatar_box.text()
        #     star_birthday = search_v(re.search('生日: [^s]+',avatar_box_text))
        #     star_age = search_v(re.search('年龄: [^s]+',avatar_box_text))
        #     star_height = search_v(re.search('身高: [^s]+',avatar_box_text))
        #     star_cup = search_v(re.search('罩杯: [^s]+',avatar_box_text))
        #     star_circum = search_v(re.search('胸围: [^s]+',avatar_box_text))
        #     star_waistline = search_v(re.search('腰围: [^s]+',avatar_box_text))
        #     star_hipline = search_v(re.search('臀围: [^s]+',avatar_box_text))
        #     star_birthplace = search_v(re.search('出生地: [^s]+',avatar_box_text))
        #     star_interest = search_v(re.search('爱好: [^s]+',avatar_box_text))
        #
        #     # url = avatar_box('a').attr('href')
        #     # self.infantry_details(url)

        # movie_box_list = pq(res('#waterfall div.item a.movie-box'))
        # for movie in movie_box_list:
        #     url = pq(movie).attr('href')
        #     self.cavalry_movie_details(url)
        #     return None

        # return None
        self.cavalry_movie_details('https://avmoo.asia/cn/movie/931e9ffb52c3a526')

    # 进入演员详情页爬取——步兵
    def infantry_details(self,url):
        # print(url)
        print('步兵详情')

    # 进入骑兵影片详情页爬取信息
    def cavalry_movie_details(self,url):
        # print(url)
        res = get_page(url)

        if not res:
            print('骑兵影片详情页出错')
            return None
        res = pq(res)

        info = res('div.movie div.info')
        new_info = self.rinse_info(info.text())
        movie_name = res('h3').text() # 影片名
        movie_code = finall_v(re.findall('识别码:(.*)发行时间',new_info)) # 识别码
        movie_issue_date = finall_v(re.findall('发行时间:(.*)长度',new_info)) # 发行时间
        movie_time = finall_v(re.findall('长度:(.*)制作商',new_info)) # 长度
        movie_manufacturer = finall_v(re.findall('制作商:(.*)发行商',new_info)) # 制作商
        movie_publisher = finall_v(re.findall('发行商:(.*)类别',new_info)) # 发行商
        movie_type = pq(info)('span.genre').text() # 类别
        # print(movie_code,movie_issue_date,movie_time, movie_manufacturer,movie_publisher,movie_type)

        #参与演出的演员
        movie_star_list = res('#avatar-waterfall .avatar-box')

        #影片样品【截图】
        movie_sample  = res('#sample-waterfall .sample-box')

        return None

    # 清洗信息
    def rinse_info(self,info):
        if not info:
            return None
        newInfo = []
        for i in info.split('\n'):
            if i:newInfo.append(i.strip())
        return ''.join(newInfo)


    def run(self):
        self.star_home()

if __name__ == '__main__':
    spider = AvmooSpider()
    spider.run()