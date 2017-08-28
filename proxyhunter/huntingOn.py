#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-28 09:09:04
# @Author  : Wangmengcn (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$
import time
import requests
from bs4 import BeautifulSoup
from itertools import cycle

test_url = 'http://ip.cn/'


class Hunter(object):
    """
    获取www.kuaidaili.com网站免费的可用proxy，
    用法：
        a = Hunter()
        for proxy in a:
            # 获取到的proxy均为已经过滤的proxy
            print proxy
    """

    def __init__(self):
        self._proxyurl = 'http://www.kuaidaili.com/ops/proxylist/{}/'
        self._proxytype = 'kdl_free'
        self._proxypool = None
        self._current_proxy = None
        self.proxies = dict()

    def gen_proxy(self):
        proxy_pool = self.gen_kdl_free()
        while True:
            for proxy in proxy_pool:
                if self.test_proxy():
                    yield self._current_proxy

    def gen_kdl_free(self):
        # 网站会持续刷新提供的proxy，所以在这里重复请求即可
        proxy_index = cycle(range(1, 11))
        for index in proxy_index:
            print('wating for new proxy')
            time.sleep(5)
            proxy_url = self._proxyurl.format(index)
            try:
                proxy_page = requests.get(proxy_url, timeout=5)
            except Exception as e:
                print(str(e))
            else:
                proxy_soup = BeautifulSoup(proxy_page.content, 'lxml')
                proxy_list = proxy_soup.select('.con-body')
                for item in proxy_list:
                    h2 = item.select('h2')
                    if h2 and u'免费高速HTTP代理IP列表' in h2[0].string:
                        proxies = item.select('tr')
                        for item in proxies[1:]:
                            info = item.select('td')
                            proxy_host = info[0].string
                            proxy_port = info[1].string
                            self._current_proxy = (proxy_host, proxy_port)
                            yield (proxy_host, proxy_port)

    def test_proxy(self):
        # 将获得的proxy通过'http://ip.cn/'测试，如果可用返回True
        if self._current_proxy:
            self.proxies['http'] = "http://{}:{}".format(*self._current_proxy)
            self.proxies['https'] = "http://{}:{}".format(*self._current_proxy)
            try:
                test_response = requests.get(
                    'http://ip.cn/', timeout=5, proxies=self.proxies)
            except Exception:
                return False
            else:
                if test_response.status_code == 200:
                    test_soup = BeautifulSoup(test_response.content, 'lxml')
                    ip_info = test_soup.select('.well')
                    if ip_info:
                        print(ip_info)
                        return True
                else:
                    return False

    def __iter__(self):
        self._proxypool = self.gen_proxy()
        return self

    def next(self):
        return next(self._proxypool)
