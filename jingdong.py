from selenium import webdriver                            #从selenium里引入webdriver
from selenium.webdriver.common.by import By               #从xx里引入By
import time                                               #引入time

driver = webdriver.Chrome()                               #实例化
url = "http://www.jd.com"                                 #实例化

driver.get(url=url)                                       #用位置变量 访问京东
#handles = driver.current_window_handle                   #获取窗口句柄并实例化
handle = driver.current_window_handle                    #获取当前窗口句柄并实例化
print(handle)                                            #打印句柄
time.sleep(2)                                             #等待2秒
driver.find_element(By.ID,"key").send_keys("华为手机")     #找到输入框 输入华为手机
time.sleep(2)
driver.find_element(By.CLASS_NAME,"button").click()       #点击搜索
time.sleep(2)
print(driver.current_url)                                 #打印网页地址
print(handle)                                             #打印句柄
driver.find_element(By.ID,"key").clear()                  #找到输入框清空
driver.find_element(By.ID,"key").send_keys("小米")         #输入小米
time.sleep(2)
driver.find_element(By.CLASS_NAME,"button").click()       #搜索
time.sleep(2)
# 找到第二个商品，并点击进入
driver.find_element(By.XPATH,'//div[@id="J_goodsList"]/ul/li[2]/div/div[1]/a/img').click()
time.sleep(2)
handles = driver.window_handles                          #获取所有窗口句柄
driver.switch_to.window(handles[-1])                      #切换到第二个窗口
time.sleep(2)
print(handles)                                              #打印句柄
# 找到商品价格
price = driver.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/div[3]/div/div[1]/div[2]/span[1]/span[2]").text
# 打印商品价格
print("价格:",price)
time.sleep(2)
#找到2年碎屏保，点击
driver.find_element(By.XPATH,'//div[@id="choose-service"]/div[2]/div/div[2]/div[1]/span[1]').click()
time.sleep(2)
#找到【加入购物车】并点击
driver.find_element(By.ID,"InitCartUrl").click()
time.sleep(2)
#切换到列表页面
driver.switch_to.window(handles[0])
time.sleep(2)
#清空输入框，搜索信息
driver.find_element(By.ID,'key').clear()
driver.find_element(By.ID,'key').send_keys('拯救者')
driver.find_element(By.XPATH,'//div[@id="search-2014"]/div/button/i').click()
time.sleep(2)
#点击第三个打开新窗口页面
driver.find_element(By.XPATH,'//div[@id="J_goodsList"]/ul/li[3]/div/div[1]/a/img').click()
time.sleep(2)
#获取新开页面的句柄，并切换到该页面
handles = driver.window_handles
driver.switch_to.window(handles[-1])
time.sleep(2)
#获取价格并打印
price = driver.find_element(By.XPATH,'/html/body/div[6]/div/div[2]/div[3]/div/div[1]/div[2]/span[1]/span[2]').text
print('价格：',price)
#获取当前页面地址
print(driver.current_url)
#加入购物车
driver.find_element(By.ID,"InitCartUrl").click()
time.sleep(2)
print(handles)
driver.quit()
