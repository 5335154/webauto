from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

driver.find_element_by_name("wd").send_keys("足球")
time.sleep(2)
driver.find_element_by_id("su").click()
time.sleep(2)
driver.back()
driver.find_element_by_class_name("s_ipt").send_keys("王者荣耀")
time.sleep(2)
driver.find_element_by_id("su").click()
time.sleep(2)
# driver.find_element_by_link_text("王者荣耀官方网站-腾讯游戏").click()
time.sleep(2)
driver.find_element_by_partial_link_text("王者荣耀吧").click()
time.sleep(2)
driver.quit()