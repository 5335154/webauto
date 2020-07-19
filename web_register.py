'''
ECShop注册功能：
进入网页
找到【注册】
点击进入【注册】
注册输入框，输入数据，进行注册
注册成功，跳转页面
'''
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get("http://192.168.1.120/upload/")
driver.maximize_window()
driver.find_element(By.XPATH,'//font[@id="ECS_MEMBERZONE"]/a[2]').click()
driver.find_element(By.ID,"username").send_keys("mingming")
driver.find_element(By.ID,"email").send_keys("1336666@qq.com")
driver.find_element(By.ID,"password1").send_keys("123456")
driver.find_element(By.ID,"conform_password").send_keys("123456")
driver.find_element(By.NAME,"extend_field5").click()
driver.find_element(By.NAME, "extend_field5").send_keys("13112341234")

ele = driver.find_element(By.NAME,"sel_question")
select = Select(ele)
select.select_by_value("friend_birthday")
driver.find_element(By.NAME,"passwd_answer").send_keys("321")

driver.find_element(By.XPATH,'/html/body/div[5]/div[3]/div[1]/form/table/tbody/tr[9]/td[2]/label/a').click()
time.sleep(2)
handles = driver.window_handles
driver.switch_to.window(handles[0])
driver.find_element(By.NAME,"agreement").click()
time.sleep(2)
driver.find_element(By.NAME,"agreement").click()
time.sleep(2)
driver.find_element(By.NAME,"Submit").click()
time.sleep(4)

driver.quit()