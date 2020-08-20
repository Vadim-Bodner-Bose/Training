from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

driver.get("https://phptravels.com/demo/")

print("page title",driver.title)    #title of the page
print("url of the page", driver.current_url)        #return the url

driver.find_element_by_xpath("//*[@id='mega-nav-navigation']/div/ul[2]/li/a").click()

time.sleep(5)




# driver.close()    # will close just the focused browser.
driver.quit()   #will close all the browsers, that are opened, in case clicking a button opens a new tap.


