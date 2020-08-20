from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

# CHROME
# create a driver
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
# get the page
driver.get("https://www.seleniumeasy.com/test/drag-and-drop-demo.html")
driver.maximize_window()

drag = driver.find_element(By.XPATH, '//*[@id="todrag"]/span[1]')
drop = driver.find_element(By.XPATH, '//*[@id="mydropzone"]')
# drop = driver.find_element(By.ID, 'mydropzone') #or by ID since it's available.
# create an object for ActionChains
action = ActionChains(driver)

# context_click is a drag and drop, drag is the source input, drop is the target
action.drag_and_drop(drag,drop).perform()

time.sleep(3)
driver.close()
