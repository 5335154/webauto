from selenium import webdriver
import time

driver = webdriver.Chrome()
url = "http://www.taobao.com"
#进入淘宝，搜索鞋
driver.get(url=url)
time.sleep(2)
driver.find_element_by_xpath("//*[@id='q']").send_keys("鞋")
driver.find_element_by_xpath("//*[@id='q']").submit()        #回车
#time.sleep(2)
#绝对路径
#driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div[1]/div[2]/form/div[1]/button").click()
#相对路径  通常把*换成具体的，可以提高效率，而且建议这样做
#driver.find_element_by_xpath('//*[@id="J_TSearchForm"]/div[1]/button').click()
#driver.find_element_by_xpath('//form[@id="J_TSearchForm"]/div[1]/button').click()
#属性搜索
#driver.find_element_by_xpath("//button[@class='btn-search tb-bg']").click()
#文本搜索
#driver.find_element_by_xpath("//button[text()='搜索']").click()
#文本模糊搜索
#driver.find_element_by_xpath("//button[contains(text(),'搜')]").click()
#time.sleep(2)

#返回上一页面
#driver.back()
# css_selector搜索
#driver.find_element_by_css_selector('#q').send_keys("阿迪达斯")
#time.sleep(2)
#driver.find_element_by_css_selector('div[class="search-button"]>button').click()
#driver.find_element_by_css_selector('.btn-search.tb-bg').click()
#driver.find_element_by_css_selector('div[class="search-button"]>button').click()
#driver.find_element_by_css_selector('form[id="J_TSearchForm"] button').click()
#driver.find_element_by_css_selector('button[class^=btn-search]').click()
#driver.find_element_by_css_selector('button[class$=tb-bg]').click()
#driver.find_element_by_css_selector('button[class*=search]').click()
# driver.find_element_by_css_selector('div[class="search-hots-fline"] :nth-child(4)').click()
# driver.find_element_by_css_selector('div[class="search-hots-fline"] :nth-of-type(1)').click()
time.sleep(3)
#driver.back()
#点击半身裙
#driver.find_element_by_css_selector('li[class="pipe"]+li+li>a').click()
# time.sleep(2)
# driver.find_element_by_css_selector('//div[class="search-hots-fline"]/a[6]').click()
# time.sleep(2)
driver.quit()