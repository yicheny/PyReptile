import grequests, os, sys, re, datetime
from bs4 import BeautifulSoup
from lxml import etree

path = r'\\'.join(os.getcwd().split('\\')[0:-1]) + '\\common'
sys.path.append(path)
from method import save_to_execl

start_time = datetime.datetime.now()

urls = []
url_common = 'https://doupocangqiong1.com'
datas = []
none_data = {
    'tit': '此项信息缺失',
    'text': '此项信息缺失'
}


# f = open('./source/斗破苍穹.txt','a+')

def get_urls(url):
    response = grequests.map([grequests.get(url)])[0]
    # response.encoding='gb2312'
    soup = BeautifulSoup(response.text, 'lxml')
    # print(soup)
    links = soup.select('div.card.mt20.fulldir > div.body > ul > li > a')
    # print(links)
    for v in links:
        urls.append(url_common + re.findall('href="(.*?)"', str(v))[0])
    print(len(urls))


def get_info(html):
    if not html: return datas.append(none_data)
    soup = BeautifulSoup(html.text, 'lxml')
    print(soup)


if __name__ == '__main__':
    get_urls(url_common + '/1/')
    reqs = [grequests.get(o) for o in urls][0:10]
    response = grequests.map(reqs, size=100)

    for v in response:
        get_info(v)

    end_time = datetime.datetime.now()
    run_time = (end_time - start_time).seconds
    print('运行时间:' + str(run_time))
