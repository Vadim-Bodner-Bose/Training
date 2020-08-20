from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
import logging, time

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")

# how many test boxes on a page, usually same class attribute.

input_boxes = driver.find_elements(By.CLASS_NAME,'form-control') # find mult elements by common value
logging.warning("# of input boxes found {}".format(input_boxes)) #return the length of the list of found input boxes

# populate text boxes
driver.find_element(By.ID, "user-message").send_keys("Hellow World")
driver.find_element(By.XPATH,'//*[@id="get-input"]/button').click()

# get status of the input box
assert driver.find_element(By.ID, "user-message").is_displayed()
assert driver.find_element(By.ID, "user-message").is_enabled()
driver.find_element(By.ID, "user-message").clear()
driver.find_element(By.ID, "user-message").send_keys("Select Me")
driver.find_element(By.ID, "user-message").click()


time.sleep(3)
driver.quit()