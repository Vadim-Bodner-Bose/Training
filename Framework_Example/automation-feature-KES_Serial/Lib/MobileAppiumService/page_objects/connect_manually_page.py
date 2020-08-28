from Lib.MobileAppiumService.page_objects.base_app import BasePage


class ConnectManuallyLocators:
    LOCATOR_ALREADY_USED_MY_COFFEE_MAKER = {
        "android_xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android."
                         "widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
                         "android.widget.RelativeLayout/android.widget.FrameLayout/android.widget."
                         "RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/"
                         "android.widget.LinearLayout/android.widget.RelativeLayout[1]/android."
                         "widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.TextView",
        "android_accessibility_id": "listviewitem_already_used_coffee_maker_for_new_device",
        "ios_accessibility_id": "listviewitem_already_used_coffee_maker_for_new_device",
        "ios_xpath": "//XCUIElementTypeStaticText[@name=\"I've already used my coffee maker\"]"
    }
    LOCATOR_ALREADY_USED_MY_COFFEE_MAKER_FOLLOW_TEXT_INSTRUCTIONS = {
        "android_xpath": "/hierarchy/android.widget.FrameLayout/android.widget."
                         "LinearLayout/android.widget.FrameLayout/android.widget."
                         "LinearLayout/android.widget.FrameLayout/android.widget."
                         "RelativeLayout/android.widget.FrameLayout/android.widget."
                         "RelativeLayout/android.widget.ScrollView/android.widget."
                         "LinearLayout/android.widget.LinearLayout/android.widget"
                         ".RelativeLayout[1]/android.widget.LinearLayout[2]/android."
                         "widget.LinearLayout/android.widget.Button[1]",
        "android_accessibility_id": "button_follow_text_instructions",
        "ios_accessibility_id": "button_follow_text_instructions",
        "ios_xpath": "//XCUIElementTypeStaticText[@name=\"Follow text instructions\"] "
    }
    LOCATOR_BRAND_NEW_COFFEE_MAKER = {
        "android_xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android."
                         "widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
                         "android.widget.RelativeLayout/android.widget.FrameLayout/android.widget."
                         "RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android."
                         "widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget."
                         "LinearLayout/android.widget.RelativeLayout/android.widget.TextView",
        "android_accessibility_id": "listviewitem_brand_new_coffee_maker_for_new_device",
        "ios_accessibility_id": "listviewitem_brand_new_coffee_maker_for_new_device",
        "ios_xpath": "//XCUIElementTypeStaticText[@name=\"I have a brand new coffee maker\"]"
    }


class ConnectManuallyPgHelper(BasePage):

    # Click actions
    def click_already_have_coffee_maker(self):
        return self.find_element(ConnectManuallyLocators.LOCATOR_ALREADY_USED_MY_COFFEE_MAKER).click()

    def click_already_have_coffee_maker_follow_instructions(self):
        return self.\
            find_element(ConnectManuallyLocators.LOCATOR_ALREADY_USED_MY_COFFEE_MAKER_FOLLOW_TEXT_INSTRUCTIONS).click()
