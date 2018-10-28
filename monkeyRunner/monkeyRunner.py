#!/user/bin/python
# coding=utf-8
#-*-UTF-8-*-
from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice
# MonkeyRunner.alert('Hello mook friends','This is title',"OK")
#连接设备
device = MonkeyRunner.waitForConnection(3,"W8R0215A16001204")
#启动APP
device.startActivity("com.tianyancha.skyeye/.activity.SplashActivity")
MonkeyRunner.sleep(9)
#点击首页搜索框
device.touch(400,480,"DOWN_AND_UP")
MonkeyRunner.sleep(1)
#点击搜索中间页搜索框
device.touch(420,140,"DOWN_AND_UP")
MonkeyRunner.sleep(1)
#输入查询词
device.type('test')
MonkeyRunner.sleep
#点击回车键
device.press('KEYCODE_ENTER','DOWN_AND_UP')
MonkeyRunner.sleep(1)
#点击排序按钮
device.touch(1000,140,"DOWN_AND_UP")
MonkeyRunner.sleep(6)
#截图
image = device.takeSnapshot()
image.writeToFile('C:/Users/Edianzu/Desktop/test.png','png')
