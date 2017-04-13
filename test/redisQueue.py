# -*- coding:utf-8 -*-

import redis

red_queue = "huaban_user_url"
red_crawled_set = "huaban_crawled_url"

red = redis.Redis(host='localhost',port=6379,db=1)

def crawl_url(url):
    red.lpush(red_queue,url)

def check_url(url):
    if red.sadd(red_crawled_set,url):
        red.lpush(red_queue,url)