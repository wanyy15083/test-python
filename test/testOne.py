import urllib2, urllib

# request = urllib2.Request("http://www.baidu.com")
# response = urllib2.urlopen(request)
# print(response.read())

# values={"username":"1508355923@qq.com","password":"WANYY15083SYG"}
# user_agent = "'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
# headers = {"User-Agent":user_agent,"Referer":"http://blog.csdn.net/"}
# data = urllib.urlencode(values)
# url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
# request = urllib2.Request(url,data,headers)
# response = urllib2.urlopen(request)
# print response.read()

# values = {}
# values["username"]="1508355923@qq.com"
# values["password"]="WANYY15083SYG"
# data = urllib.urlencode(values)
# url = "http://passport.csdn.net/account/login"
# geturl = url + "?" +data
# request = urllib2.Request(url)
# response = urllib2.urlopen(request)
# print response.read()

# enable_proxy = True
# proxy_handler = urllib2.ProxyHandler({"http":"http://some.proxy.com:8080"})
# null_proxy_handler = urllib2.ProxyHandler({})
# if enable_proxy:
#     opener = urllib2.build_opener(proxy_handler)
# else:
#     opener = urllib2.build_opener(null_proxy_handler)
# urllib2.install_opener(opener)
#
# response = urllib2.urlopen('http://www.baidu.com/',timeout=10)
# response = urllib2.urlopen('http://www.baidu.com/',data,10)
# request = urllib2.Request(url,data=data)
# request.get_method() = lambda :'PUT' or 'DELETE'
# response = urllib2.urlopen(request)

# httpHandler = urllib2.HTTPHandler(debuglevel=1)
# httpsHandle = urllib2.HTTPSHandler(debuglevel=1)
# opener = urllib2.build_opener(httpHandler,httpsHandle)
# urllib2.install_opener(opener)
# response = urllib2.urlopen('http://www.baidu.com/')
# print response.read()

# request = urllib2.Request('http://www.xxxxx.com')
# try:
#     urllib2.urlopen(request)
# except urllib2.URLError,e:
#     print e.reason

# req = urllib2.Request('http://blog.csdn.net/cscdd')
# try:
#     urllib2.urlopen(req)
# except urllib2.HTTPError,e:
#     print e.code
# except urllib2.URLError,e:
#     print e.reason
# else:
#     print 'OK'

# req = urllib2.Request('http://blog.csdn.net/cscdd')
# try:
#     urllib2.urlopen(req)
# except urllib2.URLError,e:
#     if hasattr(e,'code'):
#         print e.code
#     if hasattr(e,'reason'):
#         print e.reason
# else:
#     print 'OK'

import cookielib

# cookie = cookielib.CookieJar()
# handler = urllib2.HTTPCookieProcessor(cookie)
# opener = urllib2.build_opener(handler)
# response = opener.open('https://www.baidu.com/')
# for item in cookie:
#     print 'Name = ' + item.name
#     print 'Value = ' + item.value

# filename = 'cookie.txt'
# cookie = cookielib.MozillaCookieJar(filename)
# handler = urllib2.HTTPCookieProcessor(cookie)
# opener = urllib2.build_opener(handler)
# response = opener.open('https://www.baidu.com/')
# cookie.save(ignore_discard=True,ignore_expires=True)

# cookie = cookielib.MozillaCookieJar()
# cookie.load('cookie.txt',ignore_expires=True,ignore_discard=True)
# req = urllib2.Request('https://www.baidu.com/')
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
# response = opener.open(req)
# print response.read()

filename = 'cookie.txt'
cookie = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postdata = urllib.urlencode({'email': '1508355923@qq.com', 'password': '8188SYG175','_ref':'frame'})
loginUrl = 'https://huaban.com/auth/'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
headers = {'User-Agent':user_agent,'Referer':'http://huaban.com/','Origin':'http://huaban.com'}
request = urllib2.Request(loginUrl,postdata,headers)
result = opener.open(request)
cookie.save(ignore_discard=True, ignore_expires=True)
gradeUrl = 'http://huaban.com/pins/814174415/'
result = opener.open(gradeUrl)
print result.read()

















