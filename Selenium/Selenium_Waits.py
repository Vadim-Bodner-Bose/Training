from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
driver.get("https://www.phptravels.net/home") #operning URL takes time
#want to wait some time
driver.implicitly_wait(5) #seconds, will now wait for each element, not just the page opening in driver.get.


print(driver.title)
account = driver.find_element_by_xpath('//*[@id="//header-waypoint-sticky"]/div[1]/div/div/div[2]/div/ul/li[3]/div').click()
login = driver.find_element_by_xpath('//*[@id="//header-waypoint-sticky"]/div[1]/div/div/div[2]/div/ul/li[3]/div/div/div/a[1]').click()
email = driver.find_element_by_xpath('//*[@id="loginfrm"]/div[3]/div[1]/label/input').send_keys("user@phptravels.com")
pwd = driver.find_element_by_xpath('//*[@id="loginfrm"]/div[3]/div[2]/label/input').send_keys("demouser")
submit = driver.find_element_by_xpath('//*[@id="loginfrm"]/button').click()

time.sleep(3)
driver.quit()

