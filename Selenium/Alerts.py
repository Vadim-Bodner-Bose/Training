from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import logging, time

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

driver.get("https://www.seleniumeasy.com/test/javascript-alert-box-demo.html")

# alert is a popup where we can't access the element easily
driver.find_element(By.XPATH, '//*[@id="easycont"]/div/div[2]/div[2]/div[2]/button').click()

# driver.switch_to_alert().accept() #closes alert by choosing 'ok'
driver.switch_to_alert().dismiss() # closes by choosing 'cancel'


