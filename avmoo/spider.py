from PyReptile.avmoo.setting import START_URL,COMMON_URL,COMMON_URL_INFANTRY
from PyReptile.avmoo.utils import get_page,ReDispose
from PyReptile.common.mongoDB import MongoClient
from pyquery import PyQuery as pq
import re

finall_v = ReDispose.finall_v

class AvmooSpider():
    def __init__(self):
        self.db = MongoClient(db_name='avmoo',table_name='avmoo_stars')

    #  从演员列表进入演员详情页
    def star_home(self,url=START_URL):
        self.star = {
            'cavalry_movies':[],
            'infantry_movies':[]
        }
        res = get_page(url)
        if not res:
            print('演员列表页出错')
            return None
        res = pq(res)

        stars = res('#waterfall div.item') #获取到演员列表
        for star in stars:
            star = pq(star) #注意，这里一开始遍历出来的是原生HTML对象,所以需要使用pq转换
            self.star.update({
                'name':star('div.photo-info span').text(), #姓名
                'portrait':star('div.photo-frame img').attr('src'), #头像
                'url':star('a.avatar-box').attr('href') # 演员详情链接
            })
            # print(self.star)
            self.star_details(self.star['url'],self.star['name'])
            return None

        next = res('ul.pagination a[name="nextpage"]').attr('href')
        if next:
            url = COMMON_URL + next
            print(url)
            return self.star_home(url)
        else:
            print('爬取完成')
            return None

    # 进入影片列表页爬取——综合
    def star_details(self,url,name=''):
        res = get_page(url)
        if not res:
            print('综合影片列表页出错')
            return None
        res = pq(res)

        # 保存演员信息并进入步兵影片列表页
        avatar_box = pq(res('#waterfall div.item div.avatar-box div.photo-info'))
        if avatar_box:
            avatar_box_text = self.rinse_info(avatar_box.text())
            self.star.update({
                'birthday':finall_v(re.findall('生日: (.*)年龄',avatar_box_text)),
                'age':finall_v(re.findall('年龄: (.*)身高',avatar_box_text)),
                'height':finall_v(re.findall('身高: (.*)罩杯',avatar_box_text)),
                'cup':finall_v(re.findall('罩杯: (.*)胸围',avatar_box_text)),
                'circum':finall_v(re.findall('胸围: (.*)腰围',avatar_box_text)),
                'waistline':finall_v(re.findall('腰围: (.*)臀围',avatar_box_text)),
                'hipline':finall_v(re.findall('臀围: (.*)出生地',avatar_box_text)),
                'birthplace':finall_v(re.findall('出生地: (.*)爱好',avatar_box_text)),
                'interest':finall_v(re.findall('爱好: (.*)',avatar_box_text))
            })
            # print(self.star)
            url = avatar_box('a').attr('href')
            self.infantry_list(url,name)
            # return None

        # 进入骑兵详情页提取信息
        movie_box_list = pq(res('#waterfall div.item a.movie-box'))
        for movie in movie_box_list:
            url = pq(movie).attr('href')
            self.cavalry_movie_details(url)
            return None

        next = res('ul.pagination a[name="nextpage"]').attr('href')
        if next:
            url = COMMON_URL + next
            print(url)
            return self.star_details(url)
        else:
            self.db.add_one(self.star)
            print('%s骑兵影片爬取完成' % name)
            return None

        # self.cavalry_movie_details('https://avmoo.asia/cn/movie/931e9ffb52c3a526')
        # self.infantry_list('https://avsox.asia/cn/search/%E6%B3%A2%E5%A4%9A%E9%87%8E%E7%B5%90%E8%A1%A3',name)

    # 进入影片列表页爬取——步兵
    def infantry_list(self,url,name):
        res = get_page(url)
        if not res:
            print('步兵影片列表页出错')
            return None
        res = pq(res)

        movie_box_list = pq(res('#waterfall div.item a.movie-box'))
        for movie in movie_box_list:
            url = pq(movie).attr('href')
            self.infantry_movie_details(url)
            return None

        next = res('ul.pagination a[name="nextpage"]').attr('href')
        if next:
            url = COMMON_URL_INFANTRY + next
            return self.infantry_list(url,name)
        else:
            print('%s步兵影片爬取完成' % name)
            return None

    # 在骑兵影片详情页爬取信息
    def cavalry_movie_details(self,url):
        # print(url)
        res = get_page(url,type='save')

        if not res:
            print('骑兵影片详情页出错')
            return None
        res = pq(res)

        info = res('div.movie div.info')
        new_info = self.rinse_info(info.text())

        #参与演出的演员
        movie_stars = res('#avatar-waterfall .avatar-box')
        movie_star_list = []
        if movie_stars:
            for movie_star in movie_stars.items():
                movie_star_list.append({
                    'name': movie_star('span').text(),
                    'headImg':movie_star('img').attr('src') if movie_star('img') else None
                })
                break

        #影片样品【截图】
        movie_samples  = res('#sample-waterfall .sample-box')
        movie_sample_list = []
        if movie_samples:
            for movie_sample in movie_samples.items():
                movie_sample_list.append(movie_sample.attr('href'))
                # break

        self.star['cavalry_movies'].append({
            'movie_url': url,
            'movie_name': res('h3').text(),  # 影片名
            'movie_code': finall_v(re.findall('识别码:(.*)发行时间', new_info)),  # 识别码
            'movie_issue_date': finall_v(re.findall('发行时间:(.*)长度', new_info)),  # 发行时间
            'movie_time': finall_v(re.findall('长度:(.*)制作商', new_info)),  # 长度
            'movie_manufacturer': finall_v(re.findall('制作商:(.*)发行商', new_info)),  # 制作商
            'movie_publisher': finall_v(re.findall('发行商:(.*)类别', new_info)),  # 发行商
            'movie_type': pq(info)('span.genre').text(),  # 类别
            'movie_stars':movie_star_list,
            'movie_samples':movie_sample_list,
        })
        # print(self.star['cavalry_movies'])
        # print(self.star)
        return None

    # 在步兵影片详情页爬取信息——考虑和骑兵详情页爬取合并
    def infantry_movie_details(self, url):
        # print(url)
        res = get_page(url,type='save')

        if not res:
            print('步兵影片详情页出错')
            return None
        res = pq(res)

        info = res('div.movie div.info')
        new_info = self.rinse_info(info.text())

        # 参与演出的演员
        movie_stars = res('#avatar-waterfall .avatar-box')
        movie_star_list = []
        if movie_stars:
            for movie_star in movie_stars.items():
                movie_star_list.append({
                    'name': movie_star('span').text(),
                    'headImg': movie_star('img').attr('src') if movie_star('img') else None
                })
                # break

        # 影片样品【截图】
        movie_samples = res('#sample-waterfall .sample-box')
        movie_sample_list = []
        if movie_samples:
            for movie_sample in movie_samples.items():
                movie_sample_list.append(movie_sample.attr('href'))
                # break

        self.star['infantry_movies'].append({
            'movie_url': url,
            'movie_name': res('h3').text(),  # 影片名
            'movie_code': finall_v(re.findall('识别码:(.*)发行时间', new_info)),  # 识别码
            'movie_issue_date': finall_v(re.findall('发行时间:(.*)长度', new_info)),  # 发行时间
            'movie_time': finall_v(re.findall('长度:(.*)制作商', new_info)),  # 长度
            'movie_manufacturer': finall_v(re.findall('制作商:(.*)类别', new_info)),  # 制作商
            'movie_type': pq(info)('span.genre').text(),  # 类别
            'movie_stars': movie_star_list,
            'movie_samples': movie_sample_list
        })
        # print(self.star['infantry_movies'])
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