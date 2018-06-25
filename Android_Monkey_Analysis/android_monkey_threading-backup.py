#!/usr/bin/python
# coding:utf-8
# Author: lishuang

"""
1.增加多线程 Android monkey脚本
功能：
a.支持生成连接现有设备的monkey script
b.对生成的monkey log进行分析，生成分析日志
c.调用chkbugreport.jar对连接设备的logcat进行分析，生成bugreport
"""

import threading
from time import ctime, sleep
import os
import sys
import stat
import glob
import time
from analysis.monkey_log_analysis import analysis_monkey_report
from bugreport.analysis_bugreport import analysis_bugreport
from untils.untils import installApkPath, startActivity, stopActivity


def monkey_run():
    # 设置应用包名和入口Activity名
    pakage_name = 'com.tianyancha.skyeye'
    start_activity = 'com.tianyancha.skyeye.MainActivity'

    # 获取年月日时分秒
    now = time.strftime("%Y%m%d%H%M%S")

    # MonkeyRunner下获取运行的文件所在的路径
    rootpath = os.path.split(os.path.realpath(sys.argv[0]))[0]

    # 指定位置
    script_path = rootpath + "/monkeyscript/"
    bugreport_path = rootpath + "/analysis_bugreport/"
    apk_path = rootpath + "/apk/"

    # 如果不存在就创建目录
    if not os.path.isdir(script_path):
        os.mkdir(script_path)
    if not os.path.isdir(bugreport_path):
        os.mkdir(bugreport_path)

    # 删除已有测试cmd脚本
    # path = "E:\\Android_Monkey_Analysis\\"
    for file in glob.glob(os.path.join(script_path, '*.sh')):
        os.remove(file)

    # os.system('adb shell cat /system/build.prop >\phoneInfo.text')
    # f = rootpath + "/phoneInfo.text"

    os.system("clear")  # os.system("cls")具有清屏功能
    rt = os.popen('adb devices').readlines()  # os.popen()执行系统命令并返回执行后的结果
    n = len(rt) - 2
    print "当前已连接待测手机数为：" + str(n)
    aw = raw_input("是否要开始你的monkey测试，请输入(yes or no): ")

    if aw == 'yes':
        print "monkey测试即将开始...."
        count = raw_input("请输入你要进行的monkey执行count次数: ")
        testmodel = raw_input("请输入你是要进行单次测试还是多次连续测试，请输入(1-代表单次测试，2-代表多次连续测试): \n")
        ds = range(n)
        for i in range(n):
            nPos = rt[i + 1].index("\t")
            ds[i] = rt[i + 1][:nPos]
            dev = ds[i]
            print "\n\n设备名称是：" + dev

            # 调用安装apk
            # installApkPath(dev, apk_path)
            # time.sleep(5)

            # 启动APP的主界面
            startActivity(dev, pakage_name, start_activity)

            promodel = os.popen(
                "adb -s " + ds[i] + ' shell cat /system/build.prop | grep "ro.product.model="').readlines()  # 获取手机型号
            # print "promodel：" + promodel
            # modelname = ('').join(promodel)  # 将list转为字符串
            modelname = promodel[0]  # 从list中取出第一个值
            model = modelname[17:].strip('\r\n')
            proname = os.popen(
                "adb -s " + ds[i] + ' shell cat /system/build.prop | grep "ro.product.brand="').readlines()  # 获取手机名称
            roname = proname[0]
            name = roname[17:].strip('\r\n')
            packagename = os.popen(
                "adb -s " + ds[i] + ' shell pm list packages | grep ' + pakage_name).readlines()
            package = packagename[0]
            pk = package[8:].strip('\r\n')

            if pk == 'com.tianyancha.skyeye':
                # if dev != ' ':
                # dev_script_path = script_path +
                if not os.path.isdir(bugreport_path):
                    os.mkdir(bugreport_path)

                filedir = os.path.exists(script_path)
                if filedir:
                    print "File Exist!\n"
                else:
                    os.mkdir(script_path)
                devicedir = os.path.exists(script_path + name + '-' + model + '-' + ds[i])
                if devicedir:
                    # print "devicedir: " + devicedir
                    print "File Exist!\n"
                else:
                    os.mkdir(
                        script_path + name + '-' + model + '-' + ds[
                            i])  # 按设备ID生成日志目录文件夹  # "E:\\Android_Monkey_Analysis\\"
                wl = open(script_path + name + '-' + model + '-' + ds[i] + '-logcat' + '.sh',
                          'w')
                # wl.write('adb -s ' + dev + ' logcat -v time ACRA:E ANRManager:E System.err:W *:S')
                wl.write('adb -s ' + ds[i] + ' logcat -v time *:W')
                wl.write(
                    '> ' + script_path + '"' + name + '-' + model + '-' + ds[
                        i] + '"' + '/logcat_' + now + '_$RANDOM.txt\n')
                wl.close()

                if testmodel == '1':
                    wd = open(script_path + name + '-' + model + '-' + ds[i] + '-device' + '.sh', 'w')
                    wd.write(
                        '\nadb -s ' + ds[
                            i] + ' shell monkey -p ' + pakage_name + ' -v -v --pct-syskeys 0 --monitor-native-crashes --throttle 50 -s $RANDOM -v -v -v ' + count)  # 选择设备执行monkey
                    wd.write(
                        ' time > ' + script_path + '"' + name + '-' + model + '-' + ds[
                            i] + '"' + '/monkey_log_' + now + '_$RANDOM.txt\n')
                    wd.write('echo 测试成功完成，请查看日志文件~\n')
                    wd.close()
                elif testmodel == '2':
                    wd = open(script_path + name + '-' + model + '-' + ds[i] + '-device' + '.sh', 'w')
                    wd.write(':loop')
                    wd.write('\nset /a num+=1')
                    wd.write('\nif "%num%"=="4" goto end')
                    wd.write(
                        '\nadb -s ' + ds[
                            i] + ' shell monkey -p ' + pakage_name + ' -v -v --pct-syskeys 0 --monitor-native-crashes --throttle 50 -s $RANDOM -v -v -v ' + count)  # 选择设备执行monkey
                    wd.write(
                        ' time > ' + script_path + '"' + name + '-' + model + '-' + ds[
                            i] + '"' + '/monkey_log_' + now + '_$RANDOM.txt\n')
                    wd.write('echo 测试成功完成，请查看日志文件~\n')
                    wd.write('\nadb -s ' + ds[i] + ' shell am force-stop ' + pk)
                    wd.write('\nping -n 15 127.1 >nul')
                    wd.write('\ngoto loop')
                    wd.write('\n:end')
                    wd.close()
            else:
                print "请确认待测手机" + name + '-' + model + "未安装APP"

            # 执行上述生成的cmd脚本scriptpath
            for script_file in os.listdir(script_path):
                if os.path.isfile(os.path.join(script_path, script_file)) == True:
                    if script_file.find(ds[i] + '-device.sh') > 0:
                    # if script_file.find('device.sh') > 0:
                        print "name,model dev " + name, model, ds[i]
                        print "打印生成的monkey_script文件路径: " + os.path.join(script_path, script_file)
                        # 修改文件权限 # mode:777 https://www.cnblogs.com/oubo/archive/2011/08/09/2394552.html
                        os.chmod(os.path.join(script_path, script_file), stat.S_IRWXU | stat.S_IRGRP | stat.S_IROTH)
                        replace_file = script_file.replace(' ', '\ ')  # shell命令中文件名如果有空格，进行转义
                        # os.path.join(path1[, path2[, ...]])  #把目录和文件名合成一个路径 https://www.cnblogs.com/dkblog/archive/2011/03/25/1995537.html
                        os.system(os.path.join(script_path, replace_file))
                        time.sleep(1)

                        # 调用关闭当前包的activity
                        stopActivity(dev, pakage_name)


            # 执行分析解析上述生成的monkey txt
            monkey_log_path = script_path + name + '-' + model + '-' + dev + "/"  # ds[i]
            print "monkey txt: " + monkey_log_path
            for monkey_file in os.listdir(monkey_log_path):
                # print "file txt: " + file
                if monkey_file.find('.txt') > 0:
                    print "分析和解析monkey日志: " + monkey_file + '\n'
                    analysis_monkey_report(monkey_log_path + monkey_file, script_path, name, model, dev)  # ds[i])
                    time.sleep(1)
                else:
                    print "未匹配到.txt日志"

            # 调用chkbugreport.jar进行log分析生成报告
            print "生成Bugreport: " + monkey_file + '\n'
            analysis_bugreport(bugreport_path, name, dev)

    elif aw == 'no':
        print('请重新确认所有待测手机是否已通过adb命令连接至pc!')
    else:
        print "测试结束，输入非法，请重新输入yes or no！"
    sleep(5)


threads = []
t1 = threading.Thread(target=monkey_run)
threads.append(t1)
# t2 = threading.Thread(target=move, args=(u'阿凡达',))
# threads.append(t2)
# t3 = threading.Thread(target=analysis_bugreport)
# threads.append(t3)

if __name__ == '__main__':
    print "开启多线程，进行monkey.........\n"
    for t in threads:
        t.setDaemon(True)
        t.start()
        t.join()
    print "all over %s" % ctime()
