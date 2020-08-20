from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import logging, time

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

driver.get("https://www.seleniumeasy.com/test/table-data-download-demo.html")

# XPATH of one row: //*[@id="example"]/tbody/tr[2]
# remove square brackets and the value to match all rows: //*[@id="example"]/tbody/tr

rows = len(driver.find_elements(By.XPATH, '//*[@id="example"]/tbody/tr')) # will find all matching elements in the table and report

# Xparth of one column: //*[@id="example"]/thead/tr/th[1]
# Remove the square brackets and value to match all xpath': //*[@id="example"]/thead/tr/th

cols = len(driver.find_elements(By.XPATH, '//*[@id="example"]/thead/tr/th')) # count # of columns in a table.

logging.warning("# of rows: {0} and # of columns: {1} in a table".format(rows, cols))

for r in range(2, rows+1):
    for c in range(1, cols+1):
        tbl_value = driver.find_element(By.XPATH, "//*[@id='example']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(tbl_value, end='\t')
        # logging.warning(tbl_value)
    print()



