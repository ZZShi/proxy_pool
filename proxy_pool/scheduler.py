# -*- coding: utf-8 -*-
"""
@Time   : 2018/8/26 21:24
@File   : scheduler.py
@Author : ZZShi
程序作用：
    实现获取器、测试器、API的调度
"""
import time
from multiprocessing import Process
from api import app
from getter import Getter
from tester import Tester
from config import *


class Scheduler(object):

    @staticmethod
    def scheduler_tester(cycle=TESTER_CYCLE):
        tester = Tester()
        while True:
            print('测试器开始运行：')
            tester.run()
            time.sleep(cycle)

    @staticmethod
    def scheduler_getter(cycle=GETTER_CYCLE):
        getter = Getter()
        while True:
            print('获取器开始运行：')
            getter.run()
            time.sleep(cycle)

    @staticmethod
    def scheduler_api():
        print('API可以调用：')
        app.run(host=API_HOST, port=API_PORT)

    def run(self):
        print('代理池开始运行：')
        if GETTER_ENABLE:
            getter_process = Process(target=self.scheduler_getter, name='getter_process')
            getter_process.start()
        if TESTER_ENABLE:
            tester_process = Process(target=self.scheduler_tester, name='tester_process')
            tester_process.start()
        if API_ENABLE:
            api_process = Process(target=self.scheduler_api, name='api_process')
            api_process.start()


if __name__ == '__main__':
    s = Scheduler()
    s.run()
