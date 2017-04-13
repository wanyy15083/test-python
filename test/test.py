# -*- coding:utf-8 -*-


import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import gevent.monkey
gevent.monkey.patch_socket()
import time

import gevent
from gevent.pool import Pool
from multiprocessing.dummy import Pool
import requests
import urllib2

the_list=range(6)

def create_misson(url):
    n=h(url)
    n.print_out()

class h():
    def __init__(self,n):
        self.n=n
    def print_out(self):
        try:
            requests.get(self.n)
        except requests.exceptions.ConnectionError as e:
            print "died:%s\n" % self.n
            return

gevent_pool=Pool(20)
urls=[
    'http://zhihu.com',
    'http://facebook.com',
    'http://zhaduixueshe.com',
    'http://google.com',
    'http://hao123.com',
    'http://duoshuo.com',
    'http://v2ex.com'
]


url_list=[]
for i in range(1,500):
    url_list.append("http://tieba.baidu.com/p/2781190586?pn="+str(i))

pool=Pool(2)
start=time.time()
pool.map_async(create_misson,url_list)
pool.close()
pool.join()
print "muiltiprocessing used ",str(time.time()-start)

start=time.time()
jobs=[]
for url in url_list:
    jobs.append(gevent.spawn(create_misson,url))
gevent.joinall(jobs)
print "use gevent used ",time.time()-start

start=time.time()
gevent_pool.map(create_misson,url_list)

#pool.join()
print "use gevent_pool used ",str(time.time()-start)

start=time.time()
for url in url_list:
    create_misson(url)
print "use nothing ,it cost:",str(time.time()-start)