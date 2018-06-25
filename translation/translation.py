#!/usr/bin/python
# -*- coding:utf8 -*-
from tkinter import *
from tkinter import messagebox
import requests


# 根据用户输入的单词翻译
def translation():
    #获取用户输入的单词
    content = entry.get()
    print(content)
    if content == '':
        messagebox.showinfo('提示','请输入要翻译的单词')
    else:

        url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}
        data = {}
        data['i'] = content
        data['from'] = 'zh-CHS'
        data['to'] = 'en'
        data['smartresult'] = 'dict'
        data['client'] = 'fanyideskweb'
        #时间戳
        #data['salt'] = '1529573776807'
        #签名 加密
        # data['sign'] = 'cbda6af2df5c7cbd1e99b78e21694d46'
        data['doctype'] = 'json'
        data['version'] = '2.1'
        data['keyfrom'] = 'fanyi.web'
        data['action'] = 'FY_BY_REALTIME'
        data['action'] = 'FY_BY_REALTIME'
        data['typoResult'] = 'false'

        result = requests.post(url,data=data,headers = header)
        print(result)
        translation = result.json()
        translation = translation['translateResult'][0][0]['tgt']
        print(translation)
        res.set(translation)

# 创建窗口
root = Tk()
# 窗口标题
root.title('中英互译')
# 窗口大小
root.geometry('400x100+500+300')
#　窗口位置
#　root.geometry('+550+350')
#标签控件
lable = Label(root,text = '输入要翻译的文字:',font = ('微软雅黑'))
lable.grid()
label1 = Label(root,text = '翻译之后的结果:', font = ('微软雅黑'))
# 网格式布局 pack place
label1.grid()

res = StringVar()
#输入控件
entry = Entry(root,font  = ('微软雅黑',15))
entry.grid(row = 0,column = 1)
entry1 = Entry(root,font = ('微软雅黑',15),text = res)
entry1.grid(row = 1,column = 1)

#按钮控件
button = Button(root,text = '翻译',width = 10,font = ('微软雅黑',10),command = translation)
button.grid(row = 2,column = 0,sticky = W)
button1 = Button(root,text = '退出',width = 10,font = ('微软雅黑',10),command = root.quit)
button1.grid(row = 2,column = 1,sticky = E)
#消息循环  显示窗口
root.mainloop()