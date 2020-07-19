'''
case:未登录状态，首页商品搜索,购买。
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

# 搜索框为空搜索
driver.find_element(By.ID,"keyword").clear()
driver.find_element(By.NAME,'imageField').click()

print('为空搜索成功')
driver.save_screenshot("D:\截图\ecs_ss01.png")

# 点击商品查看详情页面，点击图片，查看大图，商品描述、属性、标签、相关商品
driver.find_element(By.XPATH,'//form[@id="compareForm"]/div/div[2]/a/img').click()


driver.find_element(By.XPATH,'//div[@id="imglist"]/a[2]/img').click()
driver.find_element(By.XPATH,'//div[@id="imglist"]/a[3]/img').click()
driver.find_element(By.XPATH,'//div[@id="com_b"]/h2[1]').click()
driver.find_element(By.XPATH,'//div[@id="com_b"]/h2[2]').click()
driver.find_element(By.XPATH,'//div[@id="com_b"]/h2[3]').click()
driver.find_element(By.XPATH,'//div[@id="com_b"]/h2[4]').click()

# 输入购买数量，点击购买
driver.find_element(By.ID,'number').send_keys(Keys.CONTROL,'a')
driver.find_element(By.ID,'number').send_keys('2')
driver.find_element(By.XPATH,'//form[@id="ECS_FORMBUY"]/ul[3]/li[2]/a/img').click()

# 结算中心
js = "document.getElementByID('goods_number_139').value='4'"
driver.execute_script(js)
# driver.find_element(By.ID,'goods_number_139').send_keys(Keys.CONTROL,'a')
# driver.find_element(By.ID,'goods_number_139').send_keys('4')

time.sleep(4)
driver.find_element(By.XPATH,'/html/body/div[7]/div[1]/table/tbody/tr/td[2]/a/img').click()

time.sleep(2)
driver.quit()