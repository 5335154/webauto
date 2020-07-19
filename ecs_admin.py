#ECShop后台订单管理搜索，会员管理添加会员

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
url = 'http://localhost/upload/admin'

#1 进入后台页面并登录
driver.get(url=url)
driver.maximize_window()
driver.find_element(By.NAME,'username').clear()
time.sleep(1)
driver.find_element(By.NAME,'username').send_keys('admin')
driver.find_element(By.NAME,'password').clear()
time.sleep(1)
driver.find_element(By.NAME,'password').send_keys('banxian123')
#driver.find_element(By.ID,'remember').click()
driver.find_element(By.CLASS_NAME,'button').click()
time.sleep(3)

#2 切换到header-frame,从顶层进入订单管理页面
driver.switch_to.frame('header-frame')
driver.find_element(By.XPATH,'//div[@id="menu-div"]/ul/li[5]/a/span[1]').click()
time.sleep(2)

#3 切换到main-frame
driver.switch_to.default_content()   #跳出所有frame
driver.switch_to.frame('main-frame')  #进入main-frame这一层
#4 分别单独输入订单号、收货人、订单状态、进行搜索
driver.find_element(By.NAME,'order_sn').send_keys('2020071680969')
driver.find_element(By.CLASS_NAME,'button').click()
time.sleep(3)

driver.find_element(By.NAME,'order_sn').clear()
driver.find_element(By.NAME,'consignee').send_keys('王辉')
driver.find_element(By.CLASS_NAME,'button').click()
time.sleep(3)

driver.find_element(By.NAME,'consignee').clear()
element = driver.find_element(By.ID,'status')
select = Select(element)
select.select_by_visible_text("无效")
driver.find_element(By.CLASS_NAME,'button').click()
time.sleep(3)

#点击 待确认、代付款、代发货
driver.find_element(By.LINK_TEXT,'待付款').click()
time.sleep(3)
driver.find_element(By.LINK_TEXT,'待发货').click()
time.sleep(3)
driver.find_element(By.LINK_TEXT,'待确认').click()
time.sleep(3)

#查看某一个订单
driver.find_element(By.XPATH,'//div[@id="listDiv"]/table[1]/tbody/tr[3]/td[7]/a').click()
time.sleep(2)
# 点击订单列表返回
driver.find_element(By.CSS_SELECTOR,'span[class="action-span"]>a').click()
time.sleep(2)

# 进入左侧菜单栏的会员管理页面
driver.switch_to.default_content()   #跳出所有frame
driver.switch_to.frame('menu-frame')  #进入menu-frame这一层

driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li[7]').click()
time.sleep(3)

# 添加会员  输入信息
driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li[7]/ul/li[2]/a').click()
time.sleep(2)
# 切入main-frame页面
driver.switch_to.default_content()   #跳出所有frame
driver.switch_to.frame('main-frame')  #进入main-frame这一层

driver.find_element(By.NAME,'username').clear()
driver.find_element(By.NAME,'username').send_keys('我是王辉1')
driver.find_element(By.XPATH,'/html/body/div[1]/form/table/tbody/tr[2]/td[2]/input').send_keys('11121@21.com')
driver.find_element(By.NAME,'password').clear()
driver.find_element(By.NAME,'password').send_keys('5335154')
driver.find_element(By.NAME,'confirm_password').send_keys('5335154')
#会员等级
ele2 = driver.find_element(By.NAME,'user_rank')
select = Select(ele2)
select.select_by_index(1)
#性别
driver.find_element(By.XPATH,'/html/body/div[1]/form/table/tbody/tr[6]/td[2]/input[2]').click()
#出生日期
ele3 = driver.find_element(By.NAME,'birthdayYear')
select = Select(ele3)
select.select_by_visible_text('1993')

ele3 = driver.find_element(By.NAME,'birthdayMonth')
select = Select(ele3)
select.select_by_visible_text('10')

ele3 = driver.find_element(By.NAME,'birthdayDay')
select = Select(ele3)
select.select_by_visible_text('31')

driver.find_element(By.ID,'credit_line').send_keys('1000')
driver.find_element(By.NAME,'extend_field1').send_keys('121@121.com')
driver.find_element(By.NAME,'extend_field2').send_keys('283166183')
driver.find_element(By.NAME,'extend_field3').send_keys('5335154')
driver.find_element(By.NAME,'extend_field4').send_keys('5335154')
driver.find_element(By.NAME,'extend_field5').send_keys('19150855945')

driver.find_element(By.CLASS_NAME,'button').click()
time.sleep(4)

# 全选会员
driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[1]/th[1]/input').click()
time.sleep(3)

driver.find_element(By.ID,'btnSubmit').click()
time.sleep(1)
print(driver.switch_to.alert.text)
time.sleep(1)
driver.switch_to.alert.accept()
time.sleep(1)
print(driver.current_url)
time.sleep(3)

driver.quit()
