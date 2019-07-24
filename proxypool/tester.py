# 测试器这里使用了aiohttp，需要了解下用法
VALID_STATUS_CODES = [200]
TEST_URL = 'http://www.dilidili.name' #用于测试的网站
BATCH_TEST_SIZE= 100 # 最大并发数量

from db import RedisClient
import aiohttp,asyncio,time
try:
    from aiohttp import ClientError
except:
    from aiohttp import ClientProxyConnectionError as ProxyConnectionError

class Tester(object):
    def __init__(self):
        self.redis = RedisClient()

    async def test_single_proxy(self,proxy):
        conn = aiohttp.TCPConnector(verify_ssl=False)
        async  with aiohttp.ClientSession(connector=conn) as session:
            try:
                if isinstance(proxy,bytes):
                    proxy = proxy.decode('utf-8')
                real_proxy = 'http://' + proxy
                print('正在测试',proxy)
                async with session.get(TEST_URL,proxy=real_proxy,timeout=15) as response:
                    if response.status in VALID_STATUS_CODES:
                        print('代理可用',proxy)
                        self.redis.set_max(proxy)
                    else:
                        print('请求响应码不合法',proxy)
                        self.redis.decrease(proxy)
            # except (ClientError, aiohttp.client_exceptions.ClientConnectorError,TimeoutError,AttributeError):
            except:
                self.redis.decrease(proxy)
                print('代理请求失败',proxy)

    def run(self):
        # print('测试器开始运行')
        try:
            proxies = self.redis.all()
            loop = asyncio.get_event_loop()
            for i in range(0,len(proxies),BATCH_TEST_SIZE):
                test_proxies = proxies[i:i + BATCH_TEST_SIZE]
                tasks = [self.test_single_proxy(proxy) for proxy in test_proxies]
                loop.run_until_complete(asyncio.wait(tasks))
                time.sleep(5)
        except Exception as e:
            print('测试器发生错误',e.args)

if __name__ == "__main__":
    test = Tester()
    test.run()

