import requests
import os
from bs4 import BeautifulSoup
import re
from lxml import etree
import json
import sys
from requests.adapters import HTTPAdapter
import datetime


sys.setrecursionlimit(10000) #python递归默认最大深度为997,超过则会报错
#注意，即使设的递归深度再大，也会受限于计算机本身的计算能力、系统版本、python版本等

start_time = datetime.datetime.now()

s = requests.Session()
s.mount('http://',HTTPAdapter(max_retries=15))
s.mount('https://',HTTPAdapter(max_retries=15))

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}

content_url = 'https://doupocangqiong1.com/novelsearch/chapter/transcode.html'
params = {
    'siteid':0,
    'bid':1,
    'cid':873530 # 873530-875451
}

def get_tits():
    url = 'https://doupocangqiong1.com/1/'
    res = requests.post(url,headers=headers)
    res.encoding = 'utf-8'
    selector = etree.HTML(res.text)
    tits = selector.xpath('/html/body/section/div[3]/div[2]/ul/li/a[@title]/text()')

params_cid = [(i) for i in range(873530,875452)]

def get_content(params):
    res = s.post(content_url,params,headers=headers)
    info = json.loads(res.text)['info']
    info = re.sub('<br>','',info)
    print(info)

# tits = get_tits()

# f = open('./source/斗破苍穹.txt','a+')

if __name__ == '__main__':


    end_time = datetime.datetime.now()
    run_time = (end_time - start_time).seconds
    print('运行时间:' + str(run_time))
