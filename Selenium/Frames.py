from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import logging, time

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

driver.get("https://chercher.tech/practice/frames-example-selenium-webdriver")

# switch to a frame and click on something in it
# driver.switch_to.frame(By.name<or ID>)

# driver.switch_to_frame(By.ID)
driver.switch_to.frame(driver.find_element(By.ID, 'frame1'))

driver.find_element(By.XPATH, '/html/body/input').send_keys("Soccer Champs - Rostov")

driver.switch_to.default_content() # go back to main view, else can't switch to a dif frame

driver.switch_to.frame('frame2')

drop_down = Select(driver.find_element(By.ID,'animals')) # for drop down need to select the object first
drop_down.select_by_value('avatar')




