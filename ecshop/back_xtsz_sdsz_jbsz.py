'''
case:后台——系统设置——商店设置——基本设置
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

# 进入基本设置——填写信息
driver.switch_to.frame('main-frame')
driver.find_element(By.ID,'basic-tab').click()

ele = driver.find_element(By.NAME,'value[201]')
select = Select(ele)
select.select_by_value('zh_cn')                                   #系统语言

driver.find_element(By.NAME,'value[202]').clear()
driver.find_element(By.NAME,'value[202]').send_keys("112233")     #ICP证书或ICP备案证书号

driver.find_element(By.NAME,'icp_file').send_keys('D:\\111.png')  #ICP 备案证书文件
driver.find_element(By.NAME,'watermark').send_keys('D:\\111.png') #水印文件
driver.find_element(By.ID,'value_205_5').click()                  #水印位置
driver.find_element(By.NAME,'value[206]').clear()
driver.find_element(By.NAME,'value[206]').send_keys('100')        #水印透明度
driver.find_element(By.ID,'value_207_1').click()                  #是否启用库存管理
driver.find_element(By.ID,'value_207_0').click()                  #是否启用库存管理
driver.find_element(By.NAME,'value[208]').clear()
driver.find_element(By.NAME,'value[208]').send_keys('1.5')        #市场价格比例

driver.find_element(By.ID,'value_209_1').click()                  #URL重写
print(driver.switch_to.alert.text)                                #获取弹窗的文本信息
driver.switch_to.alert.accept()                                   #确定

driver.find_element(By.ID,'value_209_2').click()                  #URL重写
print(driver.switch_to.alert.text)
driver.switch_to.alert.dismiss()

driver.find_element(By.ID,'value_209_0').click()                  #URL重写
driver.find_element(By.NAME,'value[210]').clear()
driver.find_element(By.NAME,'value[210]').send_keys('辉币')        #消费积分名称
driver.find_element(By.NAME,'value[211]').clear()
driver.find_element(By.NAME,'value[211]').send_keys('100')        #积分换算比例
driver.find_element(By.NAME,'value[212]').clear()
driver.find_element(By.NAME,'value[212]').send_keys('50')         #积分支付比例
driver.find_element(By.NAME,'value[213]').clear()
driver.find_element(By.NAME,'value[213]').send_keys("WH")         #商品货号前缀
driver.find_element(By.ID,'value_214_0').click()                  #用户评论是否需要审核
driver.find_element(By.ID,'value_214_1').click()                  #用户评论是否需要审核
driver.find_element(By.NAME,'no_picture').send_keys('D:\\111.png') #商品的默认图片
driver.find_element(By.NAME,'value[218]').send_keys('asdasdasd')   #统计代码
driver.find_element(By.NAME,'value[219]').clear()
driver.find_element(By.NAME,'value[219]').send_keys('7200')        #缓存存活时间（秒）
driver.find_element(By.NAME,'value[220]').clear()
driver.find_element(By.NAME,'value[220]').send_keys('30')          #会员注册赠送积分

ele = driver.find_element(By.NAME,'value[223]')
select = Select(ele)
select.select_by_value('8')                                        #默认时区

ele = driver.find_element(By.NAME,'value[224]')
select = Select(ele)
select.select_by_value('4096')                                     #附件上传大小

driver.save_screenshot('D:\截图\基本设置页面.png')
driver.find_element(By.NAME,'submit').click()

driver.save_screenshot('D:\截图\基本设置.png')
time.sleep(3)
driver.quit()