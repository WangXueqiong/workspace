#!/usr/bin/python
# coding:utf-8
# Author: lishuang

import os

# execute times
execcount = 2
# execute interval, (seconds)
execinterval = 1 * 5

monkeyclickcount = 1000

WORKSPACE = os.path.abspath(".")


def getWorkConfig():
    f = open("./.config", "r")
    config = {"monkeyclickcount": monkeyclickcount, "execcount": execcount}
    try:
        while True:
            line = f.readline()
            if line:
                line = line.strip()
                linesplit = line.split("：")
                if linesplit.__sizeof__() > 1:
                    if linesplit[0] == 'phone':
                        config['phone'] = linesplit[1]
                    elif linesplit[0] == 'monkeyclickcount':
                        config["monkeyclickcount"] = linesplit[1]
                    elif linesplit[0] == 'execcount':
                        config["execcount"] = linesplit[1]
            else:
                break
    finally:
        f.close()
        print "config : %s" % config
        return config


def installApkConfig(config):
    phoneAddr = config.get("phone")
    print 'Ready to start installing apk'

    if phoneAddr:
        installPhoneApk = "adb -s %s install -r %s\\apk\\app-inland-debug.apk" % (phoneAddr, WORKSPACE)
        os.popen(installPhoneApk)
        print "install phone apk done"


def installApkPath(dev, apk_path):
    print 'Ready to start installing apk'
    for apk_file in os.listdir(apk_path):
        if apk_file.find('.apk') > 0:
            print 'apk_path：%s' % apk_path + apk_file
            install_phone_apk = "adb -s %s install -r -d %s" % (dev, apk_path + apk_file)
            print "install APK Path：" + install_phone_apk
            os.popen(install_phone_apk)
            print "install phone apk done"


def startActivity(dev, pakage_name, start_activity):
    if dev:
        # adb shell am start -n ｛包(package)名｝/｛包名｝.{活动(activity)名称}
        print "start Activity......"
        start_activity_sh = "adb -s %s shell am start -n %s/%s" % (dev, pakage_name, start_activity)
        print "start_activity_sh：" + start_activity_sh
        os.popen(start_activity_sh)


def stopActivity(dev, pakage_name):
    if dev:
        # adb shell am force-stop ｛包(package)名｝
        print "stop Activity......"
        stop_activity_sh = "adb -s %s shell am force-stop %s" % (dev, pakage_name)
        print "stop_activity_sh：" + stop_activity_sh
        os.popen(stop_activity_sh)


def apkPath(apk_path):
    print "apk_path: " + apk_path
    for apk_file in os.listdir(apk_path):
        # print "file txt: " + file
        if apk_file.find('.apk') > 0:
            print "获取apk文件路径: " + apk_file + '\n'
            return apk_file


def killTestApp():
    forceStopApp = "adb -s %s shell am force-stop com.example.demo1" % workConfig.get('phone')
    os.popen(forceStopApp)


def fullmonkey(workconfig):
    killTestApp()

    monkeycmd = "adb -s %s shell monkey -p com.example.demo1 " \
                "--ignore-timeouts --ignore-crashes --kill-process-after-error " \
                "--pct-touch 35 --pct-syskeys 30 --pct-appswitch 35 --hprof  " \
                "--throttle 100 -v -v -v %s" \
                % (workconfig.get("phone"), workConfig.get("monkeyclickcount"))
    os.popen(monkeycmd)


def createBugReport():
    print "create bugreport file"
    # bugreport = "adb -s %s shell bugreport > %sbugreport.txt" % (workConfig.get("phone"), WORKSPACE)
    bugreport = "adb -s %s shell bugreport > bugreport.txt" % (workConfig.get("phone"))
    os.popen(bugreport)

    print "create bugreport file ,done"

    # chkbugreport = "java -jar %s\\chkbugreport.jar %s\\bugreport.txt" % (WORKSPACE, WORKSPACE)
    chkbugreport = "java -jar chkbugreport.jar bugreport.txt"
    os.popen(chkbugreport)


def returnProductInfo():
    dev = returnDevInfo()
    # 获取手机型号
    promodel = os.popen(
        "adb -s " + dev + ' shell cat /system/build.prop | grep "ro.product.model="').readlines()
    modelname = promodel[0]  # 从list中取出第一个值
    model = modelname[17:].strip('\r\n')
    return model


def returnDevInfo():
    rt = os.popen('adb devices').readlines()  # os.popen()执行系统命令并返回执行后的结果
    n = returnNum()
    ds = range(n)
    for i in range(n):
        nPos = rt[i + 1].index("\t")
        ds[i] = rt[i + 1][:nPos]
        print "\n\n设备名称是：" + ds[i]
        return ds[i]


def returnNum():
    rt = os.popen('adb devices').readlines()  # os.popen()执行系统命令并返回执行后的结果
    n = len(rt) - 2
    return n


if __name__ == '__main__':
    returnProductInfo()
# workConfig = getWorkConfig()
# installApk(workConfig)
# forcount = int(workConfig.get("execcount"))

# for i in range(forcount):
#     print "execute monkey ,loop = %s" % (i + 1)
#     fullmonkey(workConfig)
#     time.sleep(execinterval)
#
# createBugreport()

# print "Completion of the current round of testing"
# raw_input("Enter key to close")
