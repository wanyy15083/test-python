# -*- coding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import redis
import getHuabanUsers
import time
from multiprocessing.dummy import Pool
from redisQueue import red,red_queue

def create_new_slave(url,option):
    new_slave = getHuabanUsers.Huaban_Crawler(url)
    new_slave.send_request()
    return "ok"

def thread_worker():
    while True:
        url = red.lpop(red_queue)
        if not url:
            break
        create_new_slave(url)

if __name__=="__main__":

    start = time.time()
    count=0
    i=0

    red.lpush(red_queue,"http://huaban.com/w1dvcnopmu/following/")
    url=red.lpop(red_queue)
    create_new_slave(url)
    for i in range(20):
        url=red.lpop(red_queue)
        create_new_slave(url)

    threading_pool=Pool(120)
    threading_pool.map_async(thread_worker)
    threading_pool.close()
    threading_pool.join()

    print "crawler has crawled %d people ,it cost %s" %(count,time.time()-start)
