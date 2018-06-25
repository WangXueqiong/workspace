#!/usr/bin/python
# coding:utf-8
# Author: lishuang

"""
Android-monkey日志进行分析
"""

import datetime
import re
import time

"""

获取手机名称、型号生成文件报告

"""

# 获取年月日时分秒
now = time.strftime("%Y%m%d%H%M%S")


def analysis_monkey_report(monkey_log_path, script_path, name, model, dev):
    print "读取monkey日志： " + monkey_log_path
    # 读取monkey日志文件
    with open(monkey_log_path, "r") as file1:
        content = file1.readlines()

    # 准备日志分析报告
    with open(script_path + name + '-' + model + '-' + dev + '/monkey_log_analysis_' + now + '.txt\n',
              "a") as file2:
        starttime = datetime.datetime.now()
        file2.write("now:" + str(starttime) + '\n')
        print u'开始时间', starttime

        # 分析日志文件中的问题
        str1 = '.*ANR.*'
        str2 = '.*CRASH.*'
        str3 = '.*Exception.*'
        str4 = '.*finished.*'
        Acount, Ccount, Ecount = 0, 0, 0

        # 遍历日志中的每一行，来查找无响应/崩溃/异常
        for i in content:
            if re.match(str1, i):
                print u'分析过程中出现程序无响应，具体内容为：\n', i
                file2.write(i)
                Acount += 1
            elif re.match(str2, i):
                print u'分析过程中出现程序崩溃，具体内容为：\n', i
                file2.write(i)
                Ccount += 1
            elif re.match(str3, i):
                print u'分析过程中出现程序异常，异体内容为：\n', i
                file2.write(i)
                Ecount += 1
        # 如果存在任何异常则不用判断日志是否正常完成
        if Acount or Ccount or Ecount == 0:
            for i in content:
                if re.match(str4, i):
                    print u'分析过程中正常'
                    file2.write(i)

        endtime = datetime.datetime.now()
        print u'结束时间：', endtime
        file2.write("now:" + str(endtime) + '\n')
        sumtime = (endtime - starttime).seconds
        # 提示报告内容
        print u'报告已完成，请查看分析：'
        print u'位置：', monkey_log_path + name + '-' + model + '-' + dev + '/monkey_analysis_report_' + now + '.txt\n'
        print u'用时：', sumtime, 's'
