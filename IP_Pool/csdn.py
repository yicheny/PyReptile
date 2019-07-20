"""
该程序用于从代理网站获取可用ip
使用方法1： 直接运行该文件，会在同目录下生成ips.txt文件，文件内包含可用的代理
使用方法2： 其他程序导入该文件，然后直接使用该文件内定义的全局变量'proxies'
"""
import random
import threading
import time
from concurrent import futures

import requests
from pyquery import PyQuery

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) \
                  Chrome/53.0.2785.104 Safari/537.36 Core/1.53.2306.400 QQBrowser/9.5.10530.400'}
# 检测代理ip有效性的网站
CHECK_URL = 'https://ip.cn'
# 抓取地址(西刺代理)
FETCH_URL = 'http://www.xicidaili.com/wn/{}'
# 抓取页数，每页100条
PAGES = 3
# 代理类型（http/https）
PROXY_TYPE = 'https'
# 有效代理ip列表
proxies = []
# 线程池，用于同时验证多个代理ip
POOL = futures.ThreadPoolExecutor(max_workers=50)


def add_proxy(proxy: str):
    """
    添加代理
    :param proxy: 代理ip+端口号
    :return:
    """
    try:
        r = requests.get(CHECK_URL, proxies={PROXY_TYPE: proxy}, timeout=30)
        print(PyQuery(r.content.decode()).find('#result').text(), '\n')

        if r.status_code == 200 and proxy not in proxies:
            proxies.append(proxy)
    except Exception as e:
        if proxy in proxies:
            proxies.remove(proxy)
        print(proxy, e)

def fetch_proxy():
    """
    抓取代理ip
    :return:
    """
    for page in range(1, PAGES + 1):
        r = requests.get(FETCH_URL.format(page), headers=headers)
        doc = PyQuery(r.content.decode('utf-8'))
        # 获取数据列表对应的table
        table = doc('#ip_list')
        # 获取table中除了表头以外的所有行
        rows = table('tr:nth-of-type(n+2)').items()
        # 提取每一行中的ip和端口号
        for row in rows:
            ip = row('td:nth-of-type(2)').text()
            port = row('td:nth-of-type(3)').text()
            proxy = ip + ':' + port
            # 在线程池中检测该代理是否可用
            POOL.submit(add_proxy, proxy)
        # 10秒钟后抓取下一页
        time.sleep(10)


def run():
    while True:
        try:
            fetch_proxy()
            print('有效代理：', proxies)
            # 将有效代理写入文件
            with open('ips.txt', 'w', encoding='utf-8') as f:
                f.write('\n'.join(proxies))
        except Exception as e:
            print(e)
        # 抓取一次之后休息一段时间，防止被屏蔽
        time.sleep(random.randint(100, 600))


# 启动抓取线程
threading.Thread(target=run).start()
