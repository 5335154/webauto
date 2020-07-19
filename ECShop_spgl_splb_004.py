'''
1、商品管理-商品列表
2、修改商品
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

#选择商品修改
goods_newname = '商品新名字'
driver.switch_to.frame("main-frame")
driver.find_element(By.XPATH,'//div[@id="listDiv"]/table[1]/tbody/tr[3]/td[11]/a[2]/img').click()

driver.find_element(By.NAME,'goods_name').send_keys(goods_newname)#输入商品名称
#修改开始日期
js = "document.getElementById('promote_start_date').removeAttribute('readonly')"
driver.execute_script(js)
driver.find_element(By.ID,'promote_start_date').send_keys('2020-07-20')
#修改结束日期
js = "document.getElementById('promote_end_date').removeAttribute('readonly')"
driver.execute_script(js)
driver.find_element(By.ID,'promote_end_date').send_keys('2020-08-20')
#点击确定
driver.find_element(By.XPATH,'//div[@id="tabbody-div"]/form/div/input[2]').click()
#保存修改之后的图片
driver.save_screenshot("D:\workspace\img\spgl_splb_004_修改商品.png")
driver.switch_to.default_content()

#退出
driver.quit()