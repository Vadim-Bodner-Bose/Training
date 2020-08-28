from Lib.MobileAppiumService.page_objects.base_app import BasePage


class ErrorLocators:
    LOCATOR_ERROR_HEADER = {
        "android_id": "com.keurig.kconnectent:id/text_web_error_header"
    }
    LOCATOR_ERROR_MESSAGE = {
        "android_id": "com.keurig.kconnectent:id/text_web_error_message"
    }
    LOCATOR_REFRESH_LINK = {
        "android_id": "com.keurig.kconnectent:id/button_web_error_refresh"
    }

    # ANDROID PERMISSIONS
    LOCATOR_ALLOW_ANDROID_PERMISSION = {
        "android_id": "com.android.permissioncontroller:id/permission_allow_button"
    }


class ErrorPgHelper(BasePage):

    # Click actions
    def refresh_page(self):
        return self.find_element(ErrorLocators.LOCATOR_REFRESH_LINK).click()

    # Get error text
    def get_error_header(self):
        return self.find_element(ErrorLocators.LOCATOR_ERROR_HEADER).text

    def get_error_message(self):
        return self.find_element(ErrorLocators.LOCATOR_ERROR_MESSAGE).text

    # Allow ANDROID permission
    def check_if_android_permission_visible(self):
        element = self.find_element(ErrorLocators.LOCATOR_ALLOW_ANDROID_PERMISSION, 10)
        if element is not None:
            return element.is_displayed()
        else:
            return False

    def allow_android_permission(self):
        return self.find_element(ErrorLocators.LOCATOR_ALLOW_ANDROID_PERMISSION).click
