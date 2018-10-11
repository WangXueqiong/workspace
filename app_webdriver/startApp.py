# coding=utf-8
from appium import webdriver
desired_caps = {
    'platformName': 'Android',
    'deviceName': 'W8R0215A16001204',
    'platformVersion': '6.0',
    #apk包名
    'appPackage': 'com.tianyancha.skyeye',
    #apk的launcherActivity
    'appActivity': 'com.tianyancha.skyeye.activity.SplashActivity'
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)