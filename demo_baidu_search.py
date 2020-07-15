from selenium import webdriver  #引入webdriver函数
import time  #引入时间函数
driver = webdriver.Chrome() #实例化

#1、访问百度页面
driver.get("http://www.baidu.com")

#2、找到输入框并输入信息
#driver.find_element_by_id('kw').send_keys("周星驰")
driver.find_element_by_name('wd').send_keys("phthon")
time.sleep(3)        #等待3秒

#3、点击【百度一下】
#driver.find_element_by_id('su').click()
driver.find_element_by_class_name('s_btn').click()
time.sleep(3)       #等待3秒

#4、点击搜索结果
# driver.find_element_by_link_text("python教程-【免费】教程").click()
driver.find_element_by_partial_link_text('教程-【免费】教程').click()
time.sleep(10)
driver.quit()      #关闭页面
