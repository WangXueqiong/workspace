#-*-coding:utf8-*-
import urllib
import urllib2
url = "http://capi.test63.tianyancha.com/cloud-discuss/service/question/addQuestion"
headers = {'Authorization':'17610780265###1c3829906c4711e7a160a3563bb98742###1500446287430','X-AUTH-TOKEN':'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNzYxMDc4MDI2NSIsImlhdCI6MTU0MDg3MDIxOSwiZXhwIjoxNTU2NDIyMjE5fQ.b4o8ZYHawhp-NoWoJx2AvMQNAtSsHaxIqMXuIJDYRbOAMfsLcFVCb0dzCrUkenRtoZwYMnAhiulmasxc-p7n1g','version':'TYC-Web','Content-Type':'application/json'}
data = {}
data['companyGid'] = '22822';
data['content'] = '这家公司怎么样？';
#数据编码以及赋值
data = urllib.urlencode(data)
req = urllib2.Request(url, data, headers)
#打开地址并且赋值给变量
ResponseStr = urllib2.urlopen(req)
#读取获得的值
ResponseStr = ResponseStr.read()
#将获得的结果进行转码
ResponseStr = ResponseStr.decode("unicode_escape")
print ResponseStr