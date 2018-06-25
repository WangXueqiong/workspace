#! /usr/bin/python
# coding=utf-8

import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6)

url = raw_input("请输入测试地址:")
driver.get("http://" + url.rstrip())

# s = '\'{}\''.format(url.rstrip())
# print s
# driver.get(s)
# driver.get("http://www.baidu.com")

# time.sleep(1)
# driver.find_element_by_link_text("新闻").click()
time.sleep(1)
print 'title: ' + driver.title  # title方法可以获取当前页面的标题显示的字段
descriptionValue = driver.find_element_by_xpath("//meta[@itemprop='description']")
print 'description: ' + descriptionValue.get_attribute("content")
keywordsValue = driver.find_element_by_xpath("//meta[@name='keywords']")
print 'keywords: ' + keywordsValue.get_attribute("content")
driver.quit()
