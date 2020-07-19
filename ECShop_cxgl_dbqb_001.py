'''
新增促销管理夺宝奇兵
搜索新增促销
查看新增促销详情
删除促销
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

#新增
#菜单促销管理-夺宝奇兵
driver.switch_to.frame("menu-frame")
driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li[2]').click()
driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li[2]/ul/li[1]/a').click()
driver.switch_to.default_content()

#添加夺宝奇兵
driver.switch_to.frame("main-frame")
driver.find_element(By.XPATH,'/html/body/h1/span[1]/a').click()#添加夺宝奇兵

snatch_name = '夺宝奇兵大礼包'
driver.find_element(By.NAME,'snatch_name').clear()
driver.find_element(By.NAME,'snatch_name').send_keys(snatch_name)#输入活动名称
driver.find_element(By.CLASS_NAME,'button').click()#点击搜索
ele = driver.find_element(By.XPATH,'//div[@class="main-div"]/form/table/tbody/tr[3]/td[2]/select[1]')
select = Select(ele)
select.select_by_value("134")
driver.find_element(By.NAME,'start_price').clear()
driver.find_element(By.NAME,'start_price').send_keys('100')#价格下限
driver.find_element(By.NAME,'end_price').clear()
driver.find_element(By.NAME,'end_price').send_keys('800')#价格上限
driver.find_element(By.NAME,'max_price').clear()
driver.find_element(By.NAME,'max_price').send_keys('500')#最多需支付的价格
driver.find_element(By.NAME,'cost_points').clear()
driver.find_element(By.NAME,'cost_points').send_keys('100')#消耗积分
driver.find_element(By.XPATH,'/html/body/div[1]/form/table/tbody/tr[10]/td[2]/textarea').send_keys("描述")
driver.find_element(By.XPATH,'/html/body/div[1]/form/table/tbody/tr[11]/td/input[1]').click()#点击确定
time.sleep(1)
driver.save_screenshot("D:\workspace\img\ECSop_cxgl_dbqb_001_添加.png")

driver.switch_to.default_content()
#搜索,查看详情
driver.switch_to.frame("main-frame")
driver.find_element(By.XPATH,'/html/body/div[1]/form/input[1]').clear()
driver.find_element(By.XPATH,'/html/body/div[1]/form/input[1]').send_keys(snatch_name)#关键字
driver.find_element(By.XPATH,'/html/body/div[1]/form/input[2]').click()#搜索
time.sleep(2)
driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[2]/td[8]/a[1]/img').click()#查看详情
driver.save_screenshot("D:\workspace\img\ECSop_cxgl_dbqb_001_查看详情.png")
time.sleep(3)


#搜索，修改
driver.back()
driver.switch_to.frame("main-frame")
driver.find_element(By.XPATH,'/html/body/div[1]/form/input[1]').clear()
driver.find_element(By.XPATH,'/html/body/div[1]/form/input[1]').send_keys(snatch_name)#关键字
driver.find_element(By.XPATH,'/html/body/div[1]/form/input[2]').click()#关键字搜索框
time.sleep(2)
driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[2]/td[8]/a[2]/img').click()#编辑
driver.find_element(By.XPATH,'/html/body/div[1]/form/table/tbody/tr[11]/td/input[1]').click()#点击确定
time.sleep(1)
driver.save_screenshot("D:\workspace\img\ECSop_cxgl_dbqb_001_修改.png")

driver.switch_to.default_content()

#搜索，删除
driver.switch_to.frame("main-frame")
# driver.find_element(By.XPATH,'/html/body/div[1]/form/input[1]').clear()
driver.find_element(By.XPATH,'/html/body/div[1]/form/input[1]').send_keys(snatch_name)#关键字
driver.find_element(By.XPATH,'/html/body/div[1]/form/input[2]').click()#搜索
time.sleep(2)
driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[2]/td[8]/a[3]/img').click()#删除
driver.switch_to.alert.accept()#删除确认
driver.save_screenshot("D:\workspace\img\ECSop_cxgl_dbqb_001_删除.png")

driver.switch_to.default_content()
#退出
driver.quit()



