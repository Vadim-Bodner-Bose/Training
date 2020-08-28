from Lib.MobileAppiumService.page_objects.base_app import BasePage


class IdentifyYourBrewerLocators:
    LOCATOR_USING_YOUR_LOCATION_OK = {
        "android_id": "com.keurig.kconnectent:id/ok_button",
        "android_accessibility_id": "button_location_permission_ok",
        "ios_accessibility_id": "button_location_permission_ok"
    }
    LOCATOR_CANT_FIND_QR_CODE = {
        "android_xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget."
                         "FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget."
                         "RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android."
                         "widget.RelativeLayout[2]/android.widget.Button[1]",
        "android_id": "com.keurig.kconnect:id/button_cannot_find_qr",
        "android_accessibility_id": "button_cant_find_qr_code",
        "ios_accessibility_id": "button_cant_find_qr_code",
        "ios_xpath": "//XCUIElementTypeStaticText[@name=\"Can't find QR code?\"]"
    }

    LOCATOR_CONNECT_MANUALLY = {
        "android_xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget."
                         "FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget."
                         "RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android."
                         "widget.RelativeLayout[2]/android.widget.Button[2]",
        "android_id": "com.keurig.kconnect:id/button_add_manually",
        "android_accessibility_id": "button_connect_manually",
        "ios_accessibility_id": "button_connect_manually",
        "ios_xpath": "//XCUIElementTypeStaticText[@name=\"Connect Manually\"]"
    }


class IdentifyYourBrewerPgHelper(BasePage):

    # Click actions
    def click_using_your_location_ok_button(self):
        return self.find_element(IdentifyYourBrewerLocators.LOCATOR_USING_YOUR_LOCATION_OK).click()

    def click_connect_manually_link(self):
        return self.find_element(IdentifyYourBrewerLocators.LOCATOR_CONNECT_MANUALLY).click()

    # Check element visible
    def check_if_using_your_location_ok_visible(self):
        element = self.find_element(IdentifyYourBrewerLocators.LOCATOR_USING_YOUR_LOCATION_OK, 10)
        if element is not None:
            return element.is_displayed()
        else:
            return False
