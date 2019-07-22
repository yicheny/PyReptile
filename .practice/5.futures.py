import time,threading,requests
from concurrent.futures import ThreadPoolExecutor

start_time = time.time()
print('start')
urls = open('./source/proxypool.txt','r').read().split('\n')

def child_task(proxy):
    proxies = {
        'http': 'http://' + proxy,
        'https': 'https://' + proxy
    }
    try:
        res = requests.get('https://www.ipip.net/', proxies=proxies)
        print(res.status_code == 200)
    except requests.exceptions.ConnectionError as e:
        print("Error", e.args)

def run():
    executor = ThreadPoolExecutor(60)
    fs = []
    for v in urls:
        fs.append(executor.submit(child_task,v))
    executor.shutdown()

if __name__ == '__main__':
    t = threading.Thread(target=run)
    t.start()
    t.join()

    end_time = time.time()
    duration = end_time - start_time
    print('duraion',str(duration))

# 多线程使用总结
'''
1. 实例化线程: executor = ThreadPoolExecutor(num) #num表示并发线程数
2. 定义线程池 fs
3. 定义线程执行的函数，executor.submit(task,params) #task为执行的函数，params为函数参数
4. 将定义好的线程键入线程池中，fs.append(executor.submit(task,params))
5. 销毁线程池 executor.shutdown()
6. 执行以上 threading.Thread(target=run).start()

# 注意:
1. 默认会执行完主线程，再去执行多线程
> 让主线程等待其他线程，就是主线程会在join()处一直等待所有线程都结束之后，再继续运行
t = threading.Thread(target=run)
t.start()
t.join()
'''