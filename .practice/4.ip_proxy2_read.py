import requests
from concurrent import futures

ips = open('./source/old_ips.txt','r').read().split('\n')
new_file = open('./source/new_ips.txt','a+',encoding='utf-8')
new_ips = []

def get_new_ips(proxy):
    proxies = {
        'http': 'http://' + proxy,
        'https': 'https://' + proxy
    }
    try:
        res = requests.get('http://httpbin.org/get', proxies=proxies)
        # print(res.text)
        print(res.status_code==200)
        if(res.status_code==200):
            new_ips.append(proxy)
    except requests.exceptions.ConnectionError as e:
        print("Error", e.args)

if __name__ == '__main__':
    for proxy in ips:
        get_new_ips(proxy)

    for ip in new_ips:
        new_file.write(ip)