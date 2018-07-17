#!/usr/bin/dev python
# coding=utf-8
# 浏览器代理助手
import random
import requests
from bs4 import BeautifulSoup;


def getIE():
    ua_list = [
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"
    ];
    user_agent = random.choice(ua_list);
    return user_agent;


# 默认UTF-8
def getURL(web_url):
    # 随机请求头,防止反爬虫
    ua_headers = {"User-Agent": getIE()};
    response = requests.get(web_url, headers=ua_headers);
    response.encoding = 'utf-8'
    return response.text;


# 获取网页内容
def get_htmlInfo(html):
    # 载入html,不推荐使用lxml解析
    soup = BeautifulSoup(html, 'html.parser');
    return soup;


url_web = "http://www.xicidaili.com/nn/";

html = getURL(url_web);
soup = get_htmlInfo(html);
html_ips = soup.select('table#ip_list')
html_trs = html_ips[0].select('tr')

#太短的不要
for i, tag in enumerate(html_trs):
    if i != 0:
        html_tds = tag.select('td')
        out_time = html_tds[8].text
        get_day = out_time.find('天')
        if get_day > 0:
            out_ip = "'" + html_tds[5].text + "':'" + html_tds[1].text + ':' + html_tds[2].text + "',"
            print(out_ip)

