import grequests
import requests
import os
from bs4 import BeautifulSoup
import datetime
import re
from lxml import etree
import json


def get_tits():
    url = 'https://doupocangqiong1.com/1/'
    res = requests.post(url,headers=headers)
    res.encoding = 'utf-8'
    selector = etree.HTML(res.text)
    tits = selector.xpath('/html/body/section/div[3]/div[2]/ul/li/a[@title]/text()')

def get_params_cid():
    print()

def get_urls():
    res = requests.post(content_url,params,headers=headers)
    info = json.loads(res.text)['info']
    info = re.sub('<br>','',info)
    print(info)

start_time = datetime.datetime.now()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}

params = {
    'siteid':0,
    'bid':1,
    'cid':873530 # 873530-875451
}

urls = []
content_url = 'https://doupocangqiong1.com/novelsearch/chapter/transcode.html'
tits = get_tits()

# f = open('./source/斗破苍穹.txt','a+')

if __name__ == '__main__':
    # get_tits()

    end_time = datetime.datetime.now()
    run_time = (end_time - start_time).seconds
    print('运行时间:' + str(run_time))
