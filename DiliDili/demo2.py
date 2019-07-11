import requests
from bs4 import BeautifulSoup
import time
import xlwt
import os
from requests.adapters import HTTPAdapter
import datetime

# 标准网址格式http://www.dilidili.name/anime/urls/
# 获取所有的urls
# 1. 201001 - 201907
# 2. 2000xq
# 3. 2000xqq

start_time = datetime.datetime.now()

s = requests.Session()
s.mount('http://',HTTPAdapter(max_retries=15))
s.mount('https://',HTTPAdapter(max_retries=15))

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}

urls = ['2000xqq','2000xq']
datas = []
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
    try:
        wb_data = s.get(url, headers=headers,timeout=20)
        soup = BeautifulSoup(wb_data.text, 'lxml')
        links = soup.select('div.anime_list>dl>dd>h3>a')
        date = url.split('/')[-2]
        for link in links:
            href = link.get('href')
            get_info(href, date)
            # time.sleep(1)
    except ConnectionError:
        print('拒绝连接')


def get_value(v,*info):
    if isinstance(v,list):
        if(len(v)):
            if(info):
                return str(v[0].get(info[0]))+ " | " + str(v[0].text)
            else:
                return str(v[0].text)
        else:
            return '此项信息缺失'
    else:
        return '此项信息缺失'

i=0
def get_info(url,date):
    try:
        url = ['http://www.dilidili.name{}/'.format(url)][0]
        wb_data = s.get(url, headers=headers,timeout=20)
        soup = BeautifulSoup(wb_data.text, 'lxml')
        tit = soup.select('h1')
        bdy = soup.select('li.list_xz>a')
        data = {
            'tit': get_value(tit),
            'date': date,
            'bdy': get_value(bdy, 'href'),
            'url': url
        }
        datas.append(data)
        print('获取数据中...', len(datas),date,url)
    except ConnectionError:
        print('拒绝连接')

def save_to_execl(data,name,head):
    try:
        workbook = xlwt.Workbook(encoding='utf-8')
        sheet = workbook.add_sheet(name)
        for h in range(len(head)):
            sheet.write(0, h, head[h])

        i = 1
        for obj in data:
            j = 0
            for v in (obj.values()):
                sheet.write(i, j, v)
                j += 1
            i += 1
        workbook.save('%s\execl\\%s.xls' % (os.getcwd(),name))
        print('写入excel成功')
    except Exception:
        print('写入execl失败')


if __name__ == '__main__':
    getUrls('201001')
    print(len(urls),urls)
    urls = ['http://www.dilidili.name/anime/{}/'.format(url) for url in urls]
    for single_url in urls:
        get_links(single_url)
        # time.sleep(2)
    save_to_execl(datas,'DiliDili',['番名','日期','百度云链接','详情网址'])

    end_time = datetime.datetime.now()
    run_time = (end_time - start_time).seconds
    print('运行时间:' + str(run_time))