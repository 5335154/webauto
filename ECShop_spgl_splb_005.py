'''
1、商品管理-商品列表
2、批量上架
'''
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()

url = 'http://192.168.1.120/upload/admin'#后台
driver.get(url=url)
driver.implicitly_wait(10)#隐式等待


user = 'admin'
pwd = 'banxian123'

driver.find_element(By.NAME,'username').clear()
driver.find_element(By.NAME,'username').send_keys(user) #输用户名
driver.find_element(By.NAME,'password').clear()
driver.find_element(By.NAME,'password').send_keys(pwd)  #输密码
driver.find_element(By.NAME,'remember').click() #勾选保存密码
driver.find_element(By.CLASS_NAME,'button').click()  #点击登录


#商品管理菜单
driver.switch_to.frame("menu-frame")
driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li[1]').click()
driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li[1]/ul/li[1]/a').click()
driver.switch_to.default_content()
time.sleep(2)

#全选当前页面商品进行批量上架操作
driver.switch_to.frame("main-frame")
driver.find_element(By.XPATH,'//div[@id="listDiv"]/table[1]/tbody/tr[1]/th[1]/input').click()

ele = driver.find_element(By.ID,'selAction')
select = Select(ele)
select.select_by_visible_text("上架")

#批量操作截图
driver.save_screenshot("D:\workspace\img\spgl_splb_005_批量上架.png")

#退出
driver.quit()