#ECShop登录和加入购物车

from selenium import webdriver                          #引入webdriver
import time                                             #引入time
from selenium.webdriver.common.by import By             #引入By
from selenium.webdriver.support.select import Select    #引入Select


driver = webdriver.Chrome()
url = "http://localhost/upload/"

#1 点击登录，进入登录页面
driver.get(url=url)
driver.maximize_window()
time.sleep(2)
driver.find_element(By.LINK_TEXT,"登录").click()
time.sleep(2)
#2 清空、输入信息，勾选保存，点击登录
driver.find_element(By.NAME,'username').clear()
driver.find_element(By.NAME,'username').send_keys('wanghui')
driver.find_element(By.NAME,'password').send_keys('banxian123')
driver.find_element(By.ID,'remember').click()
driver.find_element(By.NAME,'submit').click()
time.sleep(5)
#3 选择特价商品第三个，点击进入
driver.find_element(By.XPATH,'/html/body/div[9]/div[3]/div[1]/div/ul[3]/li[1]/a/img').click()
time.sleep(2)
#4 清空数量，输入数量，打印本店价格和促销价格
driver.find_element(By.ID,"number").clear()
time.sleep(2)
driver.find_element(By.ID,"number").send_keys(2)
selfprice = driver.find_element(By.ID,"ECS_SHOPPRICE").text
print("本店价格:",selfprice)
cprice = driver.find_element(By.XPATH,'//form[@id="ECS_FORMBUY"]/ul[2]/li[1]/font[1]').text
print("促销价格:",cprice)
#5 点击【立即购买】
driver.find_element(By.CSS_SELECTOR,'li[class="padd"] img').click()
time.sleep(2)
#6 点击结算中心
driver.find_element(By.XPATH,'/html/body/div[7]/div[1]/table/tbody/tr/td[2]/a/img').click()
time.sleep(2)
#7 选择配送区域
# element = driver.find_element(By.ID,'selCountries_0')
# select = Select(element)
# select.select_by_visible_text('中国')
#
# element1 = driver.find_element(By.ID,'selProvinces_0')
# select1 = Select(element1)
# select1.select_by_visible_text('四川')
# time.sleep(2)
#
# element2 = driver.find_element(By.ID,'selCities_0')
# select2 = Select(element2)
# select2.select_by_visible_text('成都')
# time.sleep(2)
#
# element3 = driver.find_element(By.ID,'selDistricts_0')
# select3 = Select(element3)
# select3.select_by_visible_text('青羊区')
#8 填写信息
# driver.find_element(By.ID,'consignee_0').send_keys('王辉')
# driver.find_element(By.ID,'address_0').send_keys('海德七楼')
# driver.find_element(By.ID,'tel_0').send_keys('5335154')
# driver.find_element(By.ID,'sign_building_0').send_keys('东方广场')
# driver.find_element(By.ID,'email_0').send_keys('12@12.com')
# driver.find_element(By.ID,'zipcode_0').send_keys('621100')
# driver.find_element(By.ID,'mobile_0').send_keys('19150855945')
# driver.find_element(By.ID,'best_time_0').send_keys('12点')

#driver.find_element(By.NAME,'Submit').click()
#9 选择配送方式、支付方式
driver.find_element(By.NAME,'shipping').click()
driver.find_element(By.NAME,'payment').click()
#driver.find_element(By.XPATH,'//*[@id="theForm"]/div[11]/div[2]/input[1]').click()
driver.find_element(By.CSS_SELECTOR,'div[id="ECS_ORDERTOTAL"]+div input:nth-child(1)').click()
time.sleep(2)
#10 点击我的订单
driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/ul/li[2]/a').click()
time.sleep(2)
#11 切换到我的订单页面
handles = driver.window_handles
driver.switch_to.window(handles[-1])
time.sleep(2)
#12 点击我的订单
driver.find_element(By.XPATH,'/html/body/div[7]/div[1]/div/div/div/div/a[3]').click()
time.sleep(5)
#13 打印URL
print(driver.current_url)

driver.quit()