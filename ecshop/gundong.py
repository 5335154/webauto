'''
case:滚动页面再搜索
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

# 滚动
js = "window.scrollTo(0,1000)"
driver.execute_script(js)
time.sleep(1)
js = "window.scrollTo(0,0)"
driver.execute_script(js)
js = "window.scrollTo(0,2000)"
driver.execute_script(js)

# 商品详情
driver.find_element(By.XPATH,'//div[@id="show_hot_area"]/div[5]/a/img').click()

driver.save_screenshot('D:\截图\滚动.png')
driver.quit()
