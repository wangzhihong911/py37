#!/usr/bin/dev python
# coding=utf-8
import random
import requests
from bs4 import BeautifulSoup
import urllib

#创建时间20180717
# 浏览器代理助手
def getIE():
    ua_list = [
        "Mozilla/5.0 (Windows NT 6.2 WOW64 rv:21.0) Gecko/20100101 Firefox/21.0",
        "Mozilla/5.0 (Windows NT 6.2 WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0 WOW64 Trident/7.0 rv:11.0) like Gecko"
    ]
    user_agent = random.choice(ua_list)
    return user_agent


proxy = {'HTTPS': '117.36.103.170:8118',
         'HTTPS': '121.61.89.89:61234',
         'HTTP': '123.134.87.136:61234',
         'HTTPS': '222.185.22.165:6666',
         'HTTPS': '49.83.164.139:61234',
         'HTTPS': '14.118.253.187:6666',
         'HTTPS': '14.118.254.21:6666',
         'HTTP': '119.28.194.66:8888',
         'HTTP': '122.114.31.177:808',
         'HTTP': '61.135.217.7:80',
         'HTTP': '117.63.78.54:6666',
         'HTTPS': '180.118.243.160:808',
         'HTTPS': '116.236.160.230:8888',
         'HTTPS': '121.46.95.27:8080',
         'HTTPS': '114.228.75.50:6666',
         'HTTPS': '60.176.235.132:6666',
         'HTTPS': '49.83.160.93:61234',
         'HTTPS': '121.237.120.35:8118',
         'HTTPS': '221.228.17.172:8181',
         'HTTP': '125.118.244.157:808',
         'HTTP': '110.73.1.134:8123',
         'HTTPS': '14.118.252.103:6666',
         'HTTPS': '222.185.22.223:6666',
         'HTTP': '60.214.118.170:63000',
         'HTTP': '119.28.142.148:8888',
         'HTTPS': '14.118.255.53:6666',
         'HTTPS': '14.118.254.224:6666',
         'HTTPS': '121.231.154.117:6666',
         'HTTP': '114.239.125.14:61234',
         'HTTP': '110.73.0.124:8123',
         'HTTPS': '14.118.252.112:6666',
         'HTTP': '115.46.68.135:8123',
         'HTTP': '106.111.45.69:61234',
         'HTTPS': '121.231.32.33:6666',
         'HTTPS': '114.226.135.164:6666',
         'HTTP': '111.155.124.84:8123',
         'HTTPS': '14.118.255.74:6666',
         'HTTP': '60.176.232.13:6666',
         'HTTP': '121.234.245.182:61234',
         'HTTP': '125.118.150.197:808',
         'HTTP': '223.145.230.114:6666',
         'HTTPS': '117.63.78.167:6666',
         'HTTPS': '115.219.105.178:8010',
         'HTTPS': '121.231.155.156:6666',
         'HTTP': '106.122.170.176:8118',
         'HTTPS': '14.118.252.182:6666',
         'HTTP': '110.73.42.195:8123',
         'HTTP': '121.31.198.60:8123',
         'HTTPS': '58.19.80.227:808',
         'HTTPS': '114.226.65.62:6666',
         'HTTPS': '125.118.146.115:6666',
         'HTTPS': '58.214.50.58:8070',
         'HTTP': '183.128.243.71:6666',
         'HTTP': '110.73.1.46:8123',
         'HTTPS': '114.225.170.140:53128',
         'HTTPS': '123.55.190.36:808',
         'HTTP': '49.85.0.49:39352'}


# 默认UTF-8
def getURL(web_url):
    # 随机请求头,防止反爬虫
    ua_headers = {"User-Agent": getIE()}
    response = requests.get(web_url, headers=ua_headers, proxies=proxy)
    response.encoding = 'utf-8'
    return response.text


# 目标页面的编码格式
def getURL_CODE(web_url, incode):
    # 随机请求头,防止反爬虫
    ua_headers = {"User-Agent": getIE()}
    response = requests.get(web_url, headers=ua_headers, proxies=proxy)
    response.encoding = incode
    #print('获得请求头完毕')
    return response.text


# 获取网页内容
def get_htmlInfo(html):
    # 载入html,是哦那个lxml解析
    # soup = BeautifulSoup(html, 'lxml')  # lxml 这个狗参数有坑  内容丢失
    soup = BeautifulSoup(html, 'html.parser')
    return soup


# 得到页面访问状态
def get_status(url_web, ua_headers):
    request = urllib.request.Request(url_web, headers=ua_headers)
    response = urllib.request.urlopen(request)
    return response.getcode()
