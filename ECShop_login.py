'''
前台登录
'''
from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

url = 'http://192.168.1.120/upload/'#前台
driver.get(url=url)
driver.implicitly_wait(10)#隐式等待
time.sleep(2)

user = 'zhoulisha'
pwd = 'abc123'

driver.find_element(By.XPATH,'//font[@id="ECS_MEMBERZONE"]/a[1]').click()#登录菜单
time.sleep(2)
driver.find_element(By.NAME,'username').clear()
driver.find_element(By.NAME,'username').send_keys(user) #输用户名
driver.find_element(By.NAME,'password').clear()
driver.find_element(By.NAME,'password').send_keys(pwd)  #输密码
driver.find_element(By.NAME,'remember').click() #勾选保存密码
driver.find_element(By.NAME,'submit').click()  #点击登录
time.sleep(2)

driver.quit()



