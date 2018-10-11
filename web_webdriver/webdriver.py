# coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
time.sleep(2)
driver.find_element_by_id("kw").send_keys("Selenium2")
time.sleep(2)
driver.find_element_by_id("su").click()
time.sleep(2)
driver.quit()