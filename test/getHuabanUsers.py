# -*- coding:utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding("utf-8")

import gevent.monkey

gevent.monkey.patch_socket()
gevent.monkey.patch_ssl()

import requests
from lxml import etree
import os
import saveHuaBan
from redisQueue import check_url, crawl_url
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class Huaban_Crawler():
    def __init__(self, url):
        self.url = url
        self.header = {}
        self.header[
            "User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
        self.header["Host"] = "huaban.com"
        self.header["Referer"] = "http://huaban.com/"
        self.header["Upgrade-Insecure-Requests"] = "1"

        self.cookies = {
            "CNZZDATA1256903590": "1642451369-1470759567-null%7C1472557767",
            "__auc": "b58549f3156703b2e4b0b5795d0",
            "_cnzz_CV1256903590": "is-logon%7Clogged-in%7C1472629183193%26urlname%7Ce2cy2srtu9%7C1472629183194",
            "_ga": "GA1.2.524949235.1470761741",
            "_hmt": "1",
            "sid": "gkbDMNF7fOz6ytSutdsIpToWmTj.M4zaJfhOD3mrSc%2F6CiSkFqiEFM0A3aYC8%2BTuH%2FhncyQ",
            "uid": "7014435",
            "_asc": "3214e853156df8a0f31bb609215"
        }

        self.proxies = {"https": "http://111.79.229.196:8998"}

    def send_request(self):
        added_user_url = self.url + 'following/'
        # r = requests.get(added_user_url, cookies=self.cookies, headers=self.header, verify=False, proxies=self.proxies)
        # content = r.text
        try:
            content = self.get_dom(added_user_url)
        except:
            crawl_url(self.url)
            return

            # if r.status_code == 200:
        self.parse_user_profile(content.decode('utf-8'))

    def process_xpath_source(self, source):
        if source:
            return source[0]
        else:
            return ''

    def parse_user_profile(self, html_source):
        self.user_url = ''
        self.user_name = ''
        self.user_followers = ''
        self.user_follows = ''
        self.picture_num = ''
        self.catch_num = ''
        self.like_num = ''

        tree = etree.HTML(html_source)

        # self.user_url = self.url.split('/')[3]
        self.user_name = self.process_xpath_source(tree.xpath("//div[@class='name']/text()"))
        self.user_followers = self.process_xpath_source(tree.xpath("//a[@class='followers']/div[@class='num']/text()"))
        self.user_follows = self.process_xpath_source(tree.xpath("//a[@class='follows']/div[@class='num']/text()"))
        self.picture_num = self.process_xpath_source(tree.xpath("//a[@class='tab '][1]/text()"))
        self.catch_num = self.process_xpath_source(tree.xpath("//a[@class='tab '][2]/text()"))
        self.like_num = self.process_xpath_source(tree.xpath("//a[@class='tab '][3]/text()"))

        self.print_data_out()

        url_list = tree.xpath("//a[@class='username']/@href")
        for target_url in url_list:
            check_url('http://huaban.com' + target_url)
            print target_url

    def print_data_out(self):
        print "*" * 60
        print u"URL:%s\n" % self.url
        print u"用户：%s\n" % self.user_name
        print u"粉丝：%s\n" % self.user_followers
        print u"关注：%s\n" % self.user_follows
        print u"画板：%s\n" % self.picture_num
        print u"采集：%s\n" % self.catch_num
        print u"喜欢：%s\n" % self.like_num
        print "*" * 60

        my_dict = {
            'user_name': self.user_name,
            'user_followers': self.user_followers,
            'user_follows': self.user_follows,
            'picture_num': self.picture_num,
            'catch_num': self.catch_num,
            'like_num': self.like_num,
            'user_url': self.url
        }
        save = saveHuaBan.HuabanMysql()
        save.save_data('user', my_dict)

    def get_dom(self, url):
        cmd = 'cmd.exe /k phantomjs.exe huaban.js "%s"' % url
        result = os.popen(cmd)
        dom = result.read()
        result.close()
        return dom

# huaban = Huaban_Crawler("http://huaban.com/w1dvcnopmu")
# huaban.send_request()
