from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
import logging, time

# how many links on a page
# capture all the links on a web-page
# click on the links

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

driver.get("https://www.phptravels.net/home")

links = driver.find_elements(By.TAG_NAME, 'a') # links have a tag named 'a'
logging.warning(len(links))

cnt=0
for lnk in links:
    cnt+=1
    logging.warning("Discovered Link No.{} is {}".format(cnt, lnk.text))

our_partners = driver.find_element(By.PARTIAL_LINK_TEXT, 'Our Partners')
assert our_partners
our_partners.click

assert driver.find_element(By.LINK_TEXT, 'Our Partners')


time.sleep(1)
driver.close()



