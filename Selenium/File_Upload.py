from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

# CHROME
# create a driver
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
# get the page
driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
driver.maximize_window()

# scroll down to the desired element (will be on top of the screen, when scrolled)
upload_file = driver.find_element(By.XPATH,'//*[@id="photo"]') # find the element
driver.execute_script("arguments[0].scrollIntoView();", upload_file) # scroll to the desired element

# upload file, one can upload multiple files using the statement below
upload_file.send_keys('C://Users/rsmrostov/Documents/gitignore_global.txt')

time.sleep(2)
driver.close()