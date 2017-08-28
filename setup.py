#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-28 12:06:40
# @Author  : Wangmengcn (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$

from setuptools import setup, find_packages

setup(
    name="proxyhunter",
    version="0.0.1",
    keywords=("pip", "http", "http proxy"),
    description="free available http proxy from web",
    long_description="proxy hunter",
    license="MIT Licence",

    url="https://eclipsesv.com",
    author="wangmengcn",
    author_email="eclipse_sv@163.com",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=["requests", "lxml", "bs4"]
)
