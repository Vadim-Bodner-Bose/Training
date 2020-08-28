from Lib.MobileAppiumService.page_objects.base_app import BasePage


class LetsGetConnectedLocators:
    LOCATOR_BEGIN_BUTTON = {
        "android_id": "com.keurig.kconnect:id/start_setup_button",
        "android_xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android."
                         "widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout"
                         "/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget."
                         "Button[2]",
        "ios_xpath": "//XCUIElementTypeButton[@name=\"BEGIN\"]",
        "android_accessibility_id": "button_begin",
        "ios_accessibility_id": "button_begin"
    }


class LetsGetConnectedPgHelper(BasePage):

    # Click actions
    def click_begin_button(self):
        return self.find_element(LetsGetConnectedLocators.LOCATOR_BEGIN_BUTTON).click()
