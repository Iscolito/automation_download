# -*- coding = utf-8 -*-
# @Time : 2022/3/24 14:51
# @Author : Iscolito
# @File : readtxt.py
# @Software : PyCharm

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import json
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


path = 'C:/Users/Iscolito/Desktop/1145141919810'
path_list = os.listdir(path)
path_list.sort(key=lambda x:int(x[2:5]))
print(path_list)
magnet = []
passwords = []
for filename in path_list:
    f = open(os.path.join(path,filename),'rb')
    allfile = f.readlines()
    getfile1 = allfile[0]
    getfile2 = allfile[2]
    link = getfile1[9:-3]
    link = link.decode("utf-8")
    password = getfile2[3:-3]
    password = password.decode("utf-8")
    magnet.append(link)
    passwords.append(password)
print(magnet)
print(passwords)

driver = webdriver.Edge()

driver.get("https://pan.baidu.com/")
print("登录你的百度云")
WebDriverWait(driver,timeout=120).until(EC.url_contains('https://pan.baidu.com/disk/main?from=homeFlow#/index?category=all'))
with open('cookies.txt', 'w') as f:
    f.write(json.dumps(driver.get_cookies()))

driver.get("https://pan.baidu.com/")
with open('cookies.txt', 'r') as f:
    cookies_list = json.load(f)
    for cookie in cookies_list:
        driver.add_cookie(cookie)

for item in magnet:
    driver.get(item)
    WebDriverWait(driver,timeout=60).until(EC.text_to_be_present_in_element((By.XPATH,"//*[@id='layoutMain']/div[1]/div[1]/div/div[3]/div/div/div[2]/a[1]"),u"保存到网盘"))
    driver.find_element(By.XPATH, "//*[@id='layoutMain']/div[1]/div[1]/div/div[3]/div/div/div[2]/a[1]").click()
    WebDriverWait(driver,timeout=60).until(EC.text_to_be_present_in_element((By.XPATH,"//*[@id='fileTreeDialog']/div[4]/a[2]"),u"确定"))
    driver.find_element(By.XPATH, "//*[@id='fileTreeDialog']/div[4]/a[2]").click()
