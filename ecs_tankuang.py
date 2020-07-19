'''
弹窗处理
'''

from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = 'http://localhost/upload/'

driver.get(url=url)
driver.maximize_window()
time.sleep(2)
driver.find_element(By.LINK_TEXT,'收藏本站').click()
print(driver.switch_to.alert.text)
time.sleep(2)
driver.switch_to.alert.accept()
time.sleep(2)

driver.find_element(By.LINK_TEXT,'收藏本站').click()
print(driver.switch_to.alert.text)
time.sleep(2)
driver.switch_to.alert.dismiss()
time.sleep(2)

driver.quit()

# #引入WebDriverWait
# from selenium.webdriver.support.ui import WebDriverWait
# #引入expected_conditons类，并重命名为ES
# from selenium.webdriver.support import expected_conditions as EC
# #设置等待
# wait = WindowsError(driver,10,1)
# wait.until(EC.presence_of_element_located((By.ID,"kw")))
