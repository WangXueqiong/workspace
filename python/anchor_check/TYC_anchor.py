#!/usr/bin/env python
# -*- coding:utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        检查锚点定位测试
# Author:      lishuang
# Created:     04/28/2018
# -------------------------------------------------------------------------------

"""
获取每个维度的锚点并截图保存
"""

import os
import sys
from selenium import webdriver
import time

# 获取运行的文件所在的路径
rootpath = os.path.split(os.path.realpath(sys.argv[0]))[0]

# 指定位置
screenPath = rootpath + "/screen/"
# 如果不存在就创建目录
if not os.path.isdir(screenPath):
    os.mkdir(screenPath)

driver = webdriver.Chrome()
driver.get('http://www.tianyancha.com/company/22822?nav=nav-main-baseInfo')  # 基本信息
time.sleep(7)
# driver.save_screenshot('D:\untitled\picture\ 1.png')
driver.save_screenshot(screenPath + '1-基本信息.png')
print "1-基本信息,截图成功！"
driver.close()

driver = webdriver.Chrome()
driver.get('http://www.tianyancha.com/company/22822?nav=nav-main-graphInfo')  # 企业关系
time.sleep(5)
driver.save_screenshot(screenPath + '2-企业关系.png')
print "2-企业关系,截图成功！"
driver.close()

driver = webdriver.Chrome()
driver.get('http://www.tianyancha.com/company/22822?nav=nav-main-staffCount')  # 主要人员
time.sleep(5)
driver.save_screenshot(screenPath + '3-主要人员.png')
print "3-主要人员,截图成功！"
driver.close()

driver = webdriver.Chrome()
driver.get('http://www.tianyancha.com/company/22822?nav=nav-main-holderCount')  # 股东信息
time.sleep(5)
driver.save_screenshot(screenPath + '4-股东信息.png')
print "4-股东信息,截图成功！"
driver.close()

driver = webdriver.Chrome()
driver.get('http://www.tianyancha.com/company/22822?nav=nav-main-inverstCount')  # 对外投资
time.sleep(5)
driver.save_screenshot(screenPath + '5-对外投资.png')
print "5-对外投资,截图成功！"
driver.close()

driver = webdriver.Chrome()
driver.get('http://www.tianyancha.com/company/22822?nav=nav-main-changeCount')  # 变更记录
time.sleep(5)
driver.save_screenshot(screenPath + '6-变更记录.png')
print "6-变更记录,截图成功！"
driver.close()

driver = webdriver.Chrome()
driver.get('http://www.tianyancha.com/company/22822?nav=nav-main-reportCount')  # 企业年报
time.sleep(5)
driver.save_screenshot(screenPath + '7-企业年报.png')
print "7-企业年报,截图成功！"
driver.close()

driver = webdriver.Chrome()
driver.get('http://www.tianyancha.com/company/187782652?nav=nav-main-branchCount')  # 分支机构
time.sleep(5)
driver.save_screenshot(screenPath + '8-分支机构.png')
print "8-分支机构,截图成功！"
driver.close()

driver = webdriver.Chrome()
driver.get('http://www.tianyancha.com/company/22822?nav=nav-main-companyRongzi')  # 融资历史
time.sleep(5)
driver.save_screenshot(screenPath + '9-融资历史.png')
print "9-融资历史,截图成功！"
driver.close()

driver = webdriver.Chrome()
driver.get('http://www.tianyancha.com/company/22822?nav=nav-main-companyTeammember')  # 核心团队
time.sleep(5)
driver.save_screenshot(screenPath + '10-核心团队.png')
print "10-核心团队,截图成功！"
driver.close()

driver = webdriver.Chrome()
driver.get('http://www.tianyancha.com/company/22822?nav=nav-main-companyProduct')  # 企业业务
time.sleep(5)
driver.save_screenshot(screenPath + '11-企业业务.png')
print "11-企业业务,截图成功！"
driver.close()

driver = webdriver.Chrome()
driver.get('http://www.tianyancha.com/company/22822?nav=nav-main-jigouTzanli')  # 投资事件
time.sleep(5)
driver.save_screenshot(screenPath + '12-投资事件.png')
print "12-投资事件,截图成功！"
driver.close()

driver = webdriver.Chrome()
driver.get('http://www.tianyancha.com/company/22822?nav=nav-main-companyJingpin')  # 竞品信息
time.sleep(5)
driver.save_screenshot(screenPath + '13-竞品信息.png')
print "13-竞品信息,截图成功！"
driver.close()

driver = webdriver.Chrome()
driver.get('http://www.tianyancha.com/company/22822?nav=nav-main-lawsuitCount')  # 法律诉讼
time.sleep(5)
driver.save_screenshot(screenPath + '14-法律诉讼.png')
print "14-法律诉讼,截图成功！"
driver.close()

driver = webdriver.Chrome()
driver.get('http://www.tianyancha.com/company/22822?nav=nav-main-courtCount')  # 法院公告
time.sleep(5)
driver.save_screenshot(screenPath + '15-法院公告.png')
print "15-法院公告,截图成功！"
driver.close()

driver = webdriver.Chrome()
driver.get('http://www.tianyancha.com/company/829925009?nav=nav-main-dishonest')  # 失信人
time.sleep(5)
driver.save_screenshot(screenPath + '16-失信人.png')
print "16-失信人,截图成功！"
driver.close()

driver = webdriver.Chrome()
driver.get('http://www.tianyancha.com/company/22822?nav=nav-main-zhixing')  # 被执行人
time.sleep(5)
driver.save_screenshot(screenPath + '17-被执行人.png')
print "17-被执行人,截图成功！"
driver.close()

driver = webdriver.Chrome()
driver.get('http://www.tianyancha.com/company/1388479345?nav=nav-main-abnormalCount')  # 经营异常
time.sleep(5)
driver.save_screenshot(screenPath + '18-经营异常.png')
print "18-经营异常,截图成功！"
driver.close()

driver = webdriver.Chrome()
driver.get('http://www.tianyancha.com/company/2349303051?nav=nav-main-punishment')  # 行政处罚
time.sleep(5)
driver.save_screenshot(screenPath + '19-行政处罚.png')
print "19-行政处罚,截图成功！"
driver.close()

driver = webdriver.Chrome()
driver.get('http://www.tianyancha.com/company/1045368661?nav=nav-main-illegalCount')  # 严重违法
time.sleep(5)
driver.save_screenshot(screenPath + '20-严重违法.png')
print "20-严重违法,截图成功！"
driver.close()

driver = webdriver.Chrome()
driver.get('http://www.tianyancha.com/company/22822?nav=nav-main-equityCount')  # 股权出质
time.sleep(5)
driver.save_screenshot(screenPath + '21-股权出质.png')
print "21-股权出质,截图成功！"
driver.close()

driver = webdriver.Chrome()
driver.get('http://www.tianyancha.com/company/2335107427?nav=nav-main-mortgageCount')  # 动产抵押
time.sleep(5)
driver.save_screenshot(screenPath + '22-动产抵押.png')
print "22-动产抵押,截图成功！"
driver.close()

driver = webdriver.Chrome()
driver.get('http://www.tianyancha.com/company/22822?nav=nav-main-bidCount')  # 招投标
time.sleep(5)
driver.save_screenshot(screenPath + '23-招投标.png')
print "23-招投标,截图成功！"
driver.close()

driver = webdriver.Chrome()
driver.get('http://www.tianyancha.com/company/1208288762?nav=nav-main-ownTaxCount')  # 欠税公告
time.sleep(5)
driver.save_screenshot(screenPath + '24-欠税公告.png')
print "24-欠税公告,截图成功！"
driver.close()

driver = webdriver.Chrome()
driver.get('http://www.tianyancha.com/company/162113452?nav=nav-main-bondCount')  # 债券信息
time.sleep(5)
driver.save_screenshot(screenPath + '25-债券信息.png')
print "25-债券信息,截图成功！"
driver.close()

driver = webdriver.Chrome()
driver.get('http://www.tianyancha.com/company/2329261540?nav=nav-main-goudiCount')  # 购地信息
time.sleep(5)
driver.save_screenshot(screenPath + '26-购地信息.png')
print "26-购地信息,截图成功！"
driver.close()

driver = webdriver.Chrome()
driver.get('http://www.tianyancha.com/company/22822?nav=nav-main-recruitCount')  # 招聘
time.sleep(5)
driver.save_screenshot(screenPath + '27-招聘.png')
print "27-招聘,截图成功！"
driver.close()

driver = webdriver.Chrome()
driver.get('http://www.tianyancha.com/company/22822?nav=nav-main-taxCreditCount')  # 税务评级
time.sleep(5)
driver.save_screenshot(screenPath + '28-税务评级.png')
print "28-税务评级,截图成功！"
driver.close()

driver = webdriver.Chrome()
driver.get('http://www.tianyancha.com/company/22822?nav=nav-main-checkCount')  # 抽查检查
time.sleep(5)
driver.save_screenshot(screenPath + '29-抽查检查.png')
print "29-抽查检查,截图成功！"
driver.close()

driver = webdriver.Chrome()
driver.get('http://www.tianyancha.com/company/22822?nav=nav-main-productinfo')  # 产品信息
time.sleep(5)
driver.save_screenshot(screenPath + '30-产品信息.png')
print "30-产品信息,截图成功！"
driver.close()

driver = webdriver.Chrome()
driver.get('http://www.tianyancha.com/company/24416401?nav=nav-main-qualification')  # 资质证书
time.sleep(5)
driver.save_screenshot(screenPath + '31-资质证书.png')
print "31-资质证书,截图成功！"
driver.close()

driver = webdriver.Chrome()
driver.get('http://www.tianyancha.com/company/22822?nav=nav-main-tmCount')  # 商标信息
time.sleep(5)
driver.save_screenshot(screenPath + '32-商标信息.png')
print "32-商标信息,截图成功！"
driver.close()

driver = webdriver.Chrome()
driver.get('http://www.tianyancha.com/company/22822?nav=nav-main-patentCount')  # 专利信息
time.sleep(5)
driver.save_screenshot(screenPath + '33-专利信息.png')
print "33-专利信息,截图成功！"
driver.close()

driver = webdriver.Chrome()
driver.get('http://www.tianyancha.com/company/22822?nav=nav-main-cpoyRCount')  # 著作权
time.sleep(5)
driver.save_screenshot(screenPath + '34-著作权.png')
print "34-著作权,截图成功！"
driver.close()

driver = webdriver.Chrome()
driver.get('http://www.tianyancha.com/company/22822?nav=nav-main-icpCount')  # 网站备案
time.sleep(5)
driver.save_screenshot(screenPath + '35-网站备案.png')
print "35-网站备案,截图成功！"
driver.close()
