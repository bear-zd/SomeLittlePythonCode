# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 18:24:32 2020

@author: Bear_zd
"""

import requests
import json
import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context #我也不知道是干什么的
keys={'type':'rank','content':'all','mode':'daily','per_page':20} #Api端口的键值
url='https://api.imjad.cn/pixiv/v1/' #Api端口
r=requests.get(url,keys)
print("Status Code:",r.status_code)
response_dict=r.json()
for i in range(0,20):
    print(response_dict['response'][0]['works'][i]['work']['id'])
    pic_id=response_dict['response'][0]['works'][i]['work']['id']
    key_id={'type':'illust','id':pic_id}
    r_pic=requests.get(url,key_id)
    pic_url=r_pic.json()['response'][0]['image_urls']['large'] #保存图片的Url地址
    opener = urllib.request.build_opener()
    opener.addheaders=[('Referer', pic_url)]
    urllib.request.install_opener(opener)
    urllib.request.urlretrieve(pic_url,filename=r"C:\Users\Bear_zd\Desktop\picture\{}.png".format(i))
    print("The {} has downloaded!".format(i))
