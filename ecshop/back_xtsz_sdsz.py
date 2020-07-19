'''
case:后台——系统设置——商店设置——网店信息
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

# 切换到菜单的menu-frame,进入商店设置
driver.switch_to.frame('menu-frame')
time.sleep(1)
wait = WebDriverWait(driver,10,0.5)
wait.until(EC.presence_of_element_located((By.XPATH,'//ul[@id="menu-ul"]/li[9]')))
driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li[9]').click()
driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li[9]/ul/li[1]/a').click()
driver.save_screenshot('D:\截图\系统设置菜单栏.png')
driver.switch_to.parent_frame()        #跳出frame

# 切换到商店设置 main-frame  网店信息——填写
driver.switch_to.frame('main-frame')
driver.find_element(By.NAME,'value[101]').clear()
driver.find_element(By.NAME,'value[101]').send_keys("王辉的商店")
driver.find_element(By.NAME,'value[102]').clear()
driver.find_element(By.NAME,'value[102]').send_keys("商店标题是王辉")
driver.find_element(By.NAME,'value[103]').clear()
driver.find_element(By.NAME,'value[103]').send_keys("商店的描述是王辉")
driver.find_element(By.NAME,'value[104]').clear()
driver.find_element(By.NAME,'value[104]').send_keys("商店")

element = driver.find_element(By.NAME,'value[105]')
select = Select(element)
select.select_by_value('1')

element = driver.find_element(By.NAME,'value[106]')
select = Select(element)
select.select_by_value('26')

element = driver.find_element(By.NAME,'value[107]')
select = Select(element)
select.select_by_value('322')

driver.find_element(By.NAME,'value[108]').clear()
driver.find_element(By.NAME,'value[108]').send_keys("海德7楼")
driver.find_element(By.NAME,'value[109]').clear()
driver.find_element(By.NAME,'value[109]').send_keys("123456,234567,123123") #QQ
driver.find_element(By.NAME,'value[110]').clear()
driver.find_element(By.NAME,'value[110]').send_keys("123123,1123123")       #旺旺
driver.find_element(By.NAME,'value[111]').clear()
driver.find_element(By.NAME,'value[111]').send_keys("123123,11111")         #Skype
driver.find_element(By.NAME,'value[112]').clear()
driver.find_element(By.NAME,'value[112]').send_keys("123,321,1231")         #yahoo
driver.find_element(By.NAME,'value[113]').clear()
driver.find_element(By.NAME,'value[113]').send_keys("123@123.com")          #MSN
driver.find_element(By.NAME,'value[114]').clear()
driver.find_element(By.NAME,'value[114]').send_keys("123@123.com")          #客服邮件地址
driver.find_element(By.NAME,'value[115]').clear()
driver.find_element(By.NAME,'value[115]').send_keys("400-820-8820")         #客服电话
driver.find_element(By.NAME,'value[120]').clear()
driver.find_element(By.NAME,'value[120]').send_keys("这是王辉的用户中心公告")  #用户中心公告
driver.find_element(By.NAME,'value[121]').clear()
driver.find_element(By.NAME,'value[121]').send_keys("这是王辉的商店公告")      #商店公告

driver.find_element(By.NAME,'submit').click()                               #确定
driver.save_screenshot("D:\截图\网店信息.png")
time.sleep(2)

driver.quit()
