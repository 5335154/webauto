'''
case:系统设置—配送方式—安装—设置区域—卸载
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

# 切换到菜单的menu-frame,进入配送方式
driver.switch_to.frame('menu-frame')
time.sleep(1)
driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li[9]').click()
driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li[9]/ul/li[4]/a').click()         #进入配送方式
driver.switch_to.parent_frame()                                                      #跳出frame

# 切换到配送方式页面
# 安装EMS国内邮政特快专递
driver.switch_to.frame('main-frame')
time.sleep(1)

driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[4]/td[8]/a').click()
time.sleep(4)

driver.find_element(By.NAME,'shipping_area_name').send_keys('金牛区')  #配送区域名称
driver.find_element(By.NAME,'base_fee').clear()
driver.find_element(By.NAME,'base_fee').send_keys('50')               #500克以内费用
driver.find_element(By.NAME,'step_fee').clear()
driver.find_element(By.NAME,'step_fee').send_keys('20')               #续重每500克或其零数的费用
driver.find_element(By.NAME,'free_money').clear()
driver.find_element(By.NAME,'free_money').send_keys('10')             #免费额度

driver.find_element(By.CSS_SELECTOR,'option[value="1"]').click()
driver.find_element(By.CSS_SELECTOR,'option[value="26"]').click()
driver.find_element(By.CSS_SELECTOR,'option[value="322"]').click()
driver.find_element(By.CSS_SELECTOR,'option[value="2724"]').click()

driver.find_element(By.CSS_SELECTOR,"input[type='button']").click()   #点击+
driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()   #点击确定
time.sleep(4)

# 编辑
driver.find_element(By.XPATH,'//table[@id="listTable"]/tbody/tr[2]/td[4]/a[1]').click()

driver.find_element(By.CSS_SELECTOR,'option[value="1"]').click()
driver.find_element(By.CSS_SELECTOR,'option[value="26"]').click()
driver.find_element(By.CSS_SELECTOR,'option[value="322"]').click()
driver.find_element(By.CSS_SELECTOR,'option[value="2725"]').click()

driver.find_element(By.CSS_SELECTOR,"input[type='button']").click()   #点击+
driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()   #点击确定
time.sleep(4)

# 新建配送区域
driver.find_element(By.CSS_SELECTOR,'span[class="action-span"]>a').click()

driver.find_element(By.NAME,'shipping_area_name').send_keys('龙泉驿区')  #配送区域名称
driver.find_element(By.NAME,'base_fee').clear()
driver.find_element(By.NAME,'base_fee').send_keys('40')               #500克以内费用
driver.find_element(By.NAME,'step_fee').clear()
driver.find_element(By.NAME,'step_fee').send_keys('10')               #续重每500克或其零数的费用
driver.find_element(By.NAME,'free_money').clear()
driver.find_element(By.NAME,'free_money').send_keys('5')             #免费额度

driver.find_element(By.CSS_SELECTOR,'option[value="1"]').click()
driver.find_element(By.CSS_SELECTOR,'option[value="26"]').click()
driver.find_element(By.CSS_SELECTOR,'option[value="322"]').click()
driver.find_element(By.CSS_SELECTOR,'option[value="2727"]').click()

driver.find_element(By.CSS_SELECTOR,"input[type='button']").click()   #点击+
driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()   #点击确定
time.sleep(4)

# 移除
driver.find_element(By.XPATH,'//table[@id="listTable"]/tbody/tr[3]/td[4]/a[2]').click()
driver.switch_to.alert.accept()

#返回配送方式页面
driver.find_element(By.XPATH,'//span[@id="search_id"]/a').click()
time.sleep(1)

driver.save_screenshot("D:\截图\安装配送方式.png")

# 卸载
driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[4]/td[8]/a[1]').click()
driver.switch_to.alert.accept()
time.sleep(4)

# 安装邮政快递包裹
driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[7]/td[8]/a').click()
time.sleep(4)

driver.find_element(By.CSS_SELECTOR,'input[value="by_number"]').click()
time.sleep(2)
driver.find_element(By.NAME,'shipping_area_name').send_keys('金牛区')  #配送区域名称
driver.find_element(By.NAME,'item_fee').clear()
driver.find_element(By.NAME,'item_fee').send_keys('10')               #单件商品费用
driver.find_element(By.NAME,'free_money').clear()
driver.find_element(By.NAME,'free_money').send_keys('10')             #免费额度

driver.find_element(By.CSS_SELECTOR,'option[value="1"]').click()
driver.find_element(By.CSS_SELECTOR,'option[value="26"]').click()
driver.find_element(By.CSS_SELECTOR,'option[value="322"]').click()
driver.find_element(By.CSS_SELECTOR,'option[value="2724"]').click()

driver.find_element(By.CSS_SELECTOR,"input[type='button']").click()   #点击+
driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()   #点击确定
time.sleep(4)

#删除
driver.find_element(By.CSS_SELECTOR,'input[type="checkbox"]').click()
driver.find_element(By.CSS_SELECTOR,'input[type="submit"]').click()
driver.switch_to.alert.accept()
time.sleep(4)

# 返回配送方式页面
driver.find_element(By.XPATH,'//span[@id="search_id"]/a').click()
time.sleep(1)

# 卸载
driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[7]/td[8]/a[1]').click()
driver.switch_to.alert.accept()

driver.save_screenshot("D:\截图\删除配送方式.png")
time.sleep(4)

driver.quit()