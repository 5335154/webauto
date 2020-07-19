'''
登录进入页面
点击我的账户
点击资金管理
进行充值
体现
查看账户明细
查看申请记录
'''
from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://192.168.1.120/upload/")
driver.find_element(By.XPATH, '//font[@id="ECS_MEMBERZONE"]/a[1]').click()  # 进入登录
driver.find_element(By.NAME, "username").send_keys("mingming")  # 输入用户名
driver.find_element(By.NAME, "password").send_keys("123456")  # 输入密码
driver.find_element(By.NAME, "remember").click()  # 勾选记住信息
driver.find_element(By.NAME, "submit").click()  # 点击登录
#点击我的账户
driver.find_element(By.XPATH,'//font[@id="ECS_MEMBERZONE"]/a[1]').click()
#点击资金管理
driver.find_element(By.XPATH,'//div[@class="userMenu"]/a[13]').click()
#进入资金管理后，点充值
driver.find_element(By.LINK_TEXT,"充值").click()
driver.find_element(By.NAME,"amount").send_keys("1000") #充值金额
driver.find_element(By.NAME,"user_note").send_keys("充点钱钱") #会员备注
driver.find_element(By.NAME,"payment_id").click() #勾选支付方式
driver.find_element(By.NAME,"submit").click() #提交申请
#立即使用支付宝支付
driver.find_element(By.XPATH,'//div[@class="userCenterBox boxCenterList clearfix"]/table/tbody/tr[5]/td/div/input').click()
#跳转支付页面后返回上一页
handles = driver.window_handles
driver.switch_to.window(handles[0])
driver.find_element(By.XPATH,'//div[@class="userMenu"]/a[13]').click()
#点击提现 /html/body/div[8]/div[2]/div/div/div/table/tbody/tr/td/a[2]
driver.find_element(By.LINK_TEXT,"提现").click()
driver.find_element(By.NAME,"amount").send_keys("1000") #提现金额
driver.find_element(By.NAME,"user_note").send_keys("地方三国杀") #会员备注
driver.find_element(By.NAME,"submit").click() #提交申请
#返回上一页
driver.find_element(By.XPATH,'//div[@class="boxCenterList RelaArticle"]/div/p[2]/a').click()
#查看账户明细
driver.find_element(By.LINK_TEXT,"查看帐户明细").click()
#查看申请记录
driver.find_element(By.LINK_TEXT,"查看申请记录").click()
#安全退出 /html/body/div[8]/div[1]/div/div/div/div/a[14]/img
driver.find_element(By.XPATH,'//div[@class="userMenu"]/a[14]/img').click()

time.sleep(3)
driver.quit()