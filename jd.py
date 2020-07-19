'''
case : javascript、滚动、悬浮选择类目
'''
from selenium import webdriver                    #引入webdriver
from selenium.webdriver.common.by import By       #引入By
import time                                       #引入time

from selenium.webdriver.common.keys import Keys   #引入Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select  #引入Select
from selenium.webdriver.common.action_chains import ActionChains #引入ActionChains
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()                       #实例化
url = "http://www.jd.com"
#进入京东
driver.get(url=url)
driver.maximize_window()
driver.implicitly_wait(30)
# time.sleep(2)

#driver.find_element(By.CSS_SELECTOR,'a[href="//phat.jd.com/10-183.html"]').click()
#driver.find_element(By.CSS_SELECTOR,'li[data-index="7"] a:nth-child(3)').click()
#print(text)

# javascript 输入
# driver.find_element(By.ID,'key').clear()
# js = "document.getElementById('key').value='足球'"
# driver.execute_script(js)
# time.sleep(5)
# driver.find_element(By.XPATH,'//div[@id="search"]/div/div[2]/button').click()
# time.sleep(5)
# driver.quit()

# 搜索框输入
# driver.find_element(By.ID,'key').clear()
# driver.find_element(By.ID,'key').send_keys('足球')
# time.sleep(2)
# driver.find_element(By.XPATH,'//div[@id="search"]/div/div[2]/button').click()
# time.sleep(5)
# driver.quit()

#获取页面大小
xy = driver.find_element(By.TAG_NAME,'html').size
print(xy)

#鼠标悬浮事件   家用电器——冰箱双开门  先引入ActionChains
element = driver.find_element(By.XPATH,'//div[@id="J_cate"]/ul/li[1]/a')
action = ActionChains(driver)
action.move_to_element(element).perform()
time.sleep(1)
#点击双门
driver.find_element(By.XPATH,'//div[@id="cate_item1"]/div[1]/div[2]/dl[4]/dd/a[4]').click()
# time.sleep(1)

#关闭当前页面
handles = driver.window_handles
driver.switch_to.window(handles[-1])
driver.close()
# time.sleep(1)

#悬浮事件2  选择地区 北京
handles = driver.window_handles
driver.switch_to.window(handles[-1])

ele = driver.find_element(By.CLASS_NAME,'ui-areamini-text')
ac = ActionChains(driver)
ac.move_to_element(ele).perform()
# time.sleep(1)
driver.find_element(By.XPATH,'//li[@id="ttbar-mycity"]/div/div[2]/div/div/div[34]/a').click()
# time.sleep(1)

# 拖拽事件
# ele2 = driver.find_element(By.XPATH,'//div[@id="J_cate"]/ul/li[1]/a')
# ele3 = driver.find_element(By.ID,'key')
# ac = ActionChains(driver)
# ac.drag_and_drop(ele2,ele3)
# ac.perform()

# time.sleep(5)

# 键盘事件
# driver.find_element(By.ID,'key').clear()
# driver.find_element(By.ID,'key').send_keys('周星驰')
# time.sleep(1)
# driver.find_element(By.ID,'key').send_keys(Keys.BACK_SPACE)
# time.sleep(1)
# driver.find_element(By.ID,'key').send_keys(Keys.CONTROL,"a")
# time.sleep(1)
# driver.find_element(By.ID,'key').send_keys(Keys.CONTROL,"x")
# time.sleep(1)
# driver.find_element(By.ID,'key').send_keys(Keys.CONTROL,"v")
# time.sleep(1)
# driver.find_element(By.ID,'key').send_keys(Keys.CONTROL,"a")
# time.sleep(1)
# driver.find_element(By.ID,'key').send_keys(Keys.CONTROL,"c")
# time.sleep(1)
# driver.find_element(By.ID,'key').send_keys(Keys.CONTROL,"v")
# driver.find_element(By.ID,'key').send_keys(Keys.CONTROL,"v")
# time.sleep(1)
# driver.find_element(By.ID,'key').send_keys(Keys.ENTER)
# time.sleep(3)


# 进入超级下面的商品 (滚动)
js = "window.scrollTo(1000,3000)"
driver.execute_script(js)
# time.sleep(1)
js = "window.scrollTo(0,0)"
driver.execute_script(js)
# time.sleep(1)
js = "window.scrollTo(500,9000)"
driver.execute_script(js)
# time.sleep(1)
js = "window.scrollTo(0,0)"
driver.execute_script(js)
# time.sleep(1)
js = "window.scrollTo(1000,1200)"
driver.execute_script(js)
# time.sleep(5)
driver.find_element(By.XPATH,'//div[@id="J_coupon"]/div[2]/div/div/div[1]/a/div[1]/div[2]/div[1]').click()
# time.sleep(5)



# 截图
# driver.save_screenshot('./screenshot.png')
# driver.get_screenshot_as_file('D:\screenshot.png')
driver.quit()