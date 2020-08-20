from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
# radio button and check boxes use the same methods
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

driver.get("https://www.seleniumeasy.com/test/basic-checkbox-demo.html")


check_box_1 = driver.find_element(By.ID, "isAgeSelected")
check_box_1.click()

if(check_box_1.is_selected()):
    logging.warning("radio button is selected")
else:
    logging.error("radio button is not selected")

driver.close()