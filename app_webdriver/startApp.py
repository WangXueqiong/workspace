# coding=utf-8
from appium import webdriver
import time
desired_caps = {
    'platformName': 'Android',
    'deviceName': 'W8R0215A16001204',
    'platformVersion': '6.0',
    #apk包名
    'appPackage': 'com.tianyancha.skyeye',
    #apk的launcherActivity
    'appActivity': 'com.tianyancha.skyeye.activity.SplashActivity'
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

time.sleep(2000);
driver.findElement("com.tianyancha.skyeye:id/txt_search_copy1","id").click();
driver.input("//android.widget.EditText[@resource-id='com.tianyancha.skyeye:id/search_input_et' and @text='请输入公司名、人名等关键词']","input","百度");
driver.findElement("com.tianyancha.skyeye:id/rl_content","id").click();