# -*- coding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import gevent.monkey
gevent.monkey.patch_all()

import gevent
import redis
import getHuabanUsers
import time
from multiprocessing.dummy import Pool
import multiprocessing

red_queue = "huaban_user_url"
red_crawled_set = "huaban_crawled_url"

process_pool=Pool(multiprocessing.cpu_count()*2)

red = redis.Redis(host='localhost',port=6379,db=1)

def crawl_url(url):
    red.lpush(red_queue,url)

def check_url(url):
    if red.sadd(red_crawled_set,url):
        red.lpush(red_queue,url)

def create_new_slave(url):
    new_slave = getHuabanUsers.Huaban_Crawler(url)
    # print url
    new_slave.send_request()
    return "ok"

def gevent_worker():
    while True:
        url = red.lpop(red_queue)
        if not url:
            break
        create_new_slave(url)

def process_worker():
    jobs=[]
    for i in range(50):
        jobs.append(gevent.spawn(gevent_worker))
    gevent.joinall()

if __name__=="__main__":

    start = time.time()
    count=0

    red.lpush(red_queue,"http://huaban.com/w1dvcnopmu/")
    url=red.lpop(red_queue)
    create_new_slave(url)
    for i in range(50):
        url=red.lpop(red_queue)
        print url
        create_new_slave(url)

    process_pool.map_async(process_worker)
    process_pool.close()
    process_pool.join()

    print "crawler has crawled %d people ,it cost %s" %(count,time.time()-start)
