#!/usr/bin/dev python
# coding=utf-8
#让爬虫等待几秒
from pyDEV import BsDI, ToolDI
import os

#创建入口url
url_web = "https://www.sxtp.net/meinv/siwa/"
html = BsDI.getURL_CODE(url_web, 'utf-8')
soup = BsDI.get_htmlInfo(html)

html_body = soup.select('body')
html_inWrap = html_body[0].select('dl#nm')
html_ul=html_inWrap[0].select("p#l")
html_li = html_ul[0].select("a")

save_file ='E:\\images\\'
for tag in html_li:
    html_tit = tag.attrs['title'].strip().replace(' ', '')
    htm_em = tag.select("em")[0].text
    htm_count = htm_em.replace(str('张'),'') #得到张数
    print(htm_count)
    #break
    path= ToolDI.create_file(html_tit, save_file)
    if not os.path.exists(path):
        os.mkdir(path) #创建目录
    os.chdir(path) #进入该目录
    # #开始爬取页面
    html_href='https://www.sxtp.net'+tag.attrs['href'].strip().replace(' ', '')
    htm_orf =''
    for inner in range(1,int(htm_count)+1):
        if inner <2:
            htm_orf = html_href
        else:
            in_href = html_href.replace('.html','')
            in_href=in_href+'_'+str(inner)+'.html'
            htm_orf = in_href
        htm_pic = BsDI.getURL_CODE(htm_orf, 'utf-8')
        htm_soup = BsDI.get_htmlInfo(htm_pic)
        htm_body = htm_soup.select("dd.p")[0]
        htm_p = htm_body.select("p")[0]
        htm_img = htm_p.select("img")
        # 进入子目录,保存图片
        ToolDI.down_img(htm_img, path, inner)
    #python3默认使用utf-8  所以不在需要转码
    print('%s%s%s' % ('文件夹:', html_tit, '执行完毕'))
print('结束')