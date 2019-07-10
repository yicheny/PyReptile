import requests
from bs4 import BeautifulSoup
import time

# 标准网址格式http://www.dilidili.name/anime/urls/
# 获取所有的urls
# 1. 201001 - 201907
# 2. 2000xq
# 3. 2000xqq

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}

urls = ['2000xqq','2000xq']
def getUrls(url):
    urls.append(url)
    url = int(url)
    url = url+3
    if(url>201907):
        return
        # return urls.extend(['2000xq','2000xqq'])
    else:
        start4 = int(str(url)[0:4])
        end2 = str(url)[-2:]
        if (int(end2) > 10):
            getUrls(str(start4+1) + '01')
        else:
            getUrls(str(url))

def get_links(url):
    wb_data = requests.get(url,headers=headers)
    soup = BeautifulSoup(wb_data.text,'lxml')
    links = soup.select('div.anime_list>dl>dd>h3>a')
    date = url.split('/')[-2]
    for link in links:
        href = link.get('href')
        get_info(href,date)

def get_info(url,date):
    url = ['http://www.dilidili.name{}/'.format(url)][0]
    wb_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    tit = soup.find('h1')
    bdy = soup.select('li.list_xz>a')

if __name__ == '__main__':
    getUrls('201001')
    urls = ['http://www.dilidili.name/anime/{}/'.format(url) for url in urls]
    for single_url in urls:
        get_links(single_url)
        time.sleep(2)