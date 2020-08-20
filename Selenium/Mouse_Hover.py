from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# CHROME
# chreate a driver
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
# get the page
driver.get("https://demoqa.com/menu/")

main_menu2 = driver.find_element(By.XPATH, '//*[@id="nav"]/li[2]/a ')
sub_list = driver.find_element(By.XPATH, '//*[@id="nav"]/li[2]/ul/li[3]/a')
sub_item = driver.find_element(By.XPATH,'//*[@id="nav"]/li[2]/ul/li[3]/ul/li[1]/a')

# define actions class objects for actionchains class
actions = ActionChains(driver)

# move to the elements in the menu and click the last itme sub_item in the chain
actions.move_to_element(main_menu2).move_to_element(sub_list).move_to_element(sub_item).click().perform()


