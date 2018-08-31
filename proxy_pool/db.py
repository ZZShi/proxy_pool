# -*- coding: utf-8 -*-
"""
@Time   : 2018/8/26 14:35
@File   : db.py
@Author : ZZShi
程序作用：
    数据库类，实现数据库的增删查改
"""
import redis
from config import *
import re
from random import choice


class RedisClient(object):
    def __init__(self, host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD):
        """
        初始化
        :param host: Redis地址
        :param port: Redis端口
        :param password: Redis密码
        """
        self.db = redis.StrictRedis(host=host, port=port, password=password)

    def add(self, proxy, score=INIT_SCORE):
        """
        添加代理，设置分数为默认值10分
        :param proxy: 代理
        :param score: 分数
        :return: 添加结果
        """
        if not re.match(r'(\d+.){3}\d+:\d+', proxy):
            print('代理不符合规范：{}'.format(proxy))
        if not self.db.zscore(REDIS_KEY, proxy):
            return self.db.zadd(REDIS_KEY, score, proxy)

    def random(self):
        """
        若存在满分代理，则随机返回满分代理；若无，则随机返回；若代理池为空，报错
        :return:
        """
        result = self.db.zrangebyscore(REDIS_KEY, MAX_SCORE, MAX_SCORE)
        if result:
            return choice(result)
        else:
            result = self.db.zrevrange(REDIS_KEY, MIN_SCORE, MAX_SCORE)
            if result:
                return choice(result)
            else:
                print('代理池为空，请添加代理!!!')

    def decrease(self, proxy):
        """
        代理分值减1；若代理分数为0，则从数据库移除
        :param proxy: 代理
        :return:
        """
        score = self.db.zscore(REDIS_KEY, proxy)
        if score > MIN_SCORE:
            print('代理：{}\t\t分数减1\t\t分数：{}'.format(proxy, score - 1))
            return self.db.zincrby(REDIS_KEY, proxy, -1)
        else:
            print('代理：{}\t\t分数：{}\t\t删除'.format(proxy, score))
            return self.db.zrem(REDIS_KEY, proxy)

    def exists(self, proxy):
        """
        判断代理是否存在
        :param proxy:
        :return:
        """
        if self.db.zscore(REDIS_KEY, proxy):
            return True
        else:
            return False

    def max(self, proxy):
        """
        将代理分数设置为最高分
        :param proxy:
        :return:
        """
        print('代理：{}\t\t可以使用\t\t分数：{}'.format(proxy, MAX_SCORE))
        return self.db.zadd(REDIS_KEY, MAX_SCORE, proxy)

    def count(self):
        """
        统计数据库中代理的个数
        :return:
        """
        return self.db.zcard(REDIS_KEY)

    def all(self):
        """
        按分数排序返回所有代理
        :return:
        """
        return self.db.zrangebyscore(REDIS_KEY, MIN_SCORE, MAX_SCORE)

    def batch(self, start, stop):
        """
        获取索引范围内的代理列表
        :param start:
        :param stop:
        :return:
        """
        return self.db.zrevrange(REDIS_KEY, start, stop - 1)


if __name__ == '__main__':
    r = RedisClient()
    proxies = [
        '114.250.25.19:80',
        '118.190.210.227:3128',
        '218.60.8.99:3129'
    ]
    for proxy in proxies:
        r.add(proxy)
    print(r.random())
    r.decrease(proxy)
    print(r.exists(proxy))
    r.max('118.190.210.227:3128')
    print(r.count())
    print(r.all())