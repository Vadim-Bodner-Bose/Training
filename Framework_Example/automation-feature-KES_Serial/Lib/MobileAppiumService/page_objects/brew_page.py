from Lib.MobileAppiumService.page_objects.main_menu_page import MainMenuPgHelper
import logging

class BrewLocators:
    LOCATOR_CUSTOM_SWITCHER = {
        "android_id": "com.keurig.kconnectent:id/custom_switcher",
        "android_accessibility_id": "customswitcher_main",
        "ios_accessibility_id": "customswitcher_main",
        "ios_xpath": "//XCUIElementTypeOther[@name=\"_switcher\"]"
    }
    LOCATOR_CUSTOM_SWITCHER_TEXT_FIELD_ON = {
        "android_xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android."
                         "widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
                         "android.widget.LinearLayout/android.widget.FrameLayout/android.widget."
                         "RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/"
                         "android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget."
                         "TextView",
        "android_accessibility_id": "textview_switcher_is_on",
        "ios_accessibility_id": "textview_switcher_is_on",
        "ios_xpath": "//XCUIElementTypeStaticText[@name=\"On\"]"
    }
    LOCATOR_CUSTOM_SWITCHER_TEXT_FIELD_OFF = {
        "android_xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android."
                         "widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
                         "android.widget.LinearLayout/android.widget.FrameLayout/android.widget."
                         "RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/"
                         "android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget."
                         "TextView",
        "android_accessibility_id": "textview_switcher_is_off",
        "ios_accessibility_id": "textview_switcher_is_off",
        "ios_xpath": "//XCUIElementTypeStaticText[@name=\"Off\"]"
    }
    LOCATOR_FEW_FIRST_STEPS_CANCEL_BUTTON = {
        "android_xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android"
                         ".widget.FrameLayout/android.widget.RelativeLayout/android.widget."
                         "ImageButton",
        "android_accessibility_id": "button_onboarding_close",
        "ios_accessibility_id": "button_onboarding_close",
        "ios_xpath": "//XCUIElementTypeButton[@name=\"ic onbrd close\"]"
    }
    LOCATOR_FEW_FIRST_STEPS_NEXT_BUTTON = {
        "android_xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android."
                         "widget.FrameLayout/android.widget.RelativeLayout/android.widget.Button",
        "android_accessibility_id": "button_onboarding_next",
        "ios_accessibility_id": "button_onboarding_next",
        "ios_xpath": "	//XCUIElementTypeButton[@name=\"NEXT\"]"
    }
    LOCATOR_RECIPE_CATEGORY = {"android_id": "com.keurig.kconnectent:id/text_category",
                               "android_accessibility_id": "textview_recipe_category",
                               "ios_accessibility_id": "textview_recipe_category"
                               }
    LOCATOR_KEURIG_BREW_BUTTON = {
        "android_id": "com.keurig.kconnectent:id/normal",
        "android_accessibility_id": "button_brew",
        "ios_accessibility_id": "button_brew",
        "ios_xpath": "//XCUIElementTypeImage[@name=\"Ready\"]"
    }
    LOCATOR_TAP_TO_CANCEL_HOT_WATER_BUTTON = {
        "android_id": "com.keurig.kconnectent:id/state_title",
        "android_accessibility_id": "textview_brew_state_title",
        "ios_accessibility_id": "textview_brew_state_title"
    }
    LOCATOR_TAP_TO_CANCEL_BREW_BUTTON = {
        "android_id": "com.keurig.kconnectent:id/state_title",
        "android_accessibility_id": "textview_brew_state_title",
        "ios_accessibility_id": "textview_brew_state_title"
    }
    LOCATOR_CHECK_YOUR_MUG_CONTINUE = {
        "android_id": "com.keurig.kconnectent:id/continue_button",
        "android_accessibility_id": "button_continue",
        "ios_accessibility_id": "button_continue"
        }
    LOCATOR_CHECK_YOUR_MUG_CANCEL_BREW = {
        "android_id": "com.keurig.kconnectent:id/cancel_brew_button",
        "android_accessibility_id": "button_cancel",
        "ios_accessibility_id": "button_cancel"
    }
    LOCATOR_BREW_CANCELLED_MAIN_TEXT = {
        "android_xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget."
                         "FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget."
                         "LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android."
                         "widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/"
                         "android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget."
                         "LinearLayout/android.widget.TextView[1]",
        "android_accessibility_id": "textview_brew_canceled_message",
        "ios_accessibility_id": "textview_brew_canceled_message"
    }
    LOCATOR_BREW_CANCELLED_OK_BUTTON = {
        "android_xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android."
                         "widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
                         "android.widget.LinearLayout/android.widget.FrameLayout/android.widget."
                         "RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/"
                         "android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.Button",
        "android_accessibility_id": "button_brew_canceled",
        "ios_accessibility_id": "button_brew_canceled"
    }
    LOCATOR_POD_RECOGNITION_TITLE = {"android_id": "com.keurig.kconnectent:id/pod_recognition_title",
                                     "android_accessibility_id": "textview_pod_recognition_title",
                                     "ios_accessibility_id": "textview_pod_recognition_title"
                                     }
    LOCATOR_POD_RECOGNITION_VARIETY = {"android_id": "com.keurig.kconnectent:id/pod_recognition_variety",
                                       "android_accessibility_id": "textview_pod_recognition_variety",
                                       "ios_accessibility_id": "textview_pod_recognition_variety"
                                       }
    LOCATOR_BUTTON_4OZ = {"android_id": "com.keurig.kconnectent:id/button_4oz",
                          "android_accessibility_id": "button_cup_size_Oz4",
                          "ios_accessibility_id": "button_cup_size_Oz4"
                          }
    LOCATOR_BUTTON_6OZ = {"android_id": "com.keurig.kconnectent:id/button_6oz",
                          "android_accessibility_id": "button_cup_size_Oz6",
                          "ios_accessibility_id": "button_cup_size_Oz6"
                          }
    LOCATOR_BUTTON_8OZ = {"android_id": "com.keurig.kconnectent:id/button_8oz",
                          "android_accessibility_id": "button_cup_size_Oz8",
                          "ios_accessibility_id": "button_cup_size_Oz8"
                          }
    LOCATOR_BUTTON_10OZ = {"android_id": "com.keurig.kconnectent:id/button_10oz",
                           "android_accessibility_id": "button_cup_size_Oz10",
                           "ios_accessibility_id": "button_cup_size_Oz10"
                           }
    LOCATOR_BUTTON_12OZ = {"android_id": "com.keurig.kconnectent:id/button_12oz",
                           "android_accessibility_id": "button_cup_size_Oz12",
                           "ios_accessibility_id": "button_cup_size_Oz12"
                           }


class BrewPgHelper(MainMenuPgHelper):

    # Click actions
    def switch_power(self):
        return self.find_element(BrewLocators.LOCATOR_CUSTOM_SWITCHER, 0, 3).click()

    def cancel_few_first_steps(self):
        return self.find_element(BrewLocators.LOCATOR_FEW_FIRST_STEPS_CANCEL_BUTTON).click()

    def click_start_brewing(self):
        return self.find_element(BrewLocators.LOCATOR_KEURIG_BREW_BUTTON).click()

    def click_cancel_brew(self):
        return self.find_element(BrewLocators.LOCATOR_TAP_TO_CANCEL_HOT_WATER_BUTTON).click()

    def click_check_your_mug_continue_brew(self):
        return self.find_element(BrewLocators.LOCATOR_CHECK_YOUR_MUG_CONTINUE).click()

    def click_check_your_mug_cancel_brew(self):
        return self.find_element(BrewLocators.LOCATOR_CHECK_YOUR_MUG_CANCEL_BREW).click()

    def click_brew_cancelled_ok_button(self):
        return self.find_element(BrewLocators.LOCATOR_BREW_CANCELLED_OK_BUTTON).click()

    def click_4oz_button(self):
        return self.find_element(BrewLocators.LOCATOR_BUTTON_4OZ).click()

    def click_8oz_button(self):
        return self.find_element(BrewLocators.LOCATOR_BUTTON_8OZ).click()

    # Is element visible
    def check_if_power_on(self):
        return self.find_element(BrewLocators.LOCATOR_CUSTOM_SWITCHER_TEXT_FIELD_ON, exp_sec=3).text == "On"

    def check_if_power_off(self):
        return self.find_element(BrewLocators.LOCATOR_CUSTOM_SWITCHER_TEXT_FIELD_OFF).text == "Off"

    def check_if_continue_brew_shown(self):
        element = self.find_element(BrewLocators.LOCATOR_CHECK_YOUR_MUG_CONTINUE, 5)
        if element is not None:
            return element.is_displayed()
        else:
            return False

    def check_if_keurig_brew_button_shown(self):
        element = self.find_element(BrewLocators.LOCATOR_KEURIG_BREW_BUTTON)
        if element is not None:
            return element.text == ""
        else:
            return False

    def check_if_tap_to_cancel_hot_water_button_shown(self):
        element = self.find_element(BrewLocators.LOCATOR_TAP_TO_CANCEL_HOT_WATER_BUTTON, 5)
        if element is not None:
            return element.is_displayed()
        else:
            return False

    def check_if_tap_to_cancel_brew_button_shown(self):
        element = self.find_element(BrewLocators.LOCATOR_TAP_TO_CANCEL_BREW_BUTTON, 5)
        logging.warning("cancel_brew_button element is: {}".format(element))
        if element is not None:
            return element.is_displayed()
        else:
            return False

    def check_if_tap_to_canceling_hot_water_button_shown(self):
        element = self.find_element(BrewLocators.LOCATOR_TAP_TO_CANCEL_BREW_BUTTON, 5)
        if element is not None:
            return element.is_displayed()
        else:
            return False

    # Get text from element
    def get_hot_water_lable_text(self):
        return self.find_element(BrewLocators.LOCATOR_RECIPE_CATEGORY).text

    def get_tap_to_cancel_hot_water_button_text(self):
        my_string = self.find_element(BrewLocators.LOCATOR_TAP_TO_CANCEL_HOT_WATER_BUTTON, 5).text
        return " ".join(my_string.splitlines())

    def get_brew_cancelled_main_text(self):
        return self.find_element(BrewLocators.LOCATOR_BREW_CANCELLED_MAIN_TEXT).text

    def get_pod_recognition_title_text(self):
        return self.find_element(BrewLocators.LOCATOR_POD_RECOGNITION_TITLE).text

    def get_pod_recognition_variety_text(self):
        return self.find_element(BrewLocators.LOCATOR_POD_RECOGNITION_VARIETY).text
