#### HANDLES RECAPTURE ####

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome("C:\Drivers\chromedriver.exe")

driver.get("https://phptravels.com/demo/")


driver.find_element_by_xpath("//*[@id='mega-nav-navigation']/div/ul[2]/li/a").click()
time.sleep(6)
driver.get("https://phptravels.org/clientarea.php")
print("Current URL ",driver.current_url)

input_Email = driver.find_element_by_id("inputEmail")
input_Password = driver.find_element_by_id("inputPassword")

assert input_Email.is_displayed()
assert input_Email.is_enabled()

input_Email.send_keys(" user@phptravels.com")

assert input_Password.is_displayed()
assert input_Password.is_enabled()

input_Password.send_keys("demouser")

# recapture handler
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")))
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()


driver.switch_to_default_content()
login = driver.find_element_by_xpath("//*[@id='login']")
assert login.is_enabled()
assert login.is_displayed()
login.click()

driver.quit()