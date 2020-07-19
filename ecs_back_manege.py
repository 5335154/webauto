# 商品管理——添加新商品

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

#2 切换到menu-frame,从顶层进入商品管理-添加商品页面
driver.switch_to.frame('menu-frame')
driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li').click()
time.sleep(2)
driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li/ul/li[2]/a').click()
time.sleep(2)

# 切换到添加商品页面的main-frame
driver.switch_to.parent_frame()
driver.switch_to.frame("main-frame")
time.sleep(2)
#输入信息
driver.find_element(By.NAME,'goods_name').send_keys('王辉牌半身裙')

# 选择字体样式
element = driver.find_element(By.NAME,'goods_name_style')
select = Select(element)
select.select_by_value("u")

#选择商品分类
element = driver.find_element(By.NAME,'cat_id')
select = Select(element)
select.select_by_value('125')

# 选择商品品牌
element = driver.find_element(By.NAME,'brand_id')
select = Select(element)
select.select_by_value('30')

# 促销价
driver.find_element(By.ID,'is_promote').click()
time.sleep(1)
driver.find_element(By.ID,'promote_1').clear()
driver.find_element(By.ID,'promote_1').send_keys('150')
time.sleep(1)

#选择日期
driver.execute_script("document.getElementById('promote_start_date').removeAttribute('readonly')")
driver.find_element(By.ID,'promote_start_date').clear()
driver.find_element(By.ID,'promote_start_date').send_keys('2030-01-03')
time.sleep(2)

driver.execute_script("document.getElementById('promote_end_date').removeAttribute('readonly')")
driver.find_element(By.ID,'promote_end_date').clear()
driver.find_element(By.ID,'promote_end_date').send_keys('2050-03-03')
time.sleep(5)

# 点击确定
driver.find_element(By.XPATH,'//div[@id="tabbody-div"]/form/div/input[2]').click()
time.sleep(5)

driver.quit()