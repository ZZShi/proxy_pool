# -*- coding: utf-8 -*-
"""
@Time   : 2018/8/26 20:34
@File   : tester.py
@Author : ZZShi
程序作用：
    测试类，测试得到的代理是否有效
"""
import asyncio
import aiohttp
import time
import sys
from db import RedisClient
from config import *


class Tester(object):

    def __init__(self):
        self.db = RedisClient()

    async def test_single_proxy(self, proxy):
        """
        使用异步请求库aiohttp对代理进行测试
        :param proxy:
        :return:
        """
        conn = aiohttp.TCPConnector(verify_ssl=False)
        async with aiohttp.ClientSession(connector=conn) as session:
            try:
                if isinstance(proxy, bytes):
                    proxy = proxy.decode('utf-8')
                real_proxy = 'http://' + proxy
                print('正在测试', proxy)
                async with session.get(TEST_URL, proxy=real_proxy, timeout=15, allow_redirects=False) as r:
                    if r.status == 200:
                        self.db.max(proxy)
                        print('代理可用：', proxy)
                    else:
                        self.db.exists(proxy)
                        print('状态码不合法：', proxy)
            except Exception as e:
                self.db.decrease(proxy)
                print('代理请求异常：', proxy)

    def run(self):
        try:
            count = self.db.count()
            print('当前剩余{}个代理'.format(count))
            for i in range(0, count, BATCH_TEST_SIZE):
                start = i
                stop = min(i + BATCH_TEST_SIZE, count)
                test_proxies = self.db.batch(start, stop)
                loop = asyncio.get_event_loop()
                tasks = [self.test_single_proxy(proxy) for proxy in test_proxies]
                loop.run_until_complete(asyncio.wait(tasks))
                sys.stdout.flush()  # 刷新缓冲区
                time.sleep(5)
        except Exception as e:
            print('测试器发生错误', e.args)


if __name__ == '__main__':
    t = Tester()
    t.run()
