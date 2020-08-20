#### HANDLES RECAPTURE ####

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import logging

driver = webdriver.Chrome("C:\Drivers\chromedriver.exe")

driver.get("http://thedemosite.co.uk/login.php")

print("Current URL ",driver.current_url)

input_Email = driver.find_element_by_xpath("/html/body/table/tbody/tr/td[1]/form/div/center/table/tbody/tr/td[1]/table/tbody/tr[1]/td[2]/p/input")
input_Password = driver.find_element_by_xpath("/html/body/table/tbody/tr/td[1]/form/div/center/table/tbody/tr/td[1]/table/tbody/tr[2]/td[2]/p/input")

assert input_Email.is_displayed()
assert input_Email.is_enabled()

input_Email.send_keys("user@phptravels.com")

assert input_Password.is_displayed()
assert input_Password.is_enabled()

input_Password.send_keys("demouser")


login = driver.find_element_by_xpath("/html/body/table/tbody/tr/td[1]/form/div/center/table/tbody/tr/td[1]/table/tbody/tr[3]/td[2]/p/input")
assert login.is_enabled()
assert login.is_displayed()
login.click()

time.sleep(5)

login_status = driver.find_element_by_xpath("/html/body/table/tbody/tr/td[1]/big/blockquote/blockquote/font/center/b")
assert login_status.text == "**Failed Login**"
logging.warning(login_status.text)


driver.quit()