from Lib.MobileAppiumService.page_objects.base_app import BasePage


class GateLocators:
    # TODO: Uncomment android_accessibility_id and ios_accessibility_id when application with new IDs will be available
    LOCATOR_SHOP_NOW = {
        "android_xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                         ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                         ".RelativeLayout/android.widget.RelativeLayout[1]/android.widget.Button ",
        "android_accessibility_id": "button_shop_now",
        "ios_accessibility_id": "button_shop_now",
        "ios_xpath": "//XCUIElementTypeButton[@name=\"SHOP NOW\"]"
    }
    LOCATOR_GET_CONNECTED = {
        "android_xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                         ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                         ".RelativeLayout/android.widget.RelativeLayout[2]/android.widget.Button ",
        "android_accessibility_id": "button_get_connected",
        "ios_accessibility_id": "button_get_connected",
        "ios_xpath": "//XCUIElementTypeButton[@name=\"GET CONNECTED\"]"
    }
    LOCATOR_SIGN_IN = {
        "android_xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                         ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                         ".RelativeLayout/android.widget.RelativeLayout[3]/android.widget.Button[1] ",
        "android_accessibility_id": "button_sign_in",
        "ios_accessibility_id": "button_sign_in",
        "ios_xpath": "//XCUIElementTypeStaticText[@name=\"Sign In\"]"
    }
    LOCATOR_SIGN_UP = {
        "android_xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                         "/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android"
                         ".widget.RelativeLayout[3]/android.widget.Button[2] ",
        "android_accessibility_id": "button_sign_up",
        "ios_accessibility_id": "button_sign_up",
        "ios_xpath": "//XCUIElementTypeStaticText[@name=\"Sign Up\"]"
    }
    LOCATOR_VERSION = {
        "android_xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                         "/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android"
                         ".widget.RelativeLayout[4]/android.widget.LinearLayout/android.widget.TextView[1] ",
        "android_accessibility_id": "textview_version",
        "ios_accessibility_id": "textview_version",
        "ios_xpath": "//XCUIElementTypeStaticText[@name=\"ApplicationVersionLabel\"]"
    }
    LOCATOR_ENVIRONMENT = {
        "android_xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                         ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                         ".RelativeLayout/android.widget.RelativeLayout["
                         "4]/android.widget.LinearLayout/android.widget.TextView[3] ",
        "android_accessibility_id": "textview_configuration",
        "ios_accessibility_id": "textview_configuration",
        "ios_xpath": "//XCUIElementTypeButton[@name=\"environment_button\"]"
    }
    LOCATOR_CONNECTION = {
        "android_xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                         ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                         ".RelativeLayout/android.widget.RelativeLayout["
                         "4]/android.widget.LinearLayout/android.widget.TextView[5] ",
        "android_accessibility_id": "textview_is_connected",
        "ios_accessibility_id": "textview_is_connected",
        "ios_xpath": "//XCUIElementTypeButton[@name=\"connected_experience_button\"]"
    }
    LOCATOR_ENVIRONMENT_REG2 = {
        "android_xpath": "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget." \
                               "ListView/android.widget.LinearLayout[3]/android.widget.LinearLayout",
        "ios_accessibility_id": "REG2",
        "ios_xpath": "//XCUIElementTypeSheet[@name=\"Runtime Environment\"]/XCUIElementTypeOther/"
                     "XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeScrollView[2]/"
                     "XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther[7]"
    }
    LOCATOR_ALLOW_NOTIFICATIONS_OK_BUTTON = {
        "ios_xpath": "//XCUIElementTypeButton[@name=\"OK\"]"
    }


class SplashPgHelper(BasePage):

    # Click actions
    def click_on_the_shop_now_button(self):
        return self.find_element(GateLocators.LOCATOR_SHOP_NOW).click()

    def click_on_the_get_connected_button(self):
        return self.find_element(GateLocators.LOCATOR_GET_CONNECTED).click()

    def click_on_the_sign_in_button(self):
        return self.find_element(GateLocators.LOCATOR_SIGN_IN).click()

    def click_on_the_sign_up_button(self):
        return self.find_element(GateLocators.LOCATOR_SIGN_UP).click()

    def click_on_the_environment_link(self):
        return self.find_element(GateLocators.LOCATOR_ENVIRONMENT).click()

    def switch_environment_to_reg2(self):
        return self.find_element(GateLocators.LOCATOR_ENVIRONMENT_REG2).click()

    def click_allow_notifications_ok_button(self):
        return self.find_element(GateLocators.LOCATOR_ALLOW_NOTIFICATIONS_OK_BUTTON).click()

    # Is Enabled actions
    def check_if_the_shop_now_button_enabled(self):
        return self.find_element(GateLocators.LOCATOR_SHOP_NOW).is_enabled()

    def check_if_the_get_connected_button_enabled(self):
        return self.find_element(GateLocators.LOCATOR_GET_CONNECTED).is_enabled()

    def check_if_the_sign_in_link_enabled(self):
        return self.find_element(GateLocators.LOCATOR_SIGN_IN).is_enabled()

    def check_if_the_sign_up_link_enabled(self):
        return self.find_element(GateLocators.LOCATOR_SIGN_UP).is_enabled()

    # Get text action
    def get_sign_in_link_text(self):
        return self.find_element(GateLocators.LOCATOR_SIGN_IN).text

    def get_sign_up_link_text(self):
        return self.find_element(GateLocators.LOCATOR_SIGN_UP).text

    def get_get_connected_button_text(self):
        return self.find_element(GateLocators.LOCATOR_GET_CONNECTED).text

    def get_shop_now_button_text(self):
        return self.find_element(GateLocators.LOCATOR_SHOP_NOW).text

    def get_version_text(self):
        return self.find_element(GateLocators.LOCATOR_VERSION).text

    def get_environment_text(self):
        return self.find_element(GateLocators.LOCATOR_ENVIRONMENT).text

    def get_connection_text(self):
        return self.find_element(GateLocators.LOCATOR_CONNECTION).text
