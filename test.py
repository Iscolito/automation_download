# -*- coding = utf-8 -*-
# @Time : 2022/3/24 15:45
# @Author : Iscolito
# @File : test.py
# @Software : PyCharm

from selenium import webdriver
from selenium.webdriver.common.by import By
import json
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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


driver.get('https://pan.baidu.com/s/1VhRGYaZUS11AP1yh7SdG0g?pwd=as6y')

WebDriverWait(driver,timeout=60).until(EC.text_to_be_present_in_element((By.XPATH,"//*[@id='layoutMain']/div[1]/div[1]/div/div[3]/div/div/div[2]/a[1]"),u"保存到网盘"))
driver.find_element(By.XPATH, "//*[@id='layoutMain']/div[1]/div[1]/div/div[3]/div/div/div[2]/a[1]").click()
WebDriverWait(driver,timeout=60).until(EC.text_to_be_present_in_element((By.XPATH,"//*[@id='fileTreeDialog']/div[4]/a[2]"),u"确定"))
driver.find_element(By.XPATH,"//*[@id='fileTreeDialog']/div[4]/a[2]").click()
