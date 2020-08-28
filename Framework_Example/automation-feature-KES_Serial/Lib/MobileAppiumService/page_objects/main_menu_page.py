from Lib.MobileAppiumService.page_objects.base_app import BasePage


class MainMenuLocators:
    # TODO: Create mechanism to handle index of tabs on the page so to use appropriate index for appropriate page view
    LOCATOR_SIGN_IN_BUTTON = {
        "android_xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget."
                         "FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget."
                         "LinearLayout/android.view.ViewGroup/android.widget.Button",
        "android_accessibility_id": "button_sign_in_from_shop",
        "ios_accessibility_id": "button_sign_in_from_shop"
    }
    LOCATOR_PRODUCT_SEARCH_TEXT_FIELD = {
        "android_id": "com.keurig.kconnectent:id/edit_text_product_search"
    }
    LOCATOR_CART_BUTTON = {
        "android_id": "com.keurig.kconnectent:id/cart_root",
        "ios_accessibility_id": "ic shopping cart"
    }
    LOCATOR_BREW_TAB = {
        "android_xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget."
                         "FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget."
                         "LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/androidx."
                         "appcompat.app.ActionBar.Tab[1]",
        "android_accessibility_id": "tab_main_brew",
        "ios_accessibility_id": "tab_main_brew",
        "ios_xpath": "//XCUIElementTypeButton[@name=\"Brew\"]",
    }
    LOCATOR_BREW_TAB_TEXT = {
        "android_xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget."
                         "FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget."
                         "LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/androidx."
                         "appcompat.app.ActionBar.Tab[1]/android.widget.LinearLayout/android.widget.LinearLayout"
                         "/android.widget.TextView"
    }
    LOCATOR_SHOP_TAB = {
        "android_xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                         "/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android."
                         "widget.HorizontalScrollView/android.widget.LinearLayout/androidx.appcompat.app.ActionBar."
                         "Tab[1]",
        "android_accessibility_id": "tab_main_shop",
        "ios_accessibility_id": "tab_main_shop",
        "ios_xpath": "//XCUIElementTypeButton[@name=\"Shop\"]"
    }
    LOCATOR_SHOP_TAB_TEXT = {
        "android_xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget."
                         "FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget."
                         "LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/androidx."
                         "appcompat.app.ActionBar.Tab[1]/android.widget.LinearLayout/android.widget.LinearLayout"
                         "/android.widget.TextView",
        "android_accessibility_id": "textview_title_shop",
        "ios_accessibility_id": "textview_title_shop"
    }
    LOCATOR_ORDERS_TAB = {
        "android_xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget."
                         "FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget."
                         "LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/androidx."
                         "appcompat.app.ActionBar.Tab[2]",
        "android_accessibility_id": "tab_main_orders",
        "ios_accessibility_id": "tab_main_orders",
        "ios_xpath": "//XCUIElementTypeButton[@name=\"Orders\"]"
    }
    LOCATOR_ORDERS_TAB_TEXT = {
        "android_xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget."
                         "FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget."
                         "LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/androidx."
                         "appcompat.app.ActionBar.Tab[2]/android.widget.LinearLayout/android.widget.LinearLayout"
                         "/android.widget.TextView",
        "android_accessibility_id": "textview_title_orders",
        "ios_accessibility_id": "textview_title_orders"
    }
    LOCATOR_SETTINGS_TAB = {
        "android_xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget."
                         "FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget."
                         "LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/androidx."
                         "appcompat.app.ActionBar.Tab[3]",
        "android_accessibility_id": "tab_main_settings",
        "ios_accessibility_id": "tab_main_settings",
        "ios_xpath": "//XCUIElementTypeButton[@name=\"Settings\"]"
    }
    LOCATOR_SETTINGS_TAB_TEXT = {
        "android_xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget."
                         "FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget."
                         "LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/androidx."
                         "appcompat.app.ActionBar.Tab[3]/android.widget.LinearLayout/android.widget.LinearLayout"
                         "/android.widget.TextView",
        "android_accessibility_id": "textview_title_settings",
        "ios_accessibility_id": "textview_title_settings"
    }


class MainMenuPgHelper(BasePage):

    # Click actions
    def click_brew_tab(self):
        return self.find_element(MainMenuLocators.LOCATOR_BREW_TAB).click()

    def click_settings_tab(self):
        return self.find_element(MainMenuLocators.LOCATOR_SETTINGS_TAB).click()

    # Is Enabled actions
    def check_if_shop_tab_enabled(self):
        return self.find_element(MainMenuLocators.LOCATOR_SHOP_TAB).is_enabled()

    def check_if_orders_tab_enabled(self):
        return self.find_element(MainMenuLocators.LOCATOR_ORDERS_TAB).is_enabled()

    def check_if_settings_tab_enabled(self):
        return self.find_element(MainMenuLocators.LOCATOR_SETTINGS_TAB).is_enabled()

    # Is Selected actions
    def is_selected_brew_tab(self):
        return self.find_element(MainMenuLocators.LOCATOR_BREW_TAB).is_selected()

    def is_not_selected_brew_tab(self):
        return not self.find_element(MainMenuLocators.LOCATOR_BREW_TAB).is_selected()

    def is_selected_shop_tab(self):
        return self.find_element(MainMenuLocators.LOCATOR_SHOP_TAB).is_selected()

    def is_not_selected_shop_tab(self):
        return not self.find_element(MainMenuLocators.LOCATOR_SHOP_TAB).is_selected()

    def is_selected_orders_tab(self):
        return self.find_element(MainMenuLocators.LOCATOR_ORDERS_TAB).is_selected()

    def is_not_selected_orders_tab(self):
        return not self.find_element(MainMenuLocators.LOCATOR_ORDERS_TAB).is_selected()

    def is_selected_settings_tab(self):
        return self.find_element(MainMenuLocators.LOCATOR_SETTINGS_TAB).is_selected()

    def is_not_selected_settings_tab(self):
        return not self.find_element(MainMenuLocators.LOCATOR_SETTINGS_TAB).is_selected()

    # Is element visible
    def check_if_sign_in_button_shown(self):
        element = self.find_element(MainMenuLocators.LOCATOR_SIGN_IN_BUTTON)
        if element is not None:
            return element.is_displayed()
        else:
            return False

    # Get text action
    def get_shop_tab_text(self):
        return self.find_element(MainMenuLocators.LOCATOR_SHOP_TAB_TEXT).text

    def get_orders_tab_text(self):
        return self.find_element(MainMenuLocators.LOCATOR_ORDERS_TAB_TEXT).text

    def get_settings_tab_text(self):
        return self.find_element(MainMenuLocators.LOCATOR_SETTINGS_TAB_TEXT).text
