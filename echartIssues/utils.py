import requests
from requests.adapters import HTTPAdapter


s = requests.Session()
s.mount('http://',HTTPAdapter(max_retries=5))
s.mount('https://',HTTPAdapter(max_retries=5))

base_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7'
}

def get_page(url,options={},type='text'):
    headers = dict(base_headers, **options)
    print('正在抓取...', url)
    try:
        response = s.get(url,headers=headers,timeout=10)
        print('抓取成功', url, response.status_code)
        if response.status_code == 200:
            if type=='content':
                return response.content
            else:
                return response.text
    except Exception:
        print('抓取失败', url)
        return None