# -*- coding: utf-8 -*-
"""
@Time   : 2018/8/26 15:24
@File   : crawler.py
@Author : ZZShi
程序作用：
    爬取代理网站并解析得到代理
"""
import re

from utils import get_page


class ProxyMetaclass(type):
    def __new__(mcs, name, bases, attrs):
        """
        将此类下所有函数名以'crawl_'开头的保存在['__CrawlFunc__']列表内
        :param name:
        :param bases:
        :param attrs:
        :return:
        """
        count = 0
        attrs['__CrawlFunc__'] = []
        for k, v in attrs.items():
            if 'crawl_' in k:
                attrs['__CrawlFunc__'].append(k)
                count += 1
        attrs['__CrawlFuncCount__'] = count
        return type.__new__(mcs, name, bases, attrs)


# 多添加几个免费代理网站
# 目前只添加了西刺代理和66ip
class Crawler(object, metaclass=ProxyMetaclass):

    def get_proxies(self, callback):
        proxies = []
        func = eval('self.{}'.format(callback))
        for proxy in func():
            print('得到代理：', proxy)
            proxies.append(proxy)
        return proxies

    @staticmethod
    def crawl_xicidaili():
        base_url = 'http://www.xicidaili.com/nn/'
        for page in range(1, 11):
            url = base_url + str(page)
            html = get_page(url)
            pattern = re.compile(r'<td>((\d+?.){3}\d+?)</td>\s*?<td>(\d+?)</td>', re.S)
            try:
                ips = re.finditer(pattern, html)
                for ip in ips:
                    yield '{}:{}'.format(ip.group(1), ip.group(3))
            except Exception as e:
                print('解析失败：', e.args)

    @staticmethod
    def crawl_66ip():
        base_url = 'http://www.66ip.cn/{}.html'
        for page in range(1, 11):
            url = base_url.format(page)
            html = get_page(url)
            pattern = re.compile(r'<tr><td>((\d+?.){3}\d+?)</td><td>(\d+?)</td><td>', re.S)
            try:
                ips = re.finditer(pattern, html)
                for ip in ips:
                    yield '{}:{}'.format(ip.group(1), ip.group(3))
            except Exception as e:
                print('解析失败：', e.args)

    @staticmethod
    def _test():
        """
        just test
        :return:
        """
        ips = []
        for ip in eval('self.crawl_66ip()'):
            print(ip)
            ips.append(ip)
        print(len(ips))


if __name__ == '__main__':
    c = Crawler()
    c._test()
