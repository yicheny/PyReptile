import grequests
import os
from bs4 import BeautifulSoup
import datetime
import re
from lxml import etree

start_time = datetime.datetime.now()

urls = []
url_common = 'https://www.biqukan.com/'

# f = open('./source/仙逆.txt','a+')

def get_urls(url):
    response = grequests.map([grequests.get(url)])[0]
    response.encoding='gb2312'
    # soup = BeautifulSoup(response.text, 'lxml')
    soup = etree.HTML(response.text)
    # print(soup)
    # links = soup.select('.listmain>dl>:nth-child(n+15)')
    links = soup.xpath('/html')
    print(links)
    # for v in links:
    #     urls.append(url_common + re.findall('href="(.*?)"',str(v))[0])
    # print(len(urls))

get_urls(url_common + '/1_1094/')

if __name__ == '__main__':
    # reqs = [grequests.get(o) for o in urls]
    # response = grequests.map(reqs, size=500)

    end_time = datetime.datetime.now()
    run_time = (end_time - start_time).seconds
    print('运行时间:' + str(run_time))
