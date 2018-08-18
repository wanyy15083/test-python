# -*- coding:utf-8 -*-

__author__ = 'SYG'

import urllib.request, urllib.parse, urllib.error
import urllib.request, urllib.error, urllib.parse
import socket
import types
import time
import re
import os
import subprocess


class Login:
    def __init__(self):
        self.username = 'songyigui'
        self.password = 'Abcd123'
        self.ip_pre = '10.81'
        self.overtime = 750
        self.every = 10

    def login(self):
        print((self.getCurrentTime(), '正在尝试连接无线网络'))
        ip = self.getIP()
        data = {
            "username": self.username,
            "password": self.password,
            "serverType": "",
            "isSavePass": "on",
            "Submit1": "",
            "Language": "Chinese",
            "ClientIP": self.getIP(),
            "timeoutvalue": 45,
            "heartbeat": 240,
            "fastwebornot": False,
            "StartTime": self.getNowTime(),
            # 持续时间，超过这个时间自动掉线，可进行设置
            "shkOvertime": self.overtime,
            "strOSName": "",
            "iAdptIndex": "",
            "strAdptName": "",
            "strAdptStdName": "",
            "strFileEncoding": "",
            "PhysAddr": "",
            "bDHCPEnabled": "",
            "strIPAddrArray": "",
            "strMaskArray": "",
            "strMask": "",
            "iDHCPDelayTime": "",
            "iDHCPTryTimes": "",
            "strOldPrivateIP": self.getIP(),
            "strOldPublicIP": self.getIP(),
            "strPrivateIP": self.getIP(),
            "PublicIP": self.getIP(),
            "iIPCONFIG": 0,
            "sHttpPrefix": "http://192.168.8.10",
            "title": "CAMS Portal"
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36',
            'Host': '192.168.8.10',
            'Origin': 'http://192.168.8.10',
            'Referer': 'http://192.168.8.10/portal/index_default.jsp?Language=Chinese'
        }
        post_data = urllib.parse.urlencode(data)
        login_url = 'http://192.168.8.10/portal/login.jsp?Flag=0'
        request = urllib.request.Request(login_url, post_data, headers)
        response = urllib.request.urlopen(request)
        result = response.read.decode('gbk')
        self.getLoginResult(result)

    def getLoginResult(self, result):
        if '用户上线成功' in result:
            print((self.getCurrentTime(), "用户上线成功,在线时长为", self.overtime / 60, "分钟"))
        elif '您已经建立了连接' in result:
            print((self.getCurrentTime(), "您已经建立了连接,无需重复登陆"))
        elif "用户不存在" in result:
            print((self.getCurrentTime(), "用户不存在，请检查学号是否正确"))
        elif "用户密码错误" in result:
            pattern = re.compile('<td class="tWhite">.*?2553:(.*?)</b>.*?</td>', re.S)
            res = re.search(pattern, result)
            if res:
                print((self.getCurrentTime(), res.group(1), '请重新修改密码'))
        else:
            print((self.getCurrentTime(), '未知错误，请检查学号密码是否正确'))

    def getNowTime(self):
        return str(int(time.time())) + '000'

    def getIP(self):
        local_IP = socket.gethostbyname(socket.gethostname())
        if self.ip_pre in str(local_IP):
            return str(local_IP)
        ip_lists = socket.gethostbyname_ex(socket.gethostname())
        for ip_list in ip_lists:
            if isinstance(ip_list, list):
                for i in ip_list:
                    if self.ip_pre in str():
                        return str(i)
            elif type(ip_list) is bytes:
                if self.ip_pre in ip_list:
                    return ip_list

    def canConnect(self):
        fnull = open(os.devnull, 'w')
        result = subprocess.call('ping www.baidu.com', shell=True, stdout=fnull, stderr=fnull)
        fnull.close()
        if result:
            return False
        else:
            return True

    def getCurrentTime(self):
        return time.strftime('[%Y-%m-%d %H:%M:%S]', time.localtime(time.time()))

    def main(self):
        print((self.getCurrentTime(), "您好，欢迎使用模拟登陆系统"))
        while True:
            nowIP = self.getIP()
            if not nowIP:
                print((self.getCurrentTime(), "请检查是否正常连接QLSC_STU无线网络"))
            else:
                print((self.getCurrentTime(), "成功连接了QLSC_STU网络,本机IP为", nowIP))
                self.login()
                while True:
                    can_connect = self.canConnect()
                    if not can_connect:
                        nowIP = self.getIP()
                        if not nowIP:
                            print((self.getCurrentTime(), "当前已经掉线，请确保连接上了QLSC_STU网络"))
                        else:
                            print((self.getCurrentTime(), "当前已经掉线，正在尝试重新连接"))
                            self.login()
                    else:
                        print((self.getCurrentTime(), "当前网络连接正常"))
                    time.sleep(self.every)
                time.sleep(self.every)


login = Login()
login.main()
