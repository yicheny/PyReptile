import requests,datetime
from requests.adapters import HTTPAdapter

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}

start_time = datetime.datetime.now()

s = requests.Session()
s.mount('http://',HTTPAdapter(max_retries=15))
s.mount('https://',HTTPAdapter(max_retries=15))
url = 'https://www.biqukan.com/1_1094/5386271.html'

def get_content(url):
    res = s.get(url,headers=headers)
    res.encoding='gb2312'
    print(res.text)


if __name__ == '__main__':
    get_content(url)