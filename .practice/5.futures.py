import time,threading,requests
from concurrent.futures import ThreadPoolExecutor,wait

start_time = time.time()
urls = open('./source/ip_pool.txt','r').read().split('\n')

def child_task(proxy):
    proxies = {
        'http': 'http://' + proxy,
        'https': 'https://' + proxy
    }
    try:
        res = requests.get('http://httpbin.org/get', proxies=proxies)
        print(res.status_code == 200)
    except requests.exceptions.ConnectionError as e:
        print("Error", e.args)

def run():
    executor = ThreadPoolExecutor(60)
    fs = []
    for v in urls:
        fs.append(executor.submit(child_task,v))

if __name__ == '__main__':
    threading.Thread(target=run).start()

    end_time = time.time()
    duration = end_time - start_time
    print(str(duration))

# 多线程使用总结
'''
1. 实例化线程: executor = ThreadPoolExecutor(num) #num表示并发线程数
2. 定义线程池 fs
3. 定义线程执行的函数，executor.submit(task,params) #task为执行的函数，params为函数参数
4. 将定义好的线程键入线程池中，fs.append(executor.submit(task,params))
5. 执行线程池 threading.Thread(target=run).start()
'''