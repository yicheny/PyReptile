# 查看ip是否可用
import requests

proxy = '101.4.136.34:8080'
proxies = {
    'http':'http://'+proxy,
    'https': 'https://' + proxy
}

try:
    res = requests.get('http://httpbin.org/get',proxies=proxies)
    print(res.text)
    # print(res.status_code==200)
except requests.exceptions.ConnectionError as e:
    print("Error",e.args)