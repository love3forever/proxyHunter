# proxyHunter
在用爬虫获取各类数据的时候，自己的ip经常会被网站ban掉。好在可以使用proxy解决这个问题。
一般情况下，使用免费代理就可以满足长期爬取数据的需求，现将我自己用过的代理网站整理一下，将代理提取的过程单独拿出来供以后使用。
## 用法
1. 安装
`   pip install proxyhunter`
2. 使用
```
    In [1]: from proxyhunter.huntingOn import Hunter

    In [2]: hunter = Hunter()

    In [3]: for proxy in hunter:
       ...:     print('proxy ip: {},port: {}'.format(*proxy))
       ...:
    waiting for new proxy
    waiting for new proxy
    GeoIP: China
    proxy ip: 111.13.7.42,port: 82
```