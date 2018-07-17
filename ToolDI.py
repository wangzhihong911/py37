#!/usr/bin/dev python
# coding=utf-8
import urllib;
import BsDI;


def create_file(_inname, _inlocal):
    path = _inlocal + '%s' % _inname;
    return path;


def down_img(_urls,save_file,inner):
    #print(_urls)
    global n
    n = 1
    headers = {'User-Agent': BsDI.getIE()}
    link = _urls[0].attrs['src'];
    img_url = '';
    if link.find('!') > 0:
        img_url = link[0:link.find('!')]
    # 下载图片，取名字 webp，bmp,jpg,png,tiff,gif
    out_f = save_file + '\%s-%s.jpg' % (inner,n);
    if ".jpg" in out_f:
        out_f = save_file + '\%s-%s.jpg'% (inner,n);
    elif ".png" in out_f:
        out_f = save_file + '\%s-%s.png'% (inner,n);
    elif ".bmp" in out_f:
        out_f = save_file + '\%s-%s.bmp'% (inner,n);
    elif ".gif" in out_f:
        out_f = save_file + '\%s-%s.gif' % (inner,n);
    else:
        out_f = save_file + '\%s-%s.jpg'% (inner,n);
    request = urllib.request.Request(img_url, None, headers);
    response = urllib.request.urlopen(request)
    with open(out_f, "wb") as f:
        f.write(response.read())
    n += 1;
    # time.sleep(random.uniform(1, 3));




