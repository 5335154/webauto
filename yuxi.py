from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
time.sleep(2)
#driver.find_element_by_css_selector(".s_ipt").send_keys("足球")
#driver.find_element_by_css_selector("#kw").send_keys("王者荣耀")
#time.sleep(2)
#driver.find_element_by_css_selector(".bg.s_btn").click()
#driver.find_element_by_css_selector("[class='bg s_btn']").click()
#driver.find_element_by_css_selector('[type^=sub]").click()
#driver.find_element_by_css_selector("[type$=mit]").click()
#driver.find_element_by_css_selector("[type*=bmi]").click()

#driver.find_element_by_css_selector('').click()
#driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[3]/a[1]").click()
#driver.find_element_by_xpath("//a[@target='_blank']").click()
#driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[3]/a[5]").click()
#driver.find_element_by_xpath("//a[@target='_blank']").click()
#driver.find_element_by_xpath("/html/body/div/div/div/a[5]").click()  #绝对路径
#driver.find_element_by_xpath("//div[@id='s-top-left']/a[5]").click()  #相对路径
#driver.find_element_by_xpath("//a[5][text()='贴吧']").click()
driver.find_element_by_xpath("").click()
time.sleep(10)

driver.quit()