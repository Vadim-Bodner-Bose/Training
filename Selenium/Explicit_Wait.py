import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
driver.maximize_window()

driver.get("https://www.phptravels.net/home")
driver.implicitly_wait(10)
driver.switch_to_default_content()

# driver.find_element(By.XPATH, '//*[@id="dropdownCurrency"]')
# # driver.find_element(By.ID,'dropdownCurrency').click()
# driver.find_element(By.XPATH,'//*[@id="//header-waypoint-sticky"]/div[1]/div/div/div[2]/div/ul/li[3]/div/div/div/a[1]')\
#     .click()
# driver.find_element(By.XPATH, '//*[@id="loginfrm"]/div[3]/div[1]/label/span').send_keys('user@phptravels.com')
# driver.find_element(By.XPATH, '//*[@id="loginfrm"]/div[3]/div[2]/label/span').send_keys('demouser')
#
# driver.find_element(By.XPATH, '//*[@id="loginfrm"]/button').click()
#
# driver.close()


#  if(driver.find_element(By.XPATH, '//*[@id="gc-custom-header-nav-bar-acct-menu"]\
# /div/div/div/div/div[1]/div/div/a[1]').is_displayed()): # how to switch to the main menu?
#      print("login screen was displayed")

driver.find_element(By.XPATH,'//*[@id="search"]/div/div/div/div/div/nav/ul/li[2]/a').click() #flights
driver.find_element(By.XPATH, '//*[@id="flights"]/div/div/form/div/div/div[1]/div[1]/div/div[2]/label').click() #roundtr

# From = driver.find_element(By.XPATH,'//*[@id="select2-drop"]/div/input')
# From.clear()
# From.send_keys('BOS')

To = driver.find_element(By.XPATH, '//*[@id="s2id_location_to"]/a')
# To.clear()
To.send_keys('EWR')

Depart = driver.find_element(By.XPATH, '//*[@id="FlightsDateStart"]')
# Depart.clear()
Depart.send_keys('2020-08-10')

Return = driver.find_element(By.XPATH, '//*[@id="FlightsDateEnd"]')
# Depart.clear()
Depart.send_keys('2020-08-21')

driver.find_element(By.XPATH, '//*[@id="flights"]/div/div/form/div/div/div[3]/div[4]/button').click() #search


# driver.find_element(By.XPATH, '//*[@id="uitk-tabs-button-container"]/div[1]/li[1]/a/span').click()
# driver.find_element(By.XPATH, '//*[@id="wizard-flight-tab-roundtrip"]/div/div[1]/div/div[1]/div/div/div/button') \
#     .send_keys('New York, NY')
# driver.find_element(By.XPATH, '//*[@id="wizard-flight-tab-roundtrip"]/div/div[1]/div/div[3]/div/div/div/button') \
#     .send_keys('Boston, MA')


wait=WebDriverWait(driver, 10) #explicit wait

element = wait.until(EC.element_to_be_clickable((By.ID, 'searchform'))) \
    # define element to wait for
element.click()
time.sleep(3)

driver.close()


