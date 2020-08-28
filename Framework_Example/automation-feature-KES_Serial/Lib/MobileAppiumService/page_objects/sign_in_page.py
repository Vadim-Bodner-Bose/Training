from Lib.MobileAppiumService.page_objects.base_app import BasePage


class SignInLocators:
    LOCATOR_EMAIL = {
        "android_accessibility_id": "textview_email",
        "ios_accessibility_id": "textview_email",
        "android_xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
                         "android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android."
                         "widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget."
                         "RelativeLayout/android.widget.RelativeLayout[2]/android.widget.LinearLayout["
                         "1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                         "/android.widget.EditText",
        "ios_xpath": "//XCUIElementTypeApplication[@name=\"Keurig\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/"
                     "XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/"
                     "XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/"
                     "XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[2]/"
                     "XCUIElementTypeOther[1]/XCUIElementTypeTextField "
    }
    LOCATOR_PASSWORD = {
        "android_accessibility_id": "textview_password",
        "ios_accessibility_id": "textview_password",
        "android_xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
                         "android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android."
                         "widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget."
                         "RelativeLayout/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget."
                         "LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget."
                         "FrameLayout/android.widget.EditText",
        "ios_xpath": "//XCUIElementTypeApplication[@name=\"Keurig\"]/XCUIElementTypeWindow["
                     "1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther"
                     "/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther"
                     "/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView"
                     "/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeSecureTextField "
    }
    LOCATOR_SIGN_IN_BUTTON = {
        "android_id": "com.keurig.kconnectent:id/button_sign_in",
        "android_accessibility_id": "button_sign_in",
        "ios_accessibility_id": "button_sign_in",
        "ios_xpath": "//XCUIElementTypeButton[@name=\"SIGN IN\"]"
    }
    LOCATOR_FORGOT_PASSWORD_LINK = {
        "android_id": "com.keurig.kconnectent:id/button_forgot_password",
        "android_accessibility_id": "button_forgot_password",
        "ios_accessibility_id": "button_forgot_password",
        "ios_xpath": "//XCUIElementTypeStaticText[@name=\"Forgot password?\"]"
    }
    LOCATOR_CREATE_AN_ACCOUNT_LINK = {
        "android_id": "com.keurig.kconnectent:id/button_create_account",
        "android_accessibility_id": "button_create_account",
        "ios_accessibility_id": "button_create_account",
        "ios_xpath": "//XCUIElementTypeStaticText[@name=\"Create an account\"]"
    }
    LOCATOR_DONT_ALLOW_FINGERPRINT_BUTTON = {
        "android_xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget."
                         "FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat."
                         "widget.LinearLayoutCompat/android.widget.ScrollView/android.widget.LinearLayout/android."
                         "widget.Button[1]",
        "android_id": "android:id/button2"
    }
    LOCATOR_FINGERPRINT_POPUP = {
        "android_xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget."
                         "FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat."
                         "widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.ScrollView/android."
                         "widget.LinearLayout/android.widget.TextView",
        "android_id": "android:id/message"
    }


class SignInPgHelper(BasePage):

    # Click actions
    def click_on_the_sign_in_button(self):
        return self.find_element(SignInLocators.LOCATOR_SIGN_IN_BUTTON).click()

    def click_dont_allow_fingerprint_button(self):
        return self.find_element(SignInLocators.LOCATOR_DONT_ALLOW_FINGERPRINT_BUTTON).click()

    # Enter text to text_field
    def enter_email(self, word):
        text_field = self.find_element(SignInLocators.LOCATOR_EMAIL)
        # text_field.click()
        text_field.send_keys(word)
        return text_field

    def enter_password(self, word):
        text_field = self.find_element(SignInLocators.LOCATOR_PASSWORD)
        # text_field.click()
        text_field.send_keys(word)
        return text_field

    # Check element visible
    def check_if_fingerprint_popup_visible(self):
        element = self.find_element(SignInLocators.LOCATOR_FINGERPRINT_POPUP, 10)
        if element is not None:
            return element.is_displayed()
        else:
            return False
