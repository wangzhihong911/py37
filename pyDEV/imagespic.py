#!/usr/bin/dev python
# coding=utf-8
#让爬虫等待几秒
from pyDEV import BsDI, ToolDI
from bs4 import BeautifulSoup;
import os
import urllib;

#创建入口url
url_web = "http://48et.com/pic/12/"
html_pag = '';
for i  in range(1,1001):
    if i > 1 :
        html_pag='p_'+str(i)+'.html'
    url_web = url_web+html_pag
    html = BsDI.getURL_CODE(url_web, 'GBK')
    soup = BsDI.get_htmlInfo(html)
    html_body = soup.select('body')
    html_inWrap = html_body[0].find_all('div')
    html_mydiv = html_inWrap[8]
    html_ul = html_mydiv.find_all('ul')
    html_li = html_ul[0].select('li')
    html_href = 'http://48et.com'
    save_file = 'E:\\av_images\\'
    for tag in html_li:
        html_a = tag.select('a')[0]
        # 得到所有url地址
        html_ohref = html_a.attrs['href'].strip().replace(' ', '')
        # 得到文件名字
        html_title = html_a.text
        # 创建文件夹 开始
        path = ToolDI.create_file(html_title, save_file)
        if not os.path.exists(path):
            os.mkdir(path)  # 创建目录
        os.chdir(path)  # 进入该目录
        # 创建文件夹结束
        # 进入子页面爬取图片 开始
        html_inpage = html_href + html_ohref
        htm_pic = BsDI.getURL_CODE(html_inpage, 'GBK')
        htm_soup = BsDI.get_htmlInfo(htm_pic)
        htm_body = htm_soup.select('div.post')
        htm_img = htm_body[0].select('img')
        # [<img alt="点击大图看下一张：女王甄甄美乳微露销魂胴体春光乍泄" src="https://tupian.sxtp.net/d/file/201801/2liukckjwkcd.jpg!800"/>]
        for htm_tag in htm_img:
            inner = htm_img.index(htm_tag)
            link = htm_tag.attrs['src']
            ToolDI.copy_img(link, path, inner)
        print('%s%s%s' % ('文件夹:', html_title, '执行完毕'))


