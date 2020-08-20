from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import logging, time

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

driver.get("https://phptravels.com/demo/")

parent_hndl = driver.current_window_handle # get the handle to the current window
driver.find_element(By.XPATH,'//*[@id="mega-nav-navigation"]/div/ul[2]/li/a').click()

time.sleep(2)
child_hndl = driver.current_window_handle
all_handls = driver.window_handles #handles for all the open browsers

for handle in all_handls:
    driver.switch_to.window(handle)
    print("title of a window",driver.title)
    if driver.title == "Demo Script Test drive - PHPTRAVELS": # close specific window
        driver.close()

driver.quit()# close all the browser windows
