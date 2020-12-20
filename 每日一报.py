import selenium as se
from selenium import webdriver
import time
import random

base_url="http://selfreport.shu.edu.cn/Default.aspx"
#导入库
options = webdriver.ChromeOptions()
options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36')#UA伪装
#options.add('--headless')#隐藏浏览器界面
driver = webdriver.Chrome(options = options)
driver.get(base_url)
#使用之前需要安装selenium库并安装chorme驱动
username='19122462'
password='Zvzsdf1800'#你需要填写的账号和密码

name_input = driver.find_element_by_name('username')

pass_input = driver.find_element_by_name('password')
name_input.clear()
name_input.send_keys(username)  # 填写账号

pass_input.clear()
pass_input.send_keys(password)
driver.find_element_by_id('login-submit').click()
#登录每日一报
base_url="https://selfreport.shu.edu.cn/XueSFX/FanXRB.aspx"
driver.get(base_url)
#跳转至手机端填报窗口
day_report=driver.find_element_by_id('p1_Button1')
day_report.click()
driver.find_element_by_id('p1_ChengNuo-inputEl-icon').click()
time.sleep(random.randint(1,3))
day_temp=driver.find_element_by_id('p1_TiWen-inputEl')
day_temp.clear()
day_temp.send_keys(str(round(random.uniform(36,37),1)))  # 温度
#day_temp.send_keys(str(36.2)) #测试标记
driver.find_element_by_id('fineui_7-inputEl-icon').click()#绿色

driver.find_element_by_id('p1_ctl00_btnSubmit').click() #提交
time.sleep(random.randint(1,3))
driver.find_element_by_id('fineui_14').click() #提交确认
time.sleep(random.randint(1,3))
#晨报
base_url="https://selfreport.shu.edu.cn/XueSFX/FanXRB.aspx"
driver.get(base_url)

day_report=driver.find_element_by_id('p1_Button2')
day_report.click()
driver.find_element_by_id('p1_ChengNuo-inputEl-icon').click()
time.sleep(random.randint(1,3))
day_temp=driver.find_element_by_id('p1_TiWen-inputEl')
day_temp.clear()
day_temp.send_keys(str(round(random.uniform(36,37),1)))  # 温度
driver.find_element_by_id('fineui_7-inputEl-icon').click()#绿色

driver.find_element_by_id('p1_ctl00_btnSubmit').click() #提交
time.sleep(random.randint(1,3))
driver.find_element_by_id('fineui_14').click() #提交确认
time.sleep(3)
driver.close()