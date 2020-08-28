import logging
import os
import time

# Returns abs path relative to this file and not cwd
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class MobileTestError(object):
    pass


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.platform = driver.session['platformName']

    def find_element(self, locators, imp_sec=50, exp_sec=0):
        time.sleep(exp_sec)
        self.driver.implicitly_wait(imp_sec)
        element = None

        if 'android_accessibility_id' in locators and self.platform.lower() == "Android".lower() and element is None:
            try:
                list_of_objects_found = self.driver.find_elements_by_accessibility_id(
                    locators['android_accessibility_id'])
            except NoSuchElementException:
                list_of_objects_found = None

            if not list_of_objects_found:
                logging.warning("PAY YOUR ATTENTION: List of Android accessibility ids is empty for: " +
                      locators['android_accessibility_id'])
                element = None
            else:
                element = list_of_objects_found[0]
                logging.warning("ACCESSIBILITY ID USING")

        if 'android_id' in locators and self.platform.lower() == "Android".lower() and element is None:
            try:
                element = self.driver.find_element_by_id(locators['android_id'])
                logging.warning("ID USING")
            except NoSuchElementException:
                element = None
                logging.warning("An element could not be located for android_id: " + locators['android_id'])

        if 'android_xpath' in locators and self.platform.lower() == "Android".lower() and element is None:
            try:
                element = self.driver.find_element_by_xpath(locators['android_xpath'])
                logging.warning("XPATH USING")
            except NoSuchElementException:
                element = None
                logging.warning("An element could not be located for android_xpath: " + locators['android_xpath'])

        if 'ios_accessibility_id' in locators and self.platform.lower() == "iOS".lower() and element is None:
            try:
                list_of_objects_found = self.driver.find_elements_by_accessibility_id(locators['ios_accessibility_id'])
            except NoSuchElementException:
                list_of_objects_found = None

            if not list_of_objects_found:
                logging.warning("PAY YOUR ATTENTION: List of iOS accessibility ids is empty for: " +
                      locators['ios_accessibility_id'])
                element = None
            else:
                element = list_of_objects_found[0]

        if 'ios_xpath' in locators and self.platform.lower() == "iOS".lower() and element is None:
            try:
                element = self.driver.find_element_by_xpath(locators['ios_xpath'])
            except NoSuchElementException:
                element = None
                logging.warning("An element could not be located for ios_xpath: " + locators['ios_xpath'])

        if element is None:
            logging.warning("Locators: " + str(locators), "No appropriate locator found")

        return element

    def get_screenshot(self):
        # self.driver.save_screenshot(PATH("image.png"))
        return self.driver.get_screenshot_as_base64()

    def tap_on_element(self, element):
        actions = TouchAction(self.driver)
        actions.tap(element)
        actions.perform()

    def swipe_down(self):
        self.driver.execute_script('mobile: swipe', {'direction': 'down'})

    def is_ios(self):
        return self.driver.session['platformName'] == "iOS"

    def is_android(self):
        return self.driver.session['platformName'] == "Android"
