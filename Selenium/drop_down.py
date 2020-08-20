from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import logging, time

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

driver.get("https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html")

drop_down = Select(driver.find_element(By.ID, "select-demo")) #select a class and create an object
#select by visible text
drop_down.select_by_visible_text('Sunday')
time.sleep(2)
#select by index starts with 0
drop_down.select_by_index('2')
time.sleep(2)
#select by value
drop_down.select_by_value('Thursday')
time.sleep(2)

#count number of options in the drop down
logging.warning("# of available options {}".format(len(drop_down.options))) #returns all the options in the drop down

all_options = drop_down.options

for opt in all_options:
    logging.warning("option: {}".format(opt.text))

driver.close()