# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 21:29:41 2020

@author: a8275
"""


import win32com.client
par=[]
ppt=win32com.client.Dispatch('PowerPoint.Application')
ppt.Visible=1
filename=r'C:\Users\a8275\Desktop\无关紧要的东西\english\Abraham+Lincoln+&+The+Civil+War(new).ppt'
ppt_open=ppt.Presentations.Open(filename)
slide_count=ppt_open.Slides.Count
print("ppt的页数：",slide_count)
for i in range(1,slide_count+1):
    shapes_count=ppt_open.Slides(i).Shapes.Count
    print(f"____________________ 第{i}页:shape数：{shapes_count}_______________")
    for j in range(1,shapes_count+1):
        if ppt_open.Slides(i).Shapes(j).HasTextFrame:
            text=ppt_open.Slides(i).Shapes(j).TextFrame.TextRange.Text
            par.append(text)
ppt.quit()