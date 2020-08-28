from Lib.MobileAppiumService.page_objects.base_app import BasePage


class SignUpLocators:
    LOCATOR_FIRST_NAME = {
        "android_accessibility_id": "textview_first_name",
        "ios_accessibility_id": "textview_first_name",
        "android_xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                         ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                         ".RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget"
                         ".ScrollView/android.widget.LinearLayout/android.widget.LinearLayout["
                         "1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                         "/android.widget.EditText ",
        "ios_xpath": "//XCUIElementTypeApplication[@name=\"Keurig\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther"
                     "/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/"
                     "XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/"
                     "XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[2]/"
                     "XCUIElementTypeOther[1]/XCUIElementTypeTextField"
    }
    LOCATOR_FIRST_NAME_TEXT = {
        "android_xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget."
                         "FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget."
                         "RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget."
                         "ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget."
                         "LinearLayout/android.widget.TextView"
    }
    LOCATOR_LAST_NAME = {
        "android_accessibility_id": "textview_last_name",
        "ios_accessibility_id": "textview_last_name",
        "android_xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                         "/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout"
                         "/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android"
                         ".widget.LinearLayout/android.widget.LinearLayout["
                         "2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                         "/android.widget.EditText ",
        "ios_xpath": "//XCUIElementTypeApplication[@name=\"Keurig\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/"
                     "XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/"
                     "XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/"
                     "XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[2]/"
                     "XCUIElementTypeOther[2]/XCUIElementTypeTextField"
    }
    LOCATOR_LAST_NAME_TEXT = {
        "android_xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget."
                         "FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget."
                         "RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget."
                         "ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget."
                         "LinearLayout/android.widget.TextView"
    }
    LOCATOR_EMAIL = {
        "android_accessibility_id": "textview_email",
        "ios_accessibility_id": "textview_email",
        "android_xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                         "/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android"
                         ".widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget"
                         ".LinearLayout/android.widget.LinearLayout["
                         "3]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
                         ".widget.EditText ",
        "ios_xpath": "//XCUIElementTypeApplication[@name=\"Keurig\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/"
                     "XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/"
                     "XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/"
                     "XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[2]/"
                     "XCUIElementTypeOther[3]/XCUIElementTypeTextField"
    }
    LOCATOR_EMAIL_TEXT = {
        "android_xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget."
                         "FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget."
                         "RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget."
                         "ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget."
                         "LinearLayout/android.widget.TextView"
    }
    LOCATOR_PASSWORD = {
        "android_accessibility_id": "textview_password",
        "ios_accessibility_id": "textview_password",
        "android_xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                         "/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android"
                         ".widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget"
                         ".LinearLayout/android.widget.LinearLayout["
                         "4]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
                         ".widget.EditText ",
        "ios_xpath": "//XCUIElementTypeApplication[@name=\"Keurig\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/"
                     "XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/"
                     "XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/"
                     "XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[2]/"
                     "XCUIElementTypeOther[4]/XCUIElementTypeSecureTextField"
    }
    LOCATOR_PASSWORD_TEXT = {
        "android_xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget."
                         "FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget."
                         "RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget."
                         "ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[4]/android.widget."
                         "LinearLayout/android.widget.TextView"
    }
    LOCATOR_OFFER_EMAILS = {
        "android_accessibility_id": "checkbox_offer_emails",
        "ios_accessibility_id": "checkbox_offer_emails",
        "android_id": "com.keurig.kconnectent:id/checkbox_offers",
        "android_xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                         ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                         ".RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget"
                         ".ScrollView/android.widget.LinearLayout/android.widget.CheckBox ",
        "ios_xpath": "//XCUIElementTypeApplication[@name=\"Keurig\"]/XCUIElementTypeWindow[1]/"
                     "XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/"
                     "XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/"
                     "XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/"
                     "XCUIElementTypeOther[2]/XCUIElementTypeOther[5]/XCUIElementTypeOther"
    }
    LOCATOR_CREATE_AN_ACCOUNT = {
        "android_xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                         ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                         ".RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android"
                         ".widget.ScrollView/android.widget.LinearLayout/android.widget.Button[1] ",
        "android_accessibility_id": "button_create_account",
        "ios_accessibility_id": "button_create_account",
        "ios_xpath": "//XCUIElementTypeButton[@name=\"CREATE AN ACCOUNT\"]"
    }
    LOCATOR_SIGN_IN = {
        "android_xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                         "/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android"
                         ".widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget"
                         ".LinearLayout/android.widget.Button[2] ",
        "android_accessibility_id": "button_sign_in",
        "ios_accessibility_id": "button_sign_in",
        "ios_xpath": "//XCUIElementTypeStaticText[@name=\"Sign in\"]"
    }


class SignUpPgHelper(BasePage):

    # Is Enabled actions
    def check_if_the_first_name_field_enabled(self):
        return self.find_element(SignUpLocators.LOCATOR_FIRST_NAME).is_enabled()

    def check_if_the_last_name_field_enabled(self):
        return self.find_element(SignUpLocators.LOCATOR_LAST_NAME).is_enabled()

    def check_if_the_email_field_enabled(self):
        return self.find_element(SignUpLocators.LOCATOR_EMAIL).is_enabled()

    def check_if_the_password_field_enabled(self):
        return self.find_element(SignUpLocators.LOCATOR_PASSWORD).is_enabled()

    def check_if_the_offer_emails_field_enabled(self):
        return self.find_element(SignUpLocators.LOCATOR_OFFER_EMAILS).is_enabled()

    def check_if_the_create_an_account_button_enabled(self):
        return self.find_element(SignUpLocators.LOCATOR_CREATE_AN_ACCOUNT).is_enabled()

    def check_if_the_sign_in_link_enabled(self):
        return self.find_element(SignUpLocators.LOCATOR_SIGN_IN).is_enabled()

    # Is Checked actions
    def check_if_the_offer_emails_checkbox_checked(self):
        return self.find_element(SignUpLocators.LOCATOR_OFFER_EMAILS).get_attribute('checked')

    # Click actions
    def click_on_the_offer_emails_checkbox(self):
        return self.find_element(SignUpLocators.LOCATOR_OFFER_EMAILS).click()

    def click_on_the_create_an_account_button(self):
        return self.find_element(SignUpLocators.LOCATOR_CREATE_AN_ACCOUNT).click()

    # Get text action
    def get_sign_in_link_text(self):
        return self.find_element(SignUpLocators.LOCATOR_SIGN_IN).text

    def get_create_an_account_button_text(self):
        return self.find_element(SignUpLocators.LOCATOR_CREATE_AN_ACCOUNT).text

    def get_first_name_text(self):
        return self.find_element(SignUpLocators.LOCATOR_FIRST_NAME_TEXT).text

    def get_last_name_text(self):
        return self.find_element(SignUpLocators.LOCATOR_LAST_NAME_TEXT).text

    def get_email_text(self):
        return self.find_element(SignUpLocators.LOCATOR_EMAIL_TEXT).text

    def get_password_text(self):
        return self.find_element(SignUpLocators.LOCATOR_PASSWORD_TEXT).text

    # Enter text to text_field
    def enter_first_name(self, word):
        text_field = self.find_element(SignUpLocators.LOCATOR_FIRST_NAME)
        # text_field.click()
        text_field.send_keys(word)
        return text_field

    def enter_last_name(self, word):
        text_field = self.find_element(SignUpLocators.LOCATOR_LAST_NAME)
        # text_field.click()
        text_field.send_keys(word)
        return text_field

    def enter_email_address(self, word):
        text_field = self.find_element(SignUpLocators.LOCATOR_EMAIL)
        # text_field..click()
        text_field.send_keys(word)
        return text_field

    def enter_password(self, word):
        text_field = self.find_element(SignUpLocators.LOCATOR_PASSWORD)
        # text_field..click()
        text_field.send_keys(word)
        return text_field
