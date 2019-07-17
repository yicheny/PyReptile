import requests,datetime
from requests.adapters import HTTPAdapter
from lxml import etree


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}

start_time = datetime.datetime.now()

s = requests.Session()
s.mount('http://',HTTPAdapter(max_retries=15))
s.mount('https://',HTTPAdapter(max_retries=15))
url = 'https://www.qidian.com/all'

def get_content(url):
    res = s.get(url,headers=headers)
    html = etree.HTML(res.text)
    id = html.xpath('')
    # print(res.text)


if __name__ == '__main__':
    get_content(url)