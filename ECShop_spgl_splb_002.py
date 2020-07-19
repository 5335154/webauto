'''
商品管理-商品列表
查看商品详情
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

#商品管理菜单
driver.switch_to.frame("menu-frame")
driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li[1]').click()
driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li[1]/ul/li[1]/a').click()
time.sleep(2)
driver.switch_to.default_content()

#商品列表页面,查看
driver.switch_to.frame("main-frame")
driver.find_element(By.XPATH,'//div[@id="listDiv"]/table[1]/tbody/tr[3]/td[11]/a[1]/img').click()
time.sleep(2)

#切换商品详情页面
handles = driver.window_handles
driver.switch_to.window(handles[-1])
print("这是商品详情页面：",driver.current_url)

driver.save_screenshot("D:\workspace\img\spgl_splb_002.png")
driver.quit()