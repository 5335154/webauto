'''
case:购买商品后点击继续购买完成订单
'''

from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
url = "http://192.168.1.120/upload/"

driver.get(url=url)
driver.maximize_window()
driver.implicitly_wait(10)                    #隐式等待10秒

# 点击登录，进入登录页面
driver.get(url=url)
driver.maximize_window()
driver.find_element(By.LINK_TEXT,"登录").click()

# 清空、输入信息，勾选保存，点击登录
driver.find_element(By.NAME,'username').clear()
driver.find_element(By.NAME,'username').send_keys('wanghui')
driver.find_element(By.NAME,'password').send_keys('banxian123')
driver.find_element(By.ID,'remember').click()
driver.find_element(By.NAME,'submit').click()

# 点击商品显示详情
driver.find_element(By.XPATH,'//li[@class="goodsimg"]/a/img').click()

# 立即购买
driver.find_element(By.XPATH,'//form[@id="ECS_FORMBUY"]/ul[3]/li[2]/a/img').click()

# 继续购物
driver.find_element(By.CSS_SELECTOR,'form[id="formCart"]+table img:nth-child(1)').click()

# 继续选择商品 购买
js = "window.scrollTo(0,1000)"
driver.execute_script(js)
driver.find_element(By.XPATH,'//div[@id="show_new_area"]/div[3]/a/img').click()
driver.find_element(By.XPATH,'//form[@id="ECS_FORMBUY"]/ul[3]/li[2]/a/img').click()

# 点击结算中心
driver.find_element(By.XPATH,'/html/body/div[7]/div[1]/table/tbody/tr/td[2]/a/img').click()

# 选择配送方式、支付方式
driver.find_element(By.NAME,'shipping').click()
driver.find_element(By.NAME,'payment').click()
driver.find_element(By.CSS_SELECTOR,'div[id="ECS_ORDERTOTAL"]+div input:nth-child(1)').click()

# 点击我的订单
driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/ul/li[2]/a').click()

# 切换到我的订单页面
handles = driver.window_handles
driver.switch_to.window(handles[-1])

# 点击我的订单
driver.find_element(By.XPATH,'/html/body/div[7]/div[1]/div/div/div/div/a[3]').click()

# 截图
driver.save_screenshot("D:\截图\滚动页面购买.png")

driver.quit()

