# !/usr/bin/python
# --coding:utf-8--#
# -------------------------------------------------------------------------------
# Name:        tyc_test
# Author:      ZCC
# Created:     01/18/2018
# -------------------------------------------------------------------------------
import re
import requests

a = requests.get("https://www.tianyancha.com")
data = a.text
title = re.findall("title.*title>", data)
description = re.findall("<meta name=.description.*itemprop=.description.*！.>", data)
keywords = re.findall("<meta name=.keywords.*content=.*>", data)
print (title)
print (description)
print (keywords)
