# -*- coding: utf-8 -*-
"""
@Time   : 2018/8/26 14:24
@File   : config.py
@Author : ZZShi
程序作用：
    代理池配置
"""
# Redis数据库地址
REDIS_HOST = 'localhost'
# Redis数据库端口
REDIS_PORT = 6379
# Redis登录密码，无填None
REDIS_PASSWORD = None
# Redis数据库键名
REDIS_KEY = 'proxies'

# 代理分数
MAX_SCORE = 100
MIN_SCORE = 0
INIT_SCORE = 10

# 代理池数量限制
POOL_UPPER_THRESHOLD = 5000

# 检查周期，设置为10分钟
TESTER_CYCLE = 60 * 10
# 获取周期，设置为1天
GETTER_CYCLE = 60 * 60 * 24

# 测试链接，建议抓哪个设置哪个
TEST_URL = 'http://www.baidu.com'
# 最大批测试量
BATCH_TEST_SIZE = 100

# API配置
API_HOST = '127.0.0.1'
API_PORT = 5000

# 开关
TESTER_ENABLE = True
GETTER_ENABLE = True
API_ENABLE = True
