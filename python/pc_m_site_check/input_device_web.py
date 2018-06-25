#! /usr/bin/python
# coding=utf-8

import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6)

url = raw_input("请输入不包含http或http的URL:")
driver.get("http://" + url.rstrip())

time.sleep(1)
device = driver.find_element_by_xpath("//meta[@name='applicable-device']")
deviceTyc = driver.find_element_by_xpath("//meta[@name='tyc-device']")


# wUrl = driver.find_element_by_xpath("html/head/link[1]")

# href = driver.find_element_by_xpath("//div[@id='u1']/a[2]").get_attribute('href')

if url.__contains__('www.'):
    if device.get_attribute("content") == 'pc,mobile':
        print 'device: ' + device.get_attribute("content")
        # wUrl = driver.find_element_by_xpath("//link[@rel='alternate']")
        # print wUrl.get_attribute("href")
    elif deviceTyc.get_attribute("content") == 'pc':
        print 'deviceTyc: ' + deviceTyc.get_attribute("content")
    print('当前访问设备是PC！')
elif url.__contains__('m.'):
    if device.get_attribute("content") == 'mobile':
        print 'device: ' + device.get_attribute("content")
        mUrl = driver.find_element_by_xpath("//link[@rel='canonical']")
        print mUrl.get_attribute("href")
    elif deviceTyc.get_attribute("content") == 'mobile':
        print 'deviceTyc: ' + deviceTyc.get_attribute("content")
    print('当前访问设备是Mobile！')
else:
    print '输入信息有误！'
driver.quit()
