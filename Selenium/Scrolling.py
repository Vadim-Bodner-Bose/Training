from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import logging, time

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

driver.get("https://www.seleniumeasy.com/test/table-data-download-demo.html")

# options to scroll:
# by pixel
# till element is found
# to the end of the page

driver.maximize_window()

# driver.execute_script("window.scrollBy(0,500)", "") # scroll by pixels will move from top position 500 pixels down

# scroll down to the desired element (will be on top of the screen, when scrolled)
# desired_el = driver.find_element(By.XPATH,'//*[@id="example"]/tbody/tr[10]/td[1]') # find the element to scroll to
# driver.execute_script("arguments[0].scrollIntoView();", desired_el) # scroll to the desired eleemnt

# scroll down to the end of the page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")