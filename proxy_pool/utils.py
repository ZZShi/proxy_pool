# -*- coding: utf-8 -*-
"""
@Time   : 2018/8/26 15:26
@File   : utils.py
@Author : ZZShi
程序作用：
    实现网页抓取的通用方法
"""
import requests


def get_page(url):
    """
    抓取网页
    :param url: 代理网站链接
    :return:
    """
    hd = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)\
         Chrome/67.0.3396.62 Safari/537.36'
    }
    try:
        r = requests.get(url, headers=hd)
        r.raise_for_status()
        return r.text
    except Exception as e:
        print('失败链接：', url)
        print('失败原因：', e.args)
        return None
