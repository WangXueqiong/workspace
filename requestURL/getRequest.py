#-*-coding:utf8-*-
import urllib
import urllib2
url = "http://10.2.2.127:8888/services/v3/risk/riskInfoV5/"
#定义请求数据，并且对数据进行赋值
data = {}
data['id'] = '1553410550'
#对请求数据进行编码
data = urllib.urlencode(data)
#将数据和url进行连接
request = url+'?'+data
#打开请求，获取对象
requestResponse = urllib2.urlopen(request)
#读取服务端返回的数据
ResponseStr = requestResponse.read()
#打印数据
ResponseStr = ResponseStr.decode("unicode_escape")
print(ResponseStr)