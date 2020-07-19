'''
1、商品管理-商品列表
2、添加新商品
3、删除新增的商品
'''
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()

url = 'http://192.168.1.120/upload/admin'#后台
driver.get(url=url)
driver.implicitly_wait(10)#隐式等待


user = 'admin'
pwd = 'banxian123'

driver.find_element(By.NAME,'username').clear()
driver.find_element(By.NAME,'username').send_keys(user) #输用户名
driver.find_element(By.NAME,'password').clear()
driver.find_element(By.NAME,'password').send_keys(pwd)  #输密码
driver.find_element(By.NAME,'remember').click() #勾选保存密码
driver.find_element(By.CLASS_NAME,'button').click()  #点击登录


#商品管理菜单
driver.switch_to.frame("menu-frame")
driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li[1]').click()
driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li[1]/ul/li[1]/a').click()
driver.switch_to.default_content()
time.sleep(2)
#添加新商品
goods_name='NIKE'
goods_sn='NIKE019'
driver.switch_to.frame("main-frame")
driver.find_element(By.XPATH,'//span[@class="action-span"]/a').click()

driver.find_element(By.NAME,'goods_name').send_keys(goods_name)#输入商品名称
driver.find_element(By.NAME,'goods_sn').send_keys(goods_sn)#输入商品货号
# driver.find_element(By.XPATH,'//table[@id="general-table"]/tbody/tr[3]/td[2]/a').click()#点击添加分类
# driver.find_element(By.NAME,'addedCategoryName').send_keys("计算机")#输入分类信息
# driver.find_element(By.XPATH,'//span[@id="category_add"]/a[1]').click()#点击确定

ele = driver.find_element(By.XPATH,'//table[@id="general-table"]/tbody/tr[3]/td[2]/select')
select = Select(ele)
select.select_by_visible_text("男装")
driver.find_element(By.NAME,'shop_price').send_keys("300")#本店售价
driver.find_element(By.NAME,'market_price').send_keys("400")#市场售价
driver.find_element(By.ID,'is_promote').click()
driver.find_element(By.ID,'promote_1').send_keys("280")#促销价

#修改开始日期
js = "document.getElementById('promote_start_date').removeAttribute('readonly')"
driver.execute_script(js)
driver.find_element(By.ID,'promote_start_date').send_keys('2020-07-20')
#修改结束日期
js = "document.getElementById('promote_end_date').removeAttribute('readonly')"
driver.execute_script(js)
driver.find_element(By.ID,'promote_end_date').send_keys('2020-08-20')
#上传商品图片
driver.find_element(By.NAME,'goods_img').send_keys('D:\\222.png')
#点击确定
driver.find_element(By.XPATH,'//div[@id="tabbody-div"]/form/div/input[2]').click()
#添加成功确认
driver.save_screenshot("D:\workspace\img\spgl_splb_003_添加商品.png")
driver.switch_to.default_content()#退出到默认fram
#返回上个页面,进行删除
handles = driver.window_handles
driver.switch_to.window(handles[0])
time.sleep(3)
#根据添加的商品货号筛选进行删除
driver.switch_to.frame("main-frame")
driver.find_element(By.NAME,'keyword').clear()
driver.find_element(By.NAME,'keyword').send_keys(goods_sn)
driver.find_element(By.CLASS_NAME,'button').click()#搜索框
time.sleep(2)
driver.find_element(By.XPATH,'//div[@id="listDiv"]/table[1]/tbody/tr[3]/td[11]/a[4]/img').click()
time.sleep(2)
driver.switch_to.alert.accept()#删除
driver.save_screenshot("D:\workspace\img\spgl_splb_003_删除商品.png")

driver.switch_to.default_content()

#退出
driver.quit()