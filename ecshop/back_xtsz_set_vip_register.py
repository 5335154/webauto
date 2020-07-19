'''
case:系统设置—会员注册项设置—添加会员注册项—更改显示和必填—编辑—移除会员注册项
'''

from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
url = "http://192.168.1.120/upload/admin"

driver.get(url=url)
driver.maximize_window()
driver.implicitly_wait(10)                    #隐式等待10秒

# 登录后台系统设置
driver.maximize_window()
driver.find_element(By.NAME,'username').clear()
driver.find_element(By.NAME,'username').send_keys('admin')
driver.find_element(By.NAME,'password').clear()
driver.find_element(By.NAME,'password').send_keys('banxian123')
driver.find_element(By.CLASS_NAME,'button').click()

# 切换到菜单的menu-frame,进入会员注册项设置
driver.switch_to.frame('menu-frame')
time.sleep(1)
wait = WebDriverWait(driver,10,0.5)
wait.until(EC.presence_of_element_located((By.XPATH,'//ul[@id="menu-ul"]/li[9]')))
driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li[9]').click()
driver.find_element(By.LINK_TEXT,'会员注册项设置').click()
driver.save_screenshot('D:\截图\会员注册项设置页面.png')
driver.switch_to.parent_frame()        #跳出frame

# 切换到会员注册项设置frame页面
driver.switch_to.frame('main-frame')
time.sleep(1)

# 添加会员注册项
driver.find_element(By.LINK_TEXT,'添加会员注册项').click()

driver.find_element(By.CSS_SELECTOR,'input[type="submit"]').click()     #注册项名称为空直接提交
print(driver.switch_to.alert.text)
driver.switch_to.alert.accept()                                       #弹出框点确定

driver.find_element(By.NAME,'reg_field_name').clear()
driver.find_element(By.NAME,'reg_field_name').send_keys("王辉是谁？")   #注册项名称
driver.find_element(By.NAME,'reg_field_order').clear()
driver.find_element(By.NAME,'reg_field_order').send_keys('50')         #排序权值
driver.save_screenshot("D:\截图\添加会员注册项.png")
driver.find_element(By.CSS_SELECTOR,'input[type="submit"]').click()

driver.save_screenshot("D:\截图\添加会员注册项结果.png")
time.sleep(5)
# 更改是否显示和是否必填
driver.find_element(By.XPATH,'//table[@id="list-table"]/tbody/tr[2]/td[3]/img').click()
driver.find_element(By.XPATH,'//table[@id="list-table"]/tbody/tr[2]/td[3]/img').click()

driver.find_element(By.XPATH,'//table[@id="list-table"]/tbody/tr[4]/td[4]/img').click()
driver.find_element(By.XPATH,'//table[@id="list-table"]/tbody/tr[4]/td[4]/img').click()

# 编辑
driver.find_element(By.XPATH,'//table[@id="list-table"]/tbody/tr[2]/td[5]/a').click()

driver.find_element(By.NAME,'reg_field_name').send_keys(Keys.CONTROL,'a')
driver.find_element(By.NAME,'reg_field_name').send_keys(Keys.BACK_SPACE)
driver.find_element(By.CSS_SELECTOR,'input[type="submit"]').click()     #注册项名称为空直接提交
time.sleep(2)
print(driver.switch_to.alert.text)
driver.switch_to.alert.accept()                                       #弹出框点确定

driver.find_element(By.NAME,'reg_field_name').clear()
driver.find_element(By.NAME,'reg_field_name').send_keys("MSN1")   #注册项名称
driver.find_element(By.NAME,'reg_field_order').clear()
driver.find_element(By.NAME,'reg_field_order').send_keys('1')         #排序权值
driver.save_screenshot("D:\截图\编辑会员注册项1.png")
driver.find_element(By.CSS_SELECTOR,'input[type="submit"]').click()
time.sleep(5)

driver.find_element(By.XPATH,'//table[@id="list-table"]/tbody/tr[7]/td[5]/a').click()

driver.find_element(By.NAME,'reg_field_name').clear()
driver.find_element(By.NAME,'reg_field_name').send_keys("密码找回问题1")   #注册项名称
driver.find_element(By.NAME,'reg_field_order').clear()
driver.find_element(By.NAME,'reg_field_order').send_keys('2')         #排序权值
driver.save_screenshot("D:\截图\编辑会员注册项2.png")
driver.find_element(By.CSS_SELECTOR,'input[type="submit"]').click()
time.sleep(5)
# 移除会员注册项
driver.find_element(By.PARTIAL_LINK_TEXT,'移除').click()
print(driver.switch_to.alert.text)
driver.switch_to.alert.dismiss()                                #取消移除
driver.save_screenshot('D:\截图\刚添加的注册项.png')

driver.find_element(By.PARTIAL_LINK_TEXT,'移除').click()        #点击移除
print(driver.switch_to.alert.text)
driver.switch_to.alert.accept()                                  #确定

driver.save_screenshot("D:\截图\移除注册项.png")

driver.quit()