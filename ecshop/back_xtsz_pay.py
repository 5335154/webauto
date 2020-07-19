'''
case:系统设置—支付方式—安装—编辑—卸载
'''

from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
url = "http://192.168.1.120/upload/admin"

driver.get(url=url)
driver.maximize_window()
driver.implicitly_wait(10)                    #隐式等待10秒

# 登录后台系统设置
driver.maximize_window()
driver.find_element(By.NAME,'username').clear()
driver.find_element(By.NAME,'username').send_keys('admin')
driver.find_element(By.NAME,'password').clear()
driver.find_element(By.NAME,'password').send_keys('banxian123')
driver.find_element(By.CLASS_NAME,'button').click()

# 切换到菜单的menu-frame,进入支付方式
driver.switch_to.frame('menu-frame')
time.sleep(1)
driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li[9]').click()
driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li[9]/ul/li[3]/a').click()         #进入支付方式
driver.switch_to.parent_frame()                                                      #跳出frame

# 切换到支付方式页面
driver.switch_to.frame('main-frame')
time.sleep(1)

driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[4]/td[7]/a[1]').click() #安装财付通即时到账
driver.find_element(By.NAME,'Submit').click()
time.sleep(4)

driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[4]/td[7]/a[3]').click() #安装财付通中介担保
driver.find_element(By.NAME,'Submit').click()
time.sleep(4)

driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[5]/td[7]/a').click() #安装双乾支付
driver.find_element(By.NAME,'Submit').click()
time.sleep(4)

driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[6]/td[7]/a').click() #安装余额支付
driver.find_element(By.NAME,'Submit').click()
time.sleep(4)

driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[7]/td[7]/a').click() #安装银行汇款/转账
driver.find_element(By.NAME,'Submit').click()
time.sleep(4)

driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[8]/td[7]/a').click() #安装首信易支付
driver.find_element(By.NAME,'Submit').click()
time.sleep(4)

driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[9]/td[7]/a').click() #安装网银在线
driver.find_element(By.NAME,'Submit').click()
time.sleep(4)

driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[10]/td[7]/a').click() #安装货到付款
driver.find_element(By.NAME,'Submit').click()
time.sleep(4)

driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[11]/td[7]/a').click() #安装环迅IPS
driver.find_element(By.NAME,'Submit').click()
time.sleep(4)

driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[12]/td[7]/a').click() #安装快钱人民币网关
driver.find_element(By.NAME,'Submit').click()
time.sleep(4)

driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[13]/td[7]/a').click() #安装paypal
driver.find_element(By.NAME,'Submit').click()
time.sleep(4)

driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[14]/td[7]/a').click() #安装paypal快速结帐
driver.find_element(By.NAME,'Submit').click()
time.sleep(4)

driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[15]/td[7]/a').click() #安装邮局汇款
driver.find_element(By.NAME,'Submit').click()
time.sleep(4)

driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[16]/td[7]/a').click() #安装快钱神州行支付
driver.find_element(By.NAME,'Submit').click()
time.sleep(4)

driver.save_screenshot('D:\截图\支付方式1.png')
js = "window.scrollTo(0,2000)"
driver.execute_script(js)
driver.save_screenshot('D:\截图\支付方式2.png')

# 编辑
driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[2]/td[7]/a[2]').click()   #编辑支付宝
driver.find_element(By.NAME,'pay_name').clear()
driver.find_element(By.NAME,'Submit').click()
time.sleep(4)
driver.find_element(By.NAME,'Reset').click()
driver.find_element(By.NAME,'Submit').click()
time.sleep(4)

# 卸载
driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[2]/td[7]/a[1]').click()  #卸载支付宝
driver.switch_to.alert.accept()
time.sleep(4)

driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[3]/td[7]/a[1]').click()  #卸载银联电子支付
driver.switch_to.alert.accept()
time.sleep(4)

driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[4]/td[7]/a[1]').click()  #卸载财付通及时到账
driver.switch_to.alert.accept()
time.sleep(4)

driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[4]/td[7]/a[2]').click()  #卸载财付通中介担保
driver.switch_to.alert.accept()
time.sleep(4)

driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[5]/td[7]/a[1]').click()  #卸载双乾支付
driver.switch_to.alert.accept()
time.sleep(4)

driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[6]/td[7]/a[1]').click()  #卸载余额支付
driver.switch_to.alert.accept()
time.sleep(4)

driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[7]/td[7]/a[1]').click()  #卸载银行汇款/转账
driver.switch_to.alert.accept()
time.sleep(4)

driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[8]/td[7]/a[1]').click()  #卸载首信易支付
driver.switch_to.alert.accept()
time.sleep(4)

driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[9]/td[7]/a[1]').click()  #卸载网银在线
driver.switch_to.alert.accept()
time.sleep(4)

driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[10]/td[7]/a[1]').click()  #卸载货到付款
driver.switch_to.alert.accept()
time.sleep(4)

driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[11]/td[7]/a[1]').click()  #卸载环迅IPS
driver.switch_to.alert.accept()
time.sleep(4)

driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[12]/td[7]/a[1]').click()  #卸载快钱人民币网关
driver.switch_to.alert.accept()
time.sleep(4)

driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[13]/td[7]/a[1]').click()  #卸载paypal
driver.switch_to.alert.accept()
time.sleep(4)

driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[14]/td[7]/a[1]').click()  #卸载paypal快速到账
driver.switch_to.alert.accept()
time.sleep(4)
driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[15]/td[7]/a[1]').click()  #卸载邮局汇款
driver.switch_to.alert.accept()
time.sleep(4)

driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[16]/td[7]/a[1]').click()  #卸载快钱神州行支付
driver.switch_to.alert.accept()
time.sleep(3)

driver.save_screenshot('D:\截图\支付方式卸载1.png')
js = "window.scrollTo(0,2000)"
driver.execute_script(js)
driver.save_screenshot('D:\截图\支付方式卸载2.png')

driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[2]/td[7]/a').click() #安装支付宝
driver.find_element(By.NAME,'Submit').click()
time.sleep(4)

driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[3]/td[7]/a').click() #安装银联
driver.find_element(By.NAME,'Submit').click()
time.sleep(4)

driver.quit()