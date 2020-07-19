'''
登录后台
进入订单管理
进入订单列表
对订单列表进行搜索、查询、删除、打印
'''
from selenium import webdriver #引入webdriver
import time  #引入时间
from selenium.webdriver.common.by import By #引入By类
from selenium.webdriver.common.action_chains import  ActionChains #引入ActionChains类
from selenium.webdriver.common.keys import Keys #引入keys
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://192.168.1.120/upload/admin")
#登录后台账户和密码
driver.find_element(By.NAME,"username").send_keys("admin")
driver.find_element(By.NAME,"password").send_keys("banxian123")
driver.find_element(By.CLASS_NAME,"button").click()
#进入左边内联框架
driver.switch_to.frame("menu-frame")
#点击订单管理
driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li[3]').click()
#点击订单列表
driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li[3]/ul/li[1]/a').click()
driver.switch_to.parent_frame() #退回到上一层frame
time.sleep(2)
driver.switch_to.frame("main-frame") #进入到main—frame
#实现鼠标悬浮
ele = driver.find_element(By.XPATH,'//a[@id="order_0"]')
action = ActionChains(driver)
action.move_to_element(ele).perform()
#从悬浮图片上进入商品详情
driver.find_element(By.XPATH,'//div[@id="order_goods_layer"]/table/tbody/tr[2]/td[1]/a').click()
time.sleep(2)
#页面切换
handles = driver.window_handles
driver.switch_to.window(handles[0])
driver.switch_to.frame("main-frame") #进入main-frame页面
#点击订单号，进入订单详情页面
driver.find_element(By.XPATH,'//a[@id="order_0"]').click()
#点击进入上一个订单
driver.find_element(By.XPATH,'//form[@name="theForm"]/div[1]/table/tbody/tr[1]/td/div/input[1]').click()
#点击进入下一个订单
driver.find_element(By.CSS_SELECTOR,"input[name='next']").click()
#点击打印订单
driver.find_element(By.CSS_SELECTOR,'input[value="打印订单"]').click()
#返回上一页面
driver.switch_to.window(handles[0])
driver.switch_to.frame("main-frame")
#点击订单列表
driver.find_element(By.XPATH,'//span[@class="action-span"]/a').click()
#鼠标返回
driver.back()
#显示购物者信息
# driver.find_element(By.XPATH,'//form[@name="theForm"]/div[1]/table/tbody/tr[4]/td[2]/a[1]').click()
#点击支付方式编辑
driver.switch_to.frame("main-frame")
driver.find_element(By.XPATH,'//form[@name="theForm"]/div[1]/table/tbody/tr[5]/td[2]/a').click()
#选择支付方式
driver.find_element(By.XPATH,'//div[@class="list-div"]/table/tbody/tr[3]/td[1]/input').click()
driver.find_element(By.CLASS_NAME,"button").click()  #确定
#点击配送方式编辑
driver.find_element(By.XPATH,'//div[@class="list-div"]/table/tbody/tr[6]/td[2]/a').click()
#选择配送方式
driver.find_element(By.XPATH,'//div[@class="list-div"]/table/tbody/tr[3]/td[1]/input').click()
#选择我要报价
driver.find_element(By.NAME,"insure").click()
#确定
driver.find_element(By.NAME,"finish").click()
#配送方式，打印快递单
driver.find_element(By.XPATH,'//div[@class="list-div"]/table/tbody/tr[6]/td[2]/input').click()
#切回main-frame页面
driver.switch_to.window(handles[0])
driver.switch_to.frame("main-frame")
driver.find_element(By.XPATH,'//div[@class="list-div"]/table/tbody/tr[8]/th/a').click()
#点击确定
driver.find_element(By.NAME,"finish").click()
#退到最外层
driver.switch_to.default_content()
#进到header-frame
driver.switch_to.frame("header-frame")
#点击退出
driver.find_element(By.XPATH,'//div[@id="submenu-div"]/ul/li[1]/a/span').click()

time.sleep(3)
driver.quit()