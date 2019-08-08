"""
usingPOSTRequest.py

* 使用HTTPS的POST请求方法向服务器提交数据实现用户登录
* 使用代理IP解决防止反爬
* 设置超时提高爬虫效率
* 解析URL的方法

POST请求有什么用？
	POST是HTTP协议的请求方法之一，用于向服务器提交数据，
	例如有些网站需要用户提交用户信息（用户名密码等）。

代理IP：
	urlopen就好像opener的通用版本，当我们需要特殊功能（例如代理IP）的时候，urlopen就满足
	不了我们的需求，我们就要自己定义并创建特殊的opener了

	request中有各种处理各种特殊功能的方法：
	Proxyhandler， unknownHandler, HTTPHandler,
	HTTPDefaultErrorHandler, HTTPRedirectHandler,
	FTPHandler, FileHandler, HTTPErrorProcessor, DataHandler
"""

# coding: utf-8
import urllib.request
import urllib.error
import urllib.parse
import socket

# headers information
headers = {'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
			'Accept-language' : 'zh-CN,zh;q=0.9',
			'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
			}

#POST请求的信息，填写你的用户名和密码
value = {'source' : 'index_nav',
		'form_email' : 'he.xingran@zcst.com.cn',
		'form_password' : 'ryanho84@zcst',
		'captcha-solution' : 'effect',
		'captcha-id' : 'dUzgI0lmI1cy8iLwp3hwmJxQ:en'
		}
"""
代理IP设置用
#代理IP信息为字典格式，key为'http', value为'代理IP：端口号'
proxy = {'http' : '115.193.101.21:61234'}
"""
timeout = 2

try:
	socket.setdefaulttimeout(timeout)
	data = urllib.parse.urlencode(value).encode('utf8')
	response = urllib.request.Request(
		'http://www.douban.com/login', data = data, headers = headers)
	"""
	代理IP设置用
	#使用Proxyhandle方法生成处理器对象
	proxy_handler = urllib.request.ProxyHandler(proxy)
	#创建代理IP的opener实例
	opener = urllib.request.build_opener(proxy_handler)
	"""
	html = urllib.request.urlopen(response)
	"""
	#将设置好的post信息和headers的response作为参数,用于设置代理IP
	html = opener.open(response)
	"""
	result = html.read().decode('utf8')
	print(result)

except urllib.error.URLError as e:
	if hasattr(e, 'reason'):
		print('the Error reason is :', str(e.reason))
except urllib.error.HTTPError as e:
	if hasattr(e, 'code'):
		print('the Error code is :', str(e.code))
except socket.timeout:
	print('socket timeout!')
else:
	print('Request pass!')


