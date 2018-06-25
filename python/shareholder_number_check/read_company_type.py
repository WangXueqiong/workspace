#! /usr/bin/python
# coding=utf-8


import time

from selenium import webdriver

group_id_file = open("/Users/lishuang/Work/PythonProject/Selenium_Python/1.txt")

while 1:
    lines = group_id_file.readlines(100000)
    if not lines:
        break
    for line in lines:
        # print line
        print 'sss.tianyancha.com/company/%s?nav=nav-main-holderCount' % line
        # url = raw_input("请输入测试地址:")
        url = 'sss.tianyancha.com/company/%s?nav=nav-main-holderCount' % line
        browser = webdriver.Chrome()
        browser.maximize_window()  # 窗口最大化
        browser.get("http://" + url.rstrip())  # 在当前浏览器中访问百度
        time.sleep(1)
        print browser.title
        print '\n'
        browser.quit()


