import requests,time
from requests.adapters import HTTPAdapter

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
}
proxy = '39.137.69.10:80'
# proxy = requests.get('http://127.0.0.1:5050/random').text
# url = 'https://www.mzitu.com/188186'
url = 'http://httpbin.org/get'

start_time = time.time()

s = requests.Session()
# s.mount('http://',HTTPAdapter(max_retries=5))
# s.mount('https://',HTTPAdapter(max_retries=5))

# url = 'http://http.tiqu.alicdns.com/getip3?num=1&type=1&pro=&city=0&yys=0&port=1&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=&gm=4'


def get_content(url,proxy):
    proxies = {
        'http':'http://'+proxy,
        'https': 'https://' + proxy,
    }
    try:
        res = s.get(url, headers=headers,proxies=proxies)
        print(res.status_code)
    except Exception as e:
        print('Error',e)

def test_proxy_speed(num=1000):
    for i in range(num):
        print(requests.get('http://127.0.0.1:5050/random').text)

if __name__ == '__main__':
    get_content(url,proxy)

end_time = time.time()
print('运行时间:'+str(end_time-start_time))