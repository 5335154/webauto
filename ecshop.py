#ECShop 注册

from selenium import webdriver                    #引入webdriver
from selenium.webdriver.common.by import By       #引入By
import time                                       #引入time
from selenium.webdriver.support.select import Select  #引入Select

driver = webdriver.Chrome()                       #实例化
url = "http://localhost/upload/"

driver.get(url=url)                               #访问ecshop网页
driver.maximize_window()                          #页面最大化
time.sleep(2)
# 前台1

#1 跳转注册页面
driver.find_element(By.LINK_TEXT,'注册').click()
#2 输入注册信息，完成注册
driver.find_element(By.ID,"username").send_keys('wanghui')             #用户名
driver.find_element(By.ID,"email").send_keys('123@123.com')            #email
driver.find_element(By.ID,"password1").send_keys('banxian123')         #密码
driver.find_element(By.ID,"conform_password").send_keys('banxian123')  #确认密码
driver.find_element(By.NAME,"extend_field1").send_keys('123@123.com')  #MSN
driver.find_element(By.NAME,"extend_field2").send_keys('283166183')    #QQ
driver.find_element(By.NAME,"extend_field3").send_keys('5335154')      #办公电话
driver.find_element(By.NAME,"extend_field4").send_keys('5335154')      #家庭电话
driver.find_element(By.NAME,"extend_field5").send_keys('19150855945')  #手机
# 1) 找到下拉框
element = driver.find_element(By.TAG_NAME,"select")                    #找到下拉框并实例化
select = Select(element)                                               #实例化Select
#select.select_by_visible_text('我儿时居住地的地址？')                     #选择下拉框——密码提示问题
#select.select_by_index(3)                                             #通过索引选择
select.select_by_value('favorite_food')                                #通过value值选择
driver.find_element(By.NAME,"passwd_answer").send_keys('地球')          #密码问题答案
#3 点击会员注册
driver.find_element(By.NAME,'Submit').click()
time.sleep(5)

driver.quit()