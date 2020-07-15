from selenium import webdriver
import time                         #引入时间函数
driver = webdriver.Chrome()         #实例化
driver.get("http://www.baidu.com")  #跳转百度页面
time.sleep(2)                       #等待2秒
driver.refresh()                    #刷新页面
time.sleep(2)                       #等待2秒
driver.get("http://www.taobao.com") #淘宝页面
time.sleep(2)                       #等待2秒
driver.back()                       #后退
time.sleep(2)                       #等待2秒
driver.forward()                    #前进
time.sleep(2)                       #等待2秒
driver.get("http://www.jd.com")     #京东页面
time.sleep(2)                       #等待2秒
driver.maximize_window()            #页面最大化
time.sleep(2)                       #等待2秒
driver.set_window_size(600,480)     #页面规定大小
time.sleep(2)                       #等待2秒
driver.close()                      #退出
time.sleep(2)                       #等待2秒
driver.quit()                       #退出所有窗口并关闭浏览器驱动