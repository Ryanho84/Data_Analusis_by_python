"""
Request:
	An extensible library for opening URLs using a variety of protocols

Function urlopen:
	def urlopen(url, data = None, timeout = socket._GLOBAL_DEFAULT_TIMEOUT,
				*, cafile = None, capath = None,
				cadefault = False, context = None):
		...
	url: network address we input
	data: the extra information we send to the server request, such as user information used for login.
			the param is POST or GET.
	...
class Request:
	def __init__(self, url, data = None, headers = {},
				origin_req_host = None, unverifiable = False,
				method = None):
		...
	header: the message information of HTTP Request, such as User_Agent param,it can disguise spider to browser

class URLError:
	def __init__(self, reason, filename = None):
		self.args = reason,
		self.reason = reason
		if filename is not None:
			self.filename = filename
		...
	URLError class is the subclass of OSError

class HTTPError:
	def __init__(self, url, code, msg, hdrs, fp):
		self.code = code
		self.msg = msg
		self.hdrs = hdrs
		self.fp = fp
		self.filename = url
		...
	HTTPError class is the subclass of URLError
"""
import urllib.request
import urllib.error
try:
	headers = {'User_Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
	response = urllib.request.Request('http://python.org/', headers = headers)
	html = urllib.request.urlopen(response)
	result = html.read().decode('utf-8')

except urllib.error.URLError as e:
	if hasattr(e, 'reason'):
		print('the Error Reason is :' + str(e.reason))
except urllib.error.HTTPError as e:
	if hasattr(e, 'code'):
		print('the Error code is :' + str(e.code))
else:
	print("Request Pass!")

