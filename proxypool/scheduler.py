# 调度模块：以多进程定时运行其他模块

TESTER_CYCLE = 20  # Tester模块循环周期
GETTER_CYCLE = 20  # Getter模块循环周期
TESTER_ENABLED = True # Tester模块启动状态
GETTER_ENABLED = True # GETTER模块启动状态
API_ENABLED = True # API模块启动状态

from multiprocessing import Process
import time
from api import app
from getter import Getter
from tester import Tester

class Scheduler():
    def schedule_tester(self,cycle=TESTER_CYCLE):
        tester = Tester()
        while True:
            print('测试器开始运行')
            tester.run()
            time.sleep(cycle)

    def schedule_getter(self,cycle=GETTER_CYCLE):
        getter = Getter()
        while True:
            print('开始抓取代理')
            getter.run()
            time.sleep(cycle)

    def schedule_api(self):
        print('app开始运行')
        app.run()

    def run(self):
        print('代理池开始运行')
        if TESTER_ENABLED:
            tester_process = Process(target=self.schedule_tester())
            tester_process.start()
        if GETTER_ENABLED:
            getter_process = Process(target=self.schedule_getter())
            getter_process.start()
        if API_ENABLED:
            api_process = Process(target=self.schedule_api())
            api_process.start()


# if __name__ == '__main__':
#     scheduler = Scheduler()
#     scheduler.run()