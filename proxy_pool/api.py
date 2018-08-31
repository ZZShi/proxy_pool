# -*- coding: utf-8 -*-
"""
@Time   : 2018/8/26 21:12
@File   : api.py
@Author : ZZShi
程序作用：
    提供网页调用的接口
"""
from db import RedisClient
from flask import Flask, g


__all__ = ['app']
app = Flask(__name__)


def get_conn():
    if not hasattr(g, 'redis'):
        g.redis = RedisClient()
    return g.redis


@app.route('/')
def index():
    return '<h2>Welcome to Proxy Pool System</h2>'


@app.route('/random')
def get_proxy():
    conn = get_conn()
    return conn.random()


@app.route('/count')
def get_count():
    conn = get_conn()
    # 不能返回int型
    return str(conn.count())


if __name__ == '__main__':
    app.run()
