'''
case:未登录状态，首页商品搜索,购买
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

# 搜索框为空搜索
driver.find_element(By.ID,"keyword").clear()
driver.find_element(By.NAME,'imageField').click()

print('为空搜索成功')
driver.save_screenshot("D:\截图\ecs_ss01.png")

# 点击商品查看详情页面，点击图片，查看大图，商品描述、属性、标签、相关商品
driver.find_element(By.XPATH,'//form[@id="compareForm"]/div/div[2]/a/img').click()
# ele = driver.find_element(By.ID,'sim650054')
# ac = ActionChains(driver)
# ac.move_to_element(ele).perform()
# driver.find_element(By.ID,'sim650054').click()
# driver.find_element(By.ID,'sim650054').click()

driver.find_element(By.XPATH,'//div[@id="imglist"]/a[2]/img').click()
driver.find_element(By.XPATH,'//div[@id="imglist"]/a[3]/img').click()
driver.find_element(By.XPATH,'//div[@id="com_b"]/h2[1]').click()
driver.find_element(By.XPATH,'//div[@id="com_b"]/h2[2]').click()
driver.find_element(By.XPATH,'//div[@id="com_b"]/h2[3]').click()
driver.find_element(By.XPATH,'//div[@id="com_b"]/h2[4]').click()

# 输入购买数量，点击购买
driver.find_element(By.ID,'number').send_keys(Keys.CONTROL,'a')
driver.find_element(By.ID,'number').send_keys('2')
driver.find_element(By.XPATH,'//form[@id="ECS_FORMBUY"]/ul[3]/li[2]/a/img').click()

# 结算中心
driver.find_element(By.XPATH,'/html/body/div[7]/div[1]/table/tbody/tr/td[2]/a/img').click()
# 点击不打算登录，直接购买
driver.find_element(By.XPATH,'//form[@id="loginForm"]/table/tbody/tr[5]/td/div/input[2]').click()
# 填写收货人信息
element = driver.find_element(By.ID,'selCountries_0')
select = Select(element)
select.select_by_visible_text('中国')

element1 = driver.find_element(By.ID,'selProvinces_0')
select1 = Select(element1)
select1.select_by_visible_text('四川')
time.sleep(2)

element2 = driver.find_element(By.ID,'selCities_0')
select2 = Select(element2)
select2.select_by_visible_text('成都')
time.sleep(2)

element3 = driver.find_element(By.ID,'selDistricts_0')
select3 = Select(element3)
select3.select_by_visible_text('青羊区')

driver.find_element(By.ID,'consignee_0').send_keys('王辉')
driver.find_element(By.ID,'address_0').send_keys('海德七楼')
driver.find_element(By.ID,'tel_0').send_keys('5335154')
driver.find_element(By.ID,'sign_building_0').send_keys('东方广场')
driver.find_element(By.ID,'email_0').send_keys('12@12.com')
driver.find_element(By.ID,'zipcode_0').send_keys('621100')
driver.find_element(By.ID,'mobile_0').send_keys('19150855945')
driver.find_element(By.ID,'best_time_0').send_keys('12点')

driver.find_element(By.NAME,'Submit').click()
# 选择配送方式和支付方式
driver.find_element(By.NAME,'shipping').click()
driver.find_element(By.NAME,'payment').click()
driver.find_element(By.CSS_SELECTOR,'div[id="ECS_ORDERTOTAL"]+div input:nth-child(1)').click()

print("完成")
driver.save_screenshot("D:\截图\搜索+购物.png")
time.sleep(1)
driver.quit()