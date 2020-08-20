from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

# CHROME
# create a driver
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
# get the page
driver.get("http://demo.guru99.com/test/simple_context_menu.html")
driver.maximize_window()

right_click = driver.find_element(By.XPATH, '//*[@id="authentication"]/span')

# create an object for ActionChains
action = ActionChains(driver)

# context_click is a right_click
action.context_click(right_click).perform()

driver.find_element(By.XPATH, '//*[@id="authentication"]/ul/li[1]').click()

time.sleep(3)
driver.switch_to.alert.dismiss()
driver.close()
