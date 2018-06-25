#! /usr/bin/python
# coding=utf-8

"""
1.进入公司详情
2.进入股东信息
3.查看股东信息所有公司
4.匹配人详情并打开新的tab
5.查验他的所有公司是否一致
"""

import time
from selenium import webdriver
from tools.color_out import UseStyle

driver = webdriver.Chrome()
# driver.maximize_window()
driver.set_window_size(1920, 1080)
# driver.implicitly_wait(6)

login_url = 'http://sss.tianyancha.com/login'
user_phone = '13811567526'
user_pwd = 'ls123456'
# user_edit_element = ".//input[@class='_input input_nor contactphone']"
user_edit_element = ".//*[@id='web-content']/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/input"
# pwd_edit_element = "//div/input[@class='_input input_nor contactword']"
pwd_edit_element = ".//*[@id='web-content']/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div[3]/input"
# login_button_element = ".//div[@class='c-white b-c9 pt8 f18 text-center login_btn']"
login_button_element = ".//*[@id='web-content']/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div[5]"

driver.get(login_url)
time.sleep(2)
driver.find_element_by_xpath(user_edit_element).clear()
# driver.find_element_by_xpath(user_edit_element).click()
driver.find_element_by_xpath(user_edit_element).send_keys(user_phone)
# driver.find_element_by_xpath(pwd_edit_element).clear()
driver.find_element_by_xpath(pwd_edit_element).send_keys(user_pwd)
driver.find_element_by_xpath(login_button_element).click()
time.sleep(2)

group_id_file = open("/Users/lishuang/Work/PythonProject/Selenium_Python/shareholder_number_check/data_test/graph.txt")

while 1:
    lines = group_id_file.readlines(100000)
    if not lines:
        break
    for line in lines:
        # print line
        print UseStyle('sss.tianyancha.com/company/%s?nav=nav-main-holderCount' % line, fore='cyan')
        # print 'sss.tianyancha.com/company/%s?nav=nav-main-holderCount' % line
        # url = raw_input("请输入测试地址:")
        url = 'sss.tianyancha.com/company/%s?nav=nav-main-holderCount' % line
        driver.get("http://" + url.rstrip())
        time.sleep(2)

        # 获取table
        shareholderTable = driver.find_element_by_xpath(".//*[@id='_container_holder']/div/table")
        # table的总行数，包含标题
        shareholder_table_rows = shareholderTable.find_elements_by_tag_name('tr')
        # 去掉首行
        print "股东信息表格-行数:", len(shareholder_table_rows) - 1
        time.sleep(2)
        for x in range(len(shareholder_table_rows)):
            if x >= 1:
                shareholder_number_element = ".//*[@id='_container_holder']/div/table/tbody/tr[" + str(
                    x) + "]/td[1]/div/a"
                shareholder_value_element = ".//*[@id='_container_holder']/div/table/tbody/tr[" + str(x) + "]/td[1]/a"
                shareholderNumber = driver.find_element_by_xpath(shareholder_number_element).text
                shareholderValue = driver.find_element_by_xpath(shareholder_value_element).text
                # print '\n股东:%s,%s' % (shareholderValue.encode("utf-8"), shareholderNumber.encode("utf-8"))
                print UseStyle('\n股东:%s,%s' % (shareholderValue.encode("utf-8"), shareholderNumber.encode("utf-8")), fore='red')
                handle_1 = driver.current_window_handle
                time.sleep(3)
                driver.find_element_by_xpath(shareholder_number_element).click()
                handles = driver.window_handles
                for handle in handles:
                    # if handle != handles[0]:
                    if handle != handle_1:
                        time.sleep(1)
                        print 'switch to ', handle
                        driver.switch_to.window(handle)
                        # title方法可以获取当前页面的标题显示的字段
                        print 'title:%s ' % driver.title
                        time.sleep(5)
                        if driver.title.encode("utf-8").__contains__(shareholderValue.encode("utf-8")):
                            if '有限合伙' in shareholderValue.encode("utf-8"):
                                print '不是老板，是有限合伙'
                            elif '公司' in shareholderValue.encode("utf-8"):
                                print '不是老板，是公司'
                            elif '股' in shareholderValue.encode("utf-8"):
                                print '不是老板，是股'
                            else:
                                driver.find_element_by_xpath(
                                    ".//*[@id='web-content']/div/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div/span[2]").click()
                                time.sleep(1)
                                # 获取table
                                human_table = driver.find_element_by_xpath(
                                    "//div[@class='p20 human-table collapse humanTab humanTab2 in']/table")
                                # table的总行数，包含标题
                                human_table_rows = human_table.find_elements_by_tag_name('tr')
                                # print "他的所有公司表格-行数:", len(human_table_rows) - 1
                                print UseStyle("他的所有公司表格-行数:%s" % str(len(human_table_rows) - 1), fore='blue')
                                # 输出具体公司信息
                                # for y in range(len(human_table_rows)):
                                #     if y >= 1:
                                #         print str(y)
                                #         company_value_element = ".//tr[" + str(y) + "]/td[1]/a[@class='c9 hover_underline point']"
                                #         company_value = driver.find_element_by_xpath(company_value_element).text
                                #         print '公司:%s' % company_value.encode("utf-8")
                        driver.close()
                # driver.switch_to.window(handles[0])
                driver.switch_to.window(handle_1)
                time.sleep(1)

driver.quit()
