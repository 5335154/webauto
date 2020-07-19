'''
1、商品管理-商品列表
2、删除新增的商品
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

#选择商品进行删除
driver.switch_to.frame("main-frame")
goods_sn = driver.find_element(By.XPATH,'//div[@id="listDiv"]/table[1]/tbody/tr[3]/td[3]/span').text #获取商品货号
driver.find_element(By.XPATH,'//div[@id="listDiv"]/table[1]/tbody/tr[3]/td[11]/a[4]/img').click()
driver.switch_to.alert.accept()#确认删除
time.sleep(2)
driver.save_screenshot("D:\workspace\img\spgl_splb_006_删除商品.png")
driver.switch_to.default_content()

#根据商品货号搜索
driver.switch_to.frame("main-frame")
driver.find_element(By.NAME,'keyword').clear()
driver.find_element(By.NAME,'keyword').send_keys(goods_sn)
driver.find_element(By.CLASS_NAME,'button').click()#搜索框
time.sleep(2)
driver.save_screenshot("D:\workspace\img\spgl_splb_006_搜索商品.png")
driver.switch_to.default_content()
#退出
driver.quit()
