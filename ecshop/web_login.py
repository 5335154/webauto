'''
已成功注册合法用户
进入ECShop页面
输入用户名和密码
点击登录
跳转页面
'''
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get("http://192.168.1.120/upload/")
driver.find_element(By.XPATH,'//font[@id="ECS_MEMBERZONE"]/a[1]').click()
driver.find_element(By.NAME,"username").send_keys("mingming")
driver.find_element(By.NAME,"password").send_keys("123456")
driver.find_element(By.NAME,"remember").click()
time.sleep(2)
driver.find_element(By.NAME,"submit").click()
time.sleep(5)
driver.quit()