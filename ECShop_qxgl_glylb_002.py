'''
新增管理员
分配权限
'''
from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

url = 'http://192.168.1.120/upload/admin'#后台
driver.get(url=url)
driver.implicitly_wait(10)#隐式等待
time.sleep(2)

user = 'admin'
pwd = 'banxian123'

driver.find_element(By.NAME,'username').clear()
driver.find_element(By.NAME,'username').send_keys(user) #输用户名
driver.find_element(By.NAME,'password').clear()
driver.find_element(By.NAME,'password').send_keys(pwd)  #输密码
driver.find_element(By.NAME,'remember').click() #勾选保存密码
driver.find_element(By.CLASS_NAME,'button').click()  #点击登录
time.sleep(2)

#权限管理-管理员列表
driver.switch_to.frame("menu-frame")
driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li[8]').click()
driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li[8]/ul/li[1]/a').click()
driver.switch_to.default_content()

#新增管理员
driver.switch_to.frame("main-frame")
driver.find_element(By.XPATH,'/html/body/h1/span[1]/a').click()

#输入管理员信息
username = "zho3l1ia1"
emil = "906312a01@qq.com"
pwd1 = "abc123"
pwd2 = "abc123"
driver.find_element(By.NAME,'user_name').clear()
driver.find_element(By.NAME,'user_name').send_keys(username)#用户名
driver.find_element(By.NAME,'email').clear()
driver.find_element(By.NAME,'email').send_keys(emil)#邮箱
driver.find_element(By.NAME,'password').clear()
driver.find_element(By.NAME,'password').send_keys(pwd1)#密码
driver.find_element(By.NAME,'pwd_confirm').clear()
driver.find_element(By.NAME,'pwd_confirm').send_keys(pwd2)#确认密码

driver.find_element(By.CSS_SELECTOR,'input[type="submit"]').click()#确认
time.sleep(3)
driver.save_screenshot("D:\workspace\img\qxgl_glylb_002_新增管理用户.png")

#分配权限
ele = driver.find_elements(By.NAME,'chkGroup')
ele[0].click()
ele[1].click()
ele[2].click()
ele[3].click()
time.sleep(1)
driver.find_element(By.NAME,'Submit').click()
driver.save_screenshot("D:\workspace\img\qxgl_glylb_002_权限分配.png")

driver.switch_to.default_content()

#退出
driver.quit()



