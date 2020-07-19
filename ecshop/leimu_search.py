'''
case:首页类目商品搜索
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

# 鼠标悬浮到类目——女装
ele = driver.find_element(By.XPATH,'//div[@id="HandleLI2_2"]/a')
action = ActionChains(driver)
action.move_to_element(ele).perform()

# 点击进入 半裙类
driver.find_element(By.XPATH,'//*[@id="DisSub2_2"]/div[6]/a[1]').click()

# 点击商品
driver.find_element(By.CSS_SELECTOR,'img[src="images/no_picture.gif"]').click()
time.sleep(3)
print("成功")
driver.save_screenshot('D:\截图\搜索商品.png')
driver.quit()