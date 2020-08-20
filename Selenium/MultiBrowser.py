from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# CHROME
# chreate a driver
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
# get the page
driver.get("https://phptravels.com/demo/")

print("current url {}".format(driver.current_url))  #url of the page

print("HTML code {}".format(driver.page_source))    #html code for the page

print("Chrome Title {}".format(driver.title)) #title of the page

driver.close() #close the browser

# # IE
#
# # chreate a driver
# driver = webdriver.Ie(executable_path="C:\Drivers\IEDriverServer.exe")
# # get the page
# driver.get("https://phptravels.com/demo/")
#
# print("IE {}".format(driver.title)) #title of the page
#
# driver.close() #close the browser
#
#
# # FireFox
#
# # chreate a driver
# driver = webdriver.firefox(executable_path="C:\Drivers\geckodriver.exe")
# # get the page
# driver.get("https://phptravels.com/demo/")
#
# print("FF {}".format(driver.title)) #title of the page
#
# driver.close() #close the browser




