# -*- coding: utf-8 -*-
"""
@Time   : 2018/8/31 13:00
@File   : proxy.py
@Author : ZZShi
程序作用：
    提供两种调用方式，url调用和数据库调用
"""
from scheduler import Scheduler
from db import RedisClient


def start_pps():
    """
    启动Proxy Pool System
    启动之后可以访问'http://127.0.0.1:5000/random'调用随机可用代理
    :return:
    """
    s = Scheduler()
    s.run()


def get_proxy_from_db():
    """
    从数据库中获取可用代理
    :return:
    """
    r = RedisClient()
    return r.random()


if __name__ == '__main__':
    start_pps()
