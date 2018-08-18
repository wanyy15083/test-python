# -*- coding:utf-8 -*-

__author__ = 'SYG'

import urllib.request, urllib.parse, urllib.error
import urllib.request, urllib.error, urllib.parse
import re
import _thread
import time

# page = 1
# url = 'http://www.qiushibaike.com/hot/page/' + str(page)
# user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
# headers = {'User-Agent':user_agent}
# try:
#     request = urllib2.Request(url,headers=headers)
#     response = urllib2.urlopen(request)
#     # print response.read()
#     content = response.read().decode('utf-8')
#     pattern = re.compile('<div.*?clearfix">.*?<h2>(.*?)</h2>.*?<div.*?'+
#                          'content">(.*?)</div>(.*?)<div.*?stats">.*?number">(.*?)</i>',re.S)
#     items = re.findall(pattern,content)
#     for item in items:
#         haveImg = re.search('img',item[2])
#         if not haveImg:
#             print item[0],item[1],item[3]
# except urllib2.URLError,e:
#     if hasattr(e,'code'):
#         print e.code
#     if hasattr(e,'reason'):
#         print e.reason

#基类
class QSBK:

    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent' : self.user_agent}
        self.stories = []
        self.enable = False

    def getPage(self,pageIndex):
        try:
            url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
            request = urllib.request.Request(url,headers=self.headers)
            response = urllib.request.urlopen(request)
            pageCode = response.read().decode('utf-8')
            return pageCode
        except urllib.error.URLError as e:
            if hasattr(e,'reason'):
                print("连接糗事百科失败，失败原因",e.reason)
                return None

    def getPageItems(self,pageIndex):
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print("页面加载失败...")
            return None
        pattern = re.compile('<div.*?clearfix">.*?<h2>(.*?)</h2>.*?<div.*?content">(.*?)</div>(.*?)<div.*?stats">.*?number">(.*?)</i>',re.S)
        items = re.findall(pattern,pageCode)
        pageStories = []
        for item in items:
            haveImg = re.search('img',item[2])
            if not haveImg:
                replaceBR = re.compile('<br/>')
                text = re.sub(replaceBR,'\n',item[1])
                pageStories.append([item[0].strip(),text.strip(),item[3].strip()])
        return pageStories

    def loadPage(self):
        if self.enable == True:
            pageStories = self.getPageItems(self.pageIndex)
            if pageStories:
                self.stories.append(pageStories)
                self.pageIndex +=1

    def getOneStory(self,pageStories,page):
        for story in pageStories:
            input = input()
            self.loadPage()
            if input == 'Q':
                self.enable = False
                return
            print('第%d页\t发布人：%s\t赞：%s\n%s' %(page,story[0],story[2],story[1]))

    def start(self):
        print('正在读取糗事百科，按回车查看新段子，Q退出')
        self.enable = True
        self.loadPage()
        nowPage = 0
        while self.enable:
            if len(self.stories)>0:
                pageStories = self.stories[0]
                nowPage +=1
                del self.stories[0]
                self.getOneStory(pageStories,nowPage)

spider = QSBK()
spider.start()

































