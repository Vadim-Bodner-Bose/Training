from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chromeOptions = Options()  # object for options class
chromeOptions.add_experimental_option("prefs", {
    'download.default_directory': 'C:\DownloadSeleniumFiles'})  # define default directory

# CHROME
# create a driver
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe",
                          chrome_options=chromeOptions)  # add chrom options to driver init
# get the page
driver.get("https://www.seleniumeasy.com/test/generate-file-to-download-demo.html")
driver.maximize_window()

# Enter text for the file
driver.find_element(By.ID, 'textbox').send_keys('Vadim is learning to download files')
# Generate file
driver.find_element(By.ID, 'create').click()
# Download the file
driver.find_element(By.ID, 'link-to-download').click()

time.sleep(2)
driver.close()
