'''
权限管理
新增管理员
编辑管理员
查看日志
移除管理员
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
username = "zho3l1ia"
emil = "906312a0@qq.com"
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
driver.save_screenshot("D:\workspace\img\qxgl_glylb_001_新增管理用户.png")


#编辑
driver.find_element(By.XPATH,'/html/body/h1/span[1]/a').click()
time.sleep(2)
driver.find_element(By.XPATH,'//table[@id="list-table"]/tbody/tr[2]/td[5]/a[3]').click()
newpwd = 'abc123'
driver.find_element(By.NAME,'old_password').send_keys(pwd1)#旧密码
driver.find_element(By.NAME,'new_password').send_keys(newpwd)#新密码
driver.find_element(By.NAME,'pwd_confirm').send_keys(newpwd)#确认密码

driver.find_element(By.CSS_SELECTOR,'input[type="submit"]').click()#确认
time.sleep(3)
driver.save_screenshot("D:\workspace\img\qxgl_glylb_001_编辑管理用户.png")

#s删除
driver.find_element(By.XPATH,'//table[@id="list-table"]/tbody/tr[2]/td[5]/a[4]/img').click()
driver.switch_to.alert.accept()
driver.save_screenshot("D:\workspace\img\qxgl_glylb_001_删除管理用户.png")

driver.switch_to.default_content()

#退出
driver.quit()



