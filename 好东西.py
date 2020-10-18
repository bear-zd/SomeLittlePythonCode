# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 10:51:29 2020

@author: a8275
"""
import requests
import json
import urllib.request
import ssl

number=2000#你要获取的骚话的数量
words=[]#空列表，用于写入
ssl._create_default_https_context = ssl._create_unverified_context #我也不知道是干什么的
keys={'c':'b'} #Api端口的键值,详见内容  https://developer.hitokoto.cn/sentence/#%E8%AF%B7%E6%B1%82%E5%8F%82%E6%95%B0
url='https://v1.hitokoto.cn/' #Api端口
k=0#检测重复数量，但是随着量增大，效果可能会很弱
file=open('collected.txt','w',encoding='utf-8')
for i in range(0,number):
    r=requests.get(url,keys)
    print("Requesting "+str(i+1))
    print("the staue code:"+str(r.status_code))   
    if r.json()['hitokoto'] in words:
        print("the "+ r.json()['hitokoto']+"has already exist")
        k=k+1
        continue
    words.append(r.json()['hitokoto'])
    print("the " +r.json()['hitokoto']+"has been added")
for i in range(0,number-k):
        file.write(str(i+1)+": ")
        file.write(words[i]+'\n')

file.close()


