# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 18:28:39 2020

@author: a8275

https://pypi.org/project/pikax/
参数详见上述
"""
from pikax import Pikax, settings, params
from pikax.texts import texts
import datetime
import os

texts.lang = texts.ZH 

def DownloadRank(limit=50):
    pixiv = Pikax()
    results = pixiv.rank(limit)
    return results

def SearchRank(key,limit=50,popularity=0):
    pixiv = Pikax(settings.username, settings.password)
    results = pixiv.search(keyword=key, limit=50, popularity=1000, match=params.Match.PARTIAL)
    return results

def Down(result):
    pixiv = Pikax()
    pixiv.download(result)

x=input("Please select the mode:")
x=int(x)
if x==1:
    Down(DownloadRank(100))
elif x==2:
    x=input('Please input keyword:')
    Down(SearchRank(x))
elif x==0:
    while True:
        time = datetime.datetime.now()
        if time.hour==6 and time.minute==0 and time.second==0:
            Down(DownloadRank(200))
            system("pause")
    