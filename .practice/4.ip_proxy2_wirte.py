import requests,random,time
from requests.adapters import HTTPAdapter
from pyquery import PyQuery as pq

s = requests.Session()
s.mount('http://',HTTPAdapter(max_retries=15))
s.mount('https://',HTTPAdapter(max_retries=15))

CHECK_URL = 'https://ip.cn'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}
proxy = '101.4.136.34:8080'
proxies = {
    'http':'http://'+proxy,
    'https': 'https://' + proxy
}
common_url = 'http://www.89ip.cn'

f = open('./source/old_ips.txt','a+',encoding='utf-8')

def get_proxy_ip(url):
    res = s.get(url,headers=headers)
    doc = pq(res.text)#会转换为pq对象
    ip = doc('.layui-table tbody tr>td:nth-child(1)')
    port = doc('.layui-table tbody tr>td:nth-child(2)')
    for (i,v) in enumerate(ip):
        info = v.text.strip()+':'+port[i].text.strip() +'\n'
        print(info)
        # print('写入资源中...  ' + str(i))
        f.write(info)
    time.sleep(random.uniform(40,60))

if __name__ == '__main__':
    for i in range(1, 22):
        get_proxy_ip(common_url+'/index_%s.html' % i )

    print('执行结束!')
