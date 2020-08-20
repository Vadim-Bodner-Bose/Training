from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

driver.get("https://phptravels.com/demo/")
time.sleep(5)
print(driver.title)

driver.get("http://thedemosite.co.uk/")
time.sleep(5)
print(driver.title)

driver.back() #will go back to the previous title
time.sleep(5)
print(driver.title)

driver.forward()
time.sleep(5)
print(driver.title)

driver.close()