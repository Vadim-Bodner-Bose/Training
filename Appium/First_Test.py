from appium import webdriver
from appium.webdriver.webelement import By
# same as the configured session in appium GUI
desired_cap = {
  "automationName": "UiAutomator2",
  "app": "C:\\Users\\Vadim_Bodner\\Downloads\\Software\\Android APKs/com.bose.bosehear_10506_apps.evozi.com.apk",
  "deviceName": "CB5A2AGQ32",
  "platformName": "Android"
}
appium_server = 'http://localhost:4723/wd/hub'
driver = webdriver.Remote(appium_server, desired_cap)
driver.implicitly_wait(30)

priv_policy = driver.find_element(By.ID, 'com.bose.bosehear:id/privacy_policy_check_box')
priv_policy.click()

sign_in_cont = driver.find_element(By.ID, 'com.bose.bosehear:id/privacy_accept_button')
sign_in_cont.click()

# learn_more = driver.find_element(By.ID, 'com.bose.bosehear:id/website_button')
driver.find_element_by_accessibility_id('Learn More').click()
# learn_more.click()
driver.back()

driver.close()