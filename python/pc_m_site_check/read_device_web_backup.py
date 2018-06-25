#! /usr/bin/python
# coding=utf-8

import time
from selenium import webdriver
from tools.color_out import UseStyle

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6)

pc_site_rel_xpath = "//link[@rel='alternate']"
m_site_rel_xpath = "//link[@rel='canonical']"


def is_element_exist(xpath):
    s = driver.find_elements_by_xpath(xpath)
    if len(s) == 0:
        print "元素未找到:%s" % xpath
        return False
    elif len(s) == 1:
        return True
    else:
        print "找到%s个元素：%s" % (len(s), xpath)
        return False


with open("/Users/lishuang/Work/PythonProject/Selenium_Python/url_device2.txt", "r") as f:
    for i in f:
        url = i.strip()
        print UseStyle('get url: %s' % url, back='cyan')
        driver.get(url)
        time.sleep(3)

        device = driver.find_element_by_xpath("//meta[@name='applicable-device']")
        deviceTyc = driver.find_element_by_xpath("//meta[@name='tyc-device']")

        if url.__contains__('www.'):
            print '\npc_site: %s' % url
            if device.get_attribute("content") == 'pc':
                print 'device: ' + device.get_attribute("content")
                if is_element_exist(pc_site_rel_xpath):
                    wUrl = driver.find_element_by_xpath(pc_site_rel_xpath)
                    print 'pc_site_href: %s' % wUrl.get_attribute("href")
                else:
                    print 'pc_site  [%s] is error!' % url
            else:
                # 1高亮  31 红色   41黑色背景
                print UseStyle('device is error: %s' % device.get_attribute("content"), fore='red')
                # print '\033[1;31;40m;device is error: %s' % device.get_attribute("content")
        elif url.__contains__('m.'):
            print '\nm_site: %s' % url
            if device.get_attribute("content") == 'mobile':
                print 'device: %s' % device.get_attribute("content")
                if is_element_exist(m_site_rel_xpath):
                    mUrl = driver.find_element_by_xpath(m_site_rel_xpath)
                    print 'm_site_href: %s' % mUrl.get_attribute("href")
                else:
                    print 'm_site  [%s] is error!' % url
            else:
                print UseStyle('device is error: %s' % device.get_attribute("content"), fore='red')
                # print '\033[1;31;40m;device is error: %s' % device.get_attribute("content")
        else:
            print 'url is error！'
driver.quit()
