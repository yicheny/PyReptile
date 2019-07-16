# post多进程请求
from multiprocessing import Process
import requests
import json
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}
params = {
    'siteid':0,
    'bid':1,
    'cid':873530 # 873530-875451
}
content_url = 'https://doupocangqiong1.com/novelsearch/chapter/transcode.html'

def get_text(params):
    res = requests.post(content_url,params,headers=headers)
    info = json.loads(res.text)['info']
    info = re.sub('<br>', '', info)
    print(info)

if __name__ == '__main__':
    get_text()