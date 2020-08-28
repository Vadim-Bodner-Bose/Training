from Lib.MobileAppiumService.page_objects.main_menu_page import MainMenuPgHelper


class SettingsLocators:
    LOCATOR_CONNECT_YOUR_BREWER_TAB = {
        "android_xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android."
                         "widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
                         "android.widget.LinearLayout/android.widget.FrameLayout/android.widget."
                         "RelativeLayout/android.widget.LinearLayout/androidx.recyclerview.widget."
                         "RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout",
        "android_accessibility_id": "listitem_navigation_Connect_Your_Brewer",
        "ios_accessibility_id": "listitem_navigation_Connect_Your_Brewer",
        "ios_xpath": "//XCUIElementTypeStaticText[@name=\"Connect Your Brewer\"]"
    }
    LOCATOR_CONNECT_YOUR_BREWER_TAB_TEXT = {
        "android_xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget."
                         "FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget."
                         "LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget."
                         "LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/"
                         "android.widget.LinearLayout/android.widget.TextView"
    }
    LOCATOR_FAVORITES_TAB = {
        "android_xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android."
                         "widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
                         "android.widget.LinearLayout/android.widget.FrameLayout/android.widget."
                         "RelativeLayout/android.widget.LinearLayout/androidx.recyclerview.widget."
                         "RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout",
        "android_accessibility_id": "listitem_navigation_Favorites",
        "ios_accessibility_id": "listitem_navigation_Favorites",
        "ios_xpath": "//XCUIElementTypeStaticText[@name=\"Favorites\"]"
    }
    LOCATOR_SIGN_IN_TAB = {
        "android_xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android."
                         "widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
                         "android.widget.LinearLayout/android.widget.FrameLayout/android.widget."
                         "RelativeLayout/android.widget.LinearLayout/androidx.recyclerview.widget."
                         "RecyclerView/android.widget.LinearLayout[2]/android.widget.LinearLayout",
        "android_accessibility_id": "listitem_navigation_Sign_in",
        "ios_accessibility_id": "listitem_navigation_Sign_in",
        "ios_xpath": "//XCUIElementTypeStaticText[@name=\"Sign in\"]"
    }
    LOCATOR_SIGN_IN_TAB_TEXT = {
        "android_xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget."
                         "FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget."
                         "LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget."
                         "LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/"
                         "android.widget.LinearLayout/android.widget.TextView"
    }
    LOCATOR_REGISTER_A_BREWER_TAB = {
        "android_xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android."
                         "widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
                         "android.widget.LinearLayout/android.widget.FrameLayout/android.widget."
                         "RelativeLayout/android.widget.LinearLayout/androidx.recyclerview.widget."
                         "RecyclerView/android.widget.LinearLayout[3]/android.widget.LinearLayout",
        "android_accessibility_id": "listitem_navigation_Register_a_Brewer",
        "ios_accessibility_id": "listitem_navigation_Register_a_Brewer",
        "ios_xpath": "//XCUIElementTypeStaticText[@name=\"Register a Brewer\"]"
    }
    LOCATOR_REGISTER_A_BREWER_TAB_TEXT = {
        "android_xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget."
                         "FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget."
                         "LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget."
                         "LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]/"
                         "android.widget.LinearLayout/android.widget.TextView"
    }
    LOCATOR_MY_BREWERS_TAB = {
        "android_xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android."
                         "widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
                         "android.widget.LinearLayout/android.widget.FrameLayout/android.widget."
                         "RelativeLayout/android.widget.LinearLayout/androidx.recyclerview.widget."
                         "RecyclerView/android.widget.LinearLayout[2]/android.widget.LinearLayout",
        "android_accessibility_id": "listitem_navigation_My_Brewers",
        "ios_accessibility_id": "listitem_navigation_My_Brewers",
        "ios_xpath": "//XCUIElementTypeStaticText[@name=\"My Brewers\"]"
    }
    LOCATOR_MY_ACCOUNT_TAB = {
        "android_xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android."
                         "widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
                         "android.widget.LinearLayout/android.widget.FrameLayout/android.widget."
                         "RelativeLayout/android.widget.LinearLayout/androidx.recyclerview.widget."
                         "RecyclerView/android.widget.LinearLayout[3]/android.widget.LinearLayout",
        "android_accessibility_id": "listitem_navigation_My_Account",
        "ios_accessibility_id": "listitem_navigation_My_Account",
        "ios_xpath": "//XCUIElementTypeStaticText[@name=\"My Account\"]"
    }
    LOCATOR_COMMUNICATION_PREFERENCES_TAB = {
        "android_xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
                         "/android.widget.FrameLayout/android.widget.LinearLayout/android"
                         ".widget.FrameLayout/android.widget.LinearLayout/android.widget"
                         ".FrameLayout/android.widget.RelativeLayout/android.widget"
                         ".LinearLayout/androidx.recyclerview.widget.RecyclerView/android"
                         ".widget.LinearLayout[5]/android.widget.LinearLayout ",
        "android_accessibility_id": "listitem_navigation_Communication_Preferences",
        "ios_accessibility_id": "listitem_navigation_Communication_Preferences",
        "ios_xpath": "//XCUIElementTypeStaticText[@name=\"Communication Preferences\"]"
    }
    LOCATOR_VOICE_CONTROL_TAB = {
        "android_xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
                         "/android.widget.FrameLayout/android.widget.LinearLayout/android"
                         ".widget.FrameLayout/android.widget.LinearLayout/android.widget"
                         ".FrameLayout/android.widget.RelativeLayout/android.widget"
                         ".LinearLayout/androidx.recyclerview.widget.RecyclerView/android"
                         ".widget.LinearLayout[4]/android.widget.LinearLayout ",
        "android_accessibility_id": "listitem_navigation_Voice_Control",
        "ios_accessibility_id": "listitem_navigation_Voice_Control",
        "ios_xpath": "//XCUIElementTypeStaticText[@name=\"Voice Control\"]"
    }
    LOCATOR_SUPPORT_TAB = {
        "android_xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android."
                         "widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
                         "android.widget.LinearLayout/android.widget.FrameLayout/android.widget."
                         "RelativeLayout/android.widget.LinearLayout/androidx.recyclerview.widget."
                         "RecyclerView/android.widget.LinearLayout[6]/android.widget.LinearLayout",
        "android_accessibility_id": "listitem_navigation_Support",
        "ios_accessibility_id": "listitem_navigation_Support",
        "ios_xpath": "//XCUIElementTypeStaticText[@name=\"Support\"]"
    }
    LOCATOR_SUPPORT_TAB_TEXT = {
        "android_xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget."
                         "FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget."
                         "LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget."
                         "LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[6]/"
                         "android.widget.LinearLayout/android.widget.TextView"
    }
    LOCATOR_ABOUT_TAB = {
        "android_xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android."
                         "widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
                         "android.widget.LinearLayout/android.widget.FrameLayout/android.widget."
                         "RelativeLayout/android.widget.LinearLayout/androidx.recyclerview.widget."
                         "RecyclerView/android.widget.LinearLayout[7]/android.widget.LinearLayout",
        "android_accessibility_id": "listitem_navigation_About",
        "ios_accessibility_id": "listitem_navigation_About",
        "ios_xpath": "//XCUIElementTypeStaticText[@name=\"About\"]"
    }
    LOCATOR_ABOUT_TAB_TEXT = {
        "android_xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget."
                         "FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget."
                         "LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget."
                         "LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[7]/"
                         "android.widget.LinearLayout/android.widget.TextView"
    }
    LOCATOR_LOG_OUT_TAB = {
        "android_xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android."
                         "widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
                         "android.widget.LinearLayout/android.widget.FrameLayout/android.widget."
                         "RelativeLayout/android.widget.LinearLayout/androidx.recyclerview.widget."
                         "RecyclerView/android.widget.LinearLayout[8]/android.widget.LinearLayout",
        "android_accessibility_id": "listitem_navigation_Log_Out",
        "ios_accessibility_id": "listitem_navigation_Log_Out",
        "ios_xpath": "//XCUIElementTypeStaticText[@name=\"Log Out\"]"
    }
    LOCATOR_OK_CONFIRM_LOG_OUT_BUTTON = {
        "android_xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android."
                         "widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/"
                         "androidx.appcompat.widget.LinearLayoutCompat/android.widget.ScrollView/"
                         "android.widget.LinearLayout/android.widget.Button[2]",
        "android_id": "android:id/button1"
    }
    LOCATOR_DECLINE_LOG_OUT_BUTTON = {
        "android_xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android."
                         "widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/"
                         "androidx.appcompat.widget.LinearLayoutCompat/android.widget.ScrollView/"
                         "android.widget.LinearLayout/android.widget.Button[1]",
        "android_id": "android:id/button2"
    }
    LOCATOR_ENVIRONMENT_TAB = {
        "android_xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android."
                         "widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
                         "android.widget.LinearLayout/android.widget.FrameLayout/android.widget."
                         "RelativeLayout/android.widget.LinearLayout/androidx.recyclerview.widget."
                         "RecyclerView/android.widget.LinearLayout[9]/android.widget.LinearLayout",
        "android_accessibility_id": "listitem_navigation_Environment",
        "ios_accessibility_id": "listitem_navigation_Environment",
        "ios_xpath": "//XCUIElementTypeStaticText[@name=\"Environment\"]"
    }
    LOCATOR_FINGERPRINT_ID_TAB = {
        "android_xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android."
                         "widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
                         "android.widget.LinearLayout/android.widget.FrameLayout/android.widget."
                         "RelativeLayout/android.widget.LinearLayout/androidx.recyclerview.widget."
                         "RecyclerView/android.widget.LinearLayout[8]/android.widget.LinearLayout"
    }
    LOCATOR_FACE_ID_TAB = {
        "ios_xpath": "//XCUIElementTypeStaticText[@name=\"Face ID\"]",
        "android_accessibility_id": "listitem_navigation_Face_ID",
        "ios_accessibility_id": "listitem_navigation_Face_ID"
    }
    LOCATOR_TOUCH_ID_TAB = {
        "ios_xpath": "//XCUIElementTypeStaticText[@name=\"Touch ID\"]",
        "android_accessibility_id": "listitem_navigation_Touch_ID",
        "ios_accessibility_id": "listitem_navigation_Touch_ID"
    }


class SettingsPgHelper(MainMenuPgHelper):

    # Click actions
    def click_connect_your_brewer_tab(self):
        return self.find_element(SettingsLocators.LOCATOR_CONNECT_YOUR_BREWER_TAB).click()

    def click_my_account_tab(self):
        return self.find_element(SettingsLocators.LOCATOR_MY_ACCOUNT_TAB).click()

    def click_log_out_tab(self):
        return self.find_element(SettingsLocators.LOCATOR_LOG_OUT_TAB).click()

    def click_ok_to_confirm_log_out(self):
        return self.find_element(SettingsLocators.LOCATOR_OK_CONFIRM_LOG_OUT_BUTTON).click()

    def click_sign_in_tab(self):
        return self.find_element(SettingsLocators.LOCATOR_SIGN_IN_TAB).click()

    # Is Enabled actions
    def check_if_fingerprint_id_enabled(self):
        return self.find_element(SettingsLocators.LOCATOR_FINGERPRINT_ID_TAB).is_enabled()

    def check_if_face_id_enabled(self):
        return self.find_element(SettingsLocators.LOCATOR_FACE_ID_TAB).is_enabled()

    def check_if_touch_id_enabled(self):
        return self.find_element(SettingsLocators.LOCATOR_TOUCH_ID_TAB).is_enabled()

    def check_if_voice_control_enabled(self):
        return self.find_element(SettingsLocators.LOCATOR_VOICE_CONTROL_TAB).is_enabled()

    def check_if_favorites_enabled(self):
        return self.find_element(SettingsLocators.LOCATOR_FAVORITES_TAB).is_enabled()

    def check_if_connect_your_brewer_enabled(self):
        return self.find_element(SettingsLocators.LOCATOR_CONNECT_YOUR_BREWER_TAB).is_enabled()

    def check_if_sign_in_enabled(self):
        element = self.find_element(SettingsLocators.LOCATOR_SIGN_IN_TAB)
        if element is not None:
            return element.is_enabled()
        else:
            return False

    def check_if_my_brewers_enabled(self):
        element = self.find_element(SettingsLocators.LOCATOR_MY_BREWERS_TAB)
        if element is not None:
            return element.is_enabled()
        else:
            return False

    def check_if_my_account_enabled(self):
        element = self.find_element(SettingsLocators.LOCATOR_MY_ACCOUNT_TAB)
        if element is not None:
            return element.is_enabled()
        else:
            return False

    def check_if_communication_preferences_enabled(self):
        return self.find_element(SettingsLocators.LOCATOR_COMMUNICATION_PREFERENCES_TAB).is_enabled()

    def check_if_support_enabled(self):
        return self.find_element(SettingsLocators.LOCATOR_SUPPORT_TAB).is_enabled()

    def check_if_about_enabled(self):
        return self.find_element(SettingsLocators.LOCATOR_ABOUT_TAB).is_enabled()

    def check_if_log_out_enabled(self):
        return self.find_element(SettingsLocators.LOCATOR_LOG_OUT_TAB).is_enabled()

    def check_if_environment_enabled(self):
        return self.find_element(SettingsLocators.LOCATOR_ENVIRONMENT_TAB).is_enabled()

    def check_if_register_a_brewer_enabled(self):
        return self.find_element(SettingsLocators.LOCATOR_REGISTER_A_BREWER_TAB).is_enabled()

    # Get text action
    def get_connect_your_brewer_tab_text(self):
        return self.find_element(SettingsLocators.LOCATOR_CONNECT_YOUR_BREWER_TAB_TEXT).text

    def get_sign_in_tab_text(self):
        return self.find_element(SettingsLocators.LOCATOR_SIGN_IN_TAB_TEXT).text

    def get_register_a_brewer_tab_text(self):
        return self.find_element(SettingsLocators.LOCATOR_REGISTER_A_BREWER_TAB_TEXT).text

    def get_support_tab_text(self):
        return self.find_element(SettingsLocators.LOCATOR_SUPPORT_TAB_TEXT).text

    def get_about_tab_text(self):
        return self.find_element(SettingsLocators.LOCATOR_ABOUT_TAB_TEXT).text
