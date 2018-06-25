# !/usr/bin/python
# --coding:utf-8--#
# -------------------------------------------------------------------------------
# Name:        tyc_test
# Author:      ZCC
# Created:     01/08/2018
# -------------------------------------------------------------------------------

"""
pycurl.HTTPHEADER替换方式：
1.使用Chrome进入开发者模式
2.点击Network
3.查看require.js中的Headers，Request Headers中Cookie
4.复制Cookie信息进行替换
5.出现失败处理方案：点开失败链接查看，如果被反爬虫，进入http://60.205.170.141:6007/user-status，手机页面wap把当前手机号加入添加白名单
"""

import pycurl
import time
import certifi


class Test:
    def __init__(self):
        self.contents = ''

    def body_callback(self, buf):
        self.contents = self.contents + buf


start_time = time.time()
with open("D:\pycharm\workspace\python\online_check\data\wap.txt", "r") as f:
    for i in f:
        url = i.strip()
        # url = "https://m.tianyancha.com/company/22822"
        t = Test()
        c = pycurl.Curl()
        c.setopt(pycurl.HTTPHEADER, [
            "cookie: cookie: aliyungf_tc=AQAAAALXdkmEEg4Ahi702nTL1zm9IJ29; csrfToken=sVRBXAg2VEoM-oOJEv7rlOGV; "
            "ssuid=1169852836; TYCID=68d4d6e02c1311e8ab4dff7472e2c862; undefined=68d4d6e02c1311e8ab4dff7472e2c862; "
            "UM_distinctid=16242704ad3109-00635fd9beee4e-326d7a05-1fa400-16242704ad49aa; bannerFlag=true; "
            "Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1524377091,1524822576,1524827312,1524833085; "
            "Hm_lvt_d5ceb643638c8ee5fbf79d207b00f07e=1524838483; Hm_lpvt_d5ceb643638c8ee5fbf79d207b00f07e=1524838483; "
            "RTYCID=1ad7582a566a46f684074e3b16cd81af; token=c14e4c2a47904077889cb8055695f71f; "
            "_utm=1098937e38c24153833dc637ca21d498; cid=2352954401; ss_cidf=1; "
            "tyc-user-info=%257B%2522isExpired%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9"
            ".eyJzdWIiOiIxMzgxMTU2NzUyNiIsImlhdCI6MTUyNDkwNjMyNiwiZXhwIjoxNTQwNDU4MzI2fQ.rCsrDYDtZ9U7Ut"
            "-TSaa5ziOaTS_Sy6_j450UDXO18YVNw5AZvvdqvfHDl_xJzy0-AkTlCQPHAp2Ui0CfSKNSyA%2522%252C%2522integrity%2522"
            "%253A%25220%2525%2522%252C%2522state%2522%253A%25227%2522%252C%2522surday%2522%253A%25221095%2522%252C"
            "%2522redPoint%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522vnum%2522%253A"
            "%252250%2522%252C%2522onum%2522%253A%25225%2522%252C%2522mobile%2522%253A%252213811567526%2522%257D; "
            "auth_token=eyJhbGciOiJIUzUxMiJ9"
            ".eyJzdWIiOiIxMzgxMTU2NzUyNiIsImlhdCI6MTUyNDkwNjMyNiwiZXhwIjoxNTQwNDU4MzI2fQ.rCsrDYDtZ9U7Ut"
            "-TSaa5ziOaTS_Sy6_j450UDXO18YVNw5AZvvdqvfHDl_xJzy0-AkTlCQPHAp2Ui0CfSKNSyA; "
            "Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1524906403"])
        c.setopt(pycurl.CAINFO, certifi.where())
        c.setopt(c.URL, url)
        c.setopt(c.WRITEFUNCTION, t.body_callback)
        c.perform()
        end_time = time.time()
        duration = end_time - start_time

        if c.getinfo(pycurl.HTTP_CODE) == 200 and len(t.contents) > 6000:
            print c.getinfo(pycurl.HTTP_CODE), c.getinfo(pycurl.EFFECTIVE_URL)
            c.close()
            print 'response time is %s' % duration  # 'pycurl takes %s seconds to get %s ' % (duration, url)
            print 'lenth of the content is %d\n' % len(t.contents)
        else:
            print "\033[1;31;40m %s is false!\033[0m" % url
            print 'lenth of the content is %d\n' % len(t.contents)
