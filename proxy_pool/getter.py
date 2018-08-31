# -*- coding: utf-8 -*-
"""
@Time   : 2018/8/26 16:44
@File   : getter.py
@Author : ZZShi
程序作用：
    调用Crawler类，将得到的代理保存到数据库
"""
from db import RedisClient
from crawler import Crawler
from config import *

import sys


class Getter(object):
    def __init__(self):
        self.db = RedisClient()
        self.crawler = Crawler()

    def is_over_threshold(self):
        if self.db.count() >= POOL_UPPER_THRESHOLD:
            return True
        else:
            return False

    def run(self):
        if not self.is_over_threshold():
            for callback_label in range(self.crawler.__CrawlFuncCount__):
                callback = self.crawler.__CrawlFunc__[callback_label]
                proxies = self.crawler.get_proxies(callback)
                sys.stdout.flush()
                for proxy in proxies:
                    self.db.add(proxy)


if __name__ == '__main__':
    g = Getter()
    g.run()
