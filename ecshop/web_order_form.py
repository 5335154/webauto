'''
用户登录后，在首页进行商品选购
添加购物车
提交订单
产看订单
对订单进行合并，确认和取消
'''
from typing import Any, Union

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://192.168.1.120/upload/")
driver.find_element(By.XPATH, '//font[@id="ECS_MEMBERZONE"]/a[1]').click()  # 进入登录
driver.find_element(By.NAME, "username").send_keys("mingming")  # 输入用户名
driver.find_element(By.NAME, "password").send_keys("123456")  # 输入密码
driver.find_element(By.NAME, "remember").click()  # 勾选记住信息
driver.find_element(By.NAME, "submit").click()  # 点击登录
time.sleep(4)
driver.find_element(By.ID, "keyword").send_keys("毛衣")  # 找到搜索框，搜索毛衣
driver.find_element(By.NAME, "imageField").click()  # 点击搜索
# 找到第2个商品，点击进入商品详情页
driver.find_element(By.XPATH, '//form[@id="compareForm"]/div/div[2]/a/img').click()
# 清空默认商品数量
driver.find_element(By.NAME, "number").clear()
# 更改商品数量
driver.find_element(By.NAME, "number").send_keys("4")
# 点击添加购物车
driver.find_element(By.XPATH, '//form[@id="ECS_FORMBUY"]/ul[3]/li[2]/a/img').click()
# 进入购物车后，点击‘结算’
driver.find_element(By.XPATH, '//div[@class="flowBox"]/table/tbody/tr/td[2]/a/img').click()
# 进入添加收货人信息。引入下拉类。
# ele = driver.find_element(By.ID, "selCountries_0")  # 定位赋值,国家
# select = Select(ele)
# select.select_by_value("1")
# prov = driver.find_element(By.ID, "selProvinces_0")  # 定位赋值，省份
# select = Select(prov)
# select.select_by_value("26")
# citi = driver.find_element(By.ID, "selCities_0")  # 定位赋值，城市
# select = Select(citi)
# select.select_by_value("322")
# dist = driver.find_element(By.ID, "selDistricts_0")  # 定位赋值，区域
# select = Select(dist)
# select.select_by_value("2723")
# # 填写收货人姓名
# driver.find_element(By.NAME, "consignee").send_keys("明明")
# # 填写收货详细地址
# driver.find_element(By.NAME, "address").send_keys("成都市XXXXX")
# # 填写电话
# driver.find_element(By.NAME, "tel").send_keys("13312341234")
# # 填写邮箱
# driver.find_element(By.NAME, "email").clear()
# driver.find_element(By.NAME, "email").send_keys("1336666@qq.com")
# # 点击添加地址
# driver.find_element(By.NAME, "Submit").click()
# # 选择配送地址
driver.find_element(By.XPATH, '//table[@id="shippingTable"]/tbody/tr[2]/td[1]/input').click()
# 选择支付方式
driver.find_element(By.XPATH, '//table[@id="paymentTable"]/tbody/tr[2]/td[1]/input').click()

# 要实现窗口向下滚动
size = driver.find_element(By.TAG_NAME, "html").size
print(size)
#js = "window.scrollTo(0,1000)"
js = "window.scrollTo(0,%s)" % (size["height"]) #To(o小写),(0,%s)中是逗号
driver.execute_script(js)
#找到提交订单，点击
driver.find_element(By.XPATH,'//form[@id="theForm"]/div[11]/div[2]/input[1]').click()
#点击提交右上角我的订单
driver.find_element(By.XPATH,'//ul[@class="cart_info"]/li[2]/a').click()
#跳转页面
handles = driver.window_handles
driver.switch_to.window(handles[1])
#点击左边我的订单
driver.find_element(By.XPATH,'/html/body/div[7]/div[1]/div/div/div/div/a[3]').click()
#点击某一条订单信息
driver.find_element(By.XPATH,'/html/body/div[8]/div[2]/div/div/div/table/tbody/tr[4]/td[1]/a').click()
#查看发送/商家留言
# driver.find_element(By.XPATH,'/html/body/div[8]/div[2]/div/div/div/table[1]/tbody/tr[1]/td[2]/a').click()
driver.find_element(By.LINK_TEXT,"[发送/查看商家留言]").click()
#订单留言操作
driver.find_element(By.NAME,"msg_title").send_keys("毛衣")
driver.find_element(By.NAME,"msg_content").send_keys("你好")
driver.find_element(By.CLASS_NAME,"bnt_bonus").click()
#删除留言
driver.find_element(By.XPATH,'//div[@class="f_r"]/a').click()
driver.switch_to.alert.accept()
#回到我的订单列表
driver.find_element(By.XPATH,'/html/body/div[7]/div[1]/div/div/div/div/a[3]').click()
#取消订单
driver.find_element(By.XPATH,'/html/body/div[8]/div[2]/div/div/div/table/tbody/tr[2]/td[5]/font/a').click()
driver.switch_to.alert.dismiss()
order = driver.find_element(By.NAME,"to_order")  #找主订单
select = Select(order)
select.select_by_index(1)
#找从订单
order = driver.find_element(By.NAME,"from_order")
select = Select(order)
select.select_by_index(2)
#合并订单
driver.find_element(By.NAME,"Submit").click()
driver.switch_to.alert.accept()
time.sleep(5)
driver.quit()
