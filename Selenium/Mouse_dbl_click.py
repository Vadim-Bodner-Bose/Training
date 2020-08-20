from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# CHROME
# chreate a driver
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
# get the page
driver.get("http://demo.guru99.com/test/simple_context_menu.html")
driver.maximize_window()

dbl_click = driver.find_element(By.XPATH,'//*[@id="authentication"]/button')

# create an object for ActionChains
action = ActionChains(driver)

action.double_click(dbl_click).perform()

# dismiss the alert that comes up after the dbl-click
driver.switch_to.alert.dismiss()



