# KP-18274 Android | Happy path, first time connection:
# Connect Brewer Manually >>there is no visible nets >> I've brewed on my Premium brewer (text)
import logging

import pytest
import time

from Config.MobileApp_Config import MOBILE_VERSION, MOBILE_ENVIRONMENT, WIFI_NETWORK
from Lib.GLOBALS.CLI_RESPONSES import AL_ACK, AL_CONFIGURATION_SAVED, AL_WIFI_PROFILE
from Lib.GLOBALS.CLOUD_EVENTS import AYLA_DEVICE_ON, AYLA_DEVICE_OFF
from Lib.GLOBALS.MOBILE_APP_TEXT_ATTRIBUTES import FIRST_NAME, LAST_NAME, EMAIL_PLACEHOLDER, PWD_PLACEHOLDER
from Lib.MobileAppiumService.page_objects.connect_manually_page import ConnectManuallyPgHelper
from Lib.MobileAppiumService.page_objects.gate_page import SplashPgHelper
from Lib.MobileAppiumService.page_objects.identify_your_brewer_page import IdentifyYourBrewerPgHelper
from Lib.MobileAppiumService.page_objects.lets_get_connected_page import LetsGetConnectedPgHelper
from Lib.MobileAppiumService.page_objects.settings_page import SettingsPgHelper
from Lib.GLOBALS import CLI_COMMANDS as CLI
from Lib.MobileAppiumService.page_objects.sign_up_page import SignUpPgHelper
from Tests.E2eTests import ayla
from Utils.DateTime import DateTime as Time
from Utils.ReplacePlaceHolder import TestingUtils


@pytest.mark.KP_18274
def test_e2e_happy_path_first_time_connection(driver, xray, dsn, serial_con, wifi_network):
    # STEP 0: Check brewer status is Offline
    assert ayla.get_device_status(dsn) == AYLA_DEVICE_OFF

    # STEP 1: Open Splash page, check version, env
    gate_page = SplashPgHelper(driver)

    if gate_page.is_ios():
        gate_page.click_allow_notifications_ok_button()
    gate_page.check_if_the_sign_up_link_enabled()
    assert gate_page.get_version_text() == MOBILE_VERSION

    pytest.global_response = pytest.global_response.__add__('\nBuild: ' + MOBILE_VERSION + '\n')

    # STEP 2. Go to Sign Up page
    gate_page.click_on_the_sign_up_button()

    # STEP 3. Populate Sign Up page with appropriate credentials and sign up
    signup_page = SignUpPgHelper(driver)
    signup_page.enter_first_name(FIRST_NAME)
    signup_page.enter_last_name(LAST_NAME)
    user_login = TestingUtils.replacePlaceholder(EMAIL_PLACEHOLDER)
    signup_page.enter_email_address(user_login)
    if signup_page.is_ios():
        signup_page.swipe_down()
    signup_page.enter_password(TestingUtils.replacePlaceholder(PWD_PLACEHOLDER))
    signup_page.click_on_the_create_an_account_button()

    pytest.global_response = pytest.global_response.__add__('\nUser: ' + user_login + '\n')

    # STEP 4. Switch to Settings page
    settings_page = SettingsPgHelper(driver)
    if settings_page.is_ios():
        settings_page.click_settings_tab()  # This action remove question asking to save new password
        Time.explicit_wait()
    settings_page.click_settings_tab()

    # STEP 5. Click Connect Your Brewer
    settings_page.click_connect_your_brewer_tab()

    xray.post_screenshot(pytest.test_case_key, settings_page.get_screenshot())

    # TODO: Connectivity CLI integration - list of profiles should be empty, remove all profiles if not empty
    pytest.global_response = pytest.global_response.__add__(
        '\nShow Wi-Fi Configuration and Remove Current Profiles:' + '\n')
    assert not serial_con.send_receive_data(CLI.AL_CURRENT_WIFI_STATUS, "0            {}".format(WIFI_NETWORK), 40)

    # TODO: Connectivity CLI integration - Force brewer to set AP mode

    # log to xray, that brewer is set to AP mode
    pytest.global_response = pytest.global_response.__add__('\nAP Mode Enable: ' + '\n')
    serial_con.send_receive_data(CLI.AL_TURN_OFF_WIFI, AL_ACK)
    time.sleep(1)
    serial_con.send_receive_data((CLI.AL_SET_ACTIVE_PROFILE_0, AL_ACK))
    time.sleep(1)
    serial_con.send_receive_data((CLI.AL_ERASE_ACTIVE_PROFILE, AL_ACK))
    time.sleep(1)
    serial_con.send_receive_data((CLI.AL_SAVE_CONFIGURATION, AL_CONFIGURATION_SAVED))
    time.sleep(20)
    serial_con.send_receive_data((CLI.AL_ENABLE_ACTIVE_PROFILE, AL_ACK))
    time.sleep(1)
    serial_con.send_receive_data((CLI.AL_TURN_ON_WIFI, AL_ACK))
    time.sleep(1)
    serial_con.send_receive_data((CLI.AL_SAVE_CONFIGURATION, AL_CONFIGURATION_SAVED))
    time.sleep(15)
    # STEP 6. Click Begin for Lets Get Connected page
    lets_get_connected_page = LetsGetConnectedPgHelper(driver)
    logging.warning("------------Click Lets get connected - begin button------------")
    lets_get_connected_page.click_begin_button()
    xray.post_screenshot(pytest.test_case_key, lets_get_connected_page.get_screenshot())

    # STEP 7. Confirm you agree that Keurig using your location
    identify_your_brewer_page = IdentifyYourBrewerPgHelper(driver)
    logging.warning("------------Identify Location (Optional step)------------")
    if identify_your_brewer_page.check_if_using_your_location_ok_visible():
        identify_your_brewer_page.click_using_your_location_ok_button()
    xray.post_screenshot(pytest.test_case_key, identify_your_brewer_page.get_screenshot())

    # STEP 8. Choose to Connect manually
    # ATTENTION: DO NOT MOVE MOBILE PHONE. The page opened contains QR code scanner and it's trying to focus and scan,
    # so not action could be done before scanner is focused on something!!!
    logging.warning("------------Click-connect manually------------")
    identify_your_brewer_page.click_connect_manually_link()
    xray.post_screenshot(pytest.test_case_key, identify_your_brewer_page.get_screenshot())

    # STEP 9. Choose you already have coffee maker and follow instructions
    connect_manually = ConnectManuallyPgHelper(driver)
    xray.post_screenshot(pytest.test_case_key, identify_your_brewer_page.get_screenshot())
    logging.warning("------------Click-already_use-brewer------------")
    connect_manually.click_already_have_coffee_maker()
    xray.post_screenshot(pytest.test_case_key, connect_manually.get_screenshot())

    logging.warning("------------Click-follow instructions------------")
    connect_manually.click_already_have_coffee_maker_follow_instructions()
    xray.post_screenshot(pytest.test_case_key, connect_manually.get_screenshot())

    # STEP 9: Check the brewer status is Online
    assert ayla.get_device_status(dsn) == AYLA_DEVICE_ON

    # TODO: Tap Link button
    # TODO: Wait for Connect Brewer To Network screen
    # TODO: Submit credentials for Wi-Fi network, take screenshot before submission
    # TODO: Wait for Success screen

    # TODO: Connectivity CLI integration - Check there is only one Wi-Fi profile exists

    assert serial_con.send_receive_data(CLI.AL_CURRENT_WIFI_STATUS, AL_WIFI_PROFILE.format(wifi_network), 40)

    # TODO: Connectivity CLI integration - save logs to file
    # TODO: Ayla integration - Check that brewer status has changed to ONLINE - DONE
    # TODO: Mobile app log - Setup Appliance logs are saved to file
