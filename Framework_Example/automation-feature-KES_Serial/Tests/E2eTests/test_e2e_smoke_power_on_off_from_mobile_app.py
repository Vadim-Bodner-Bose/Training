# KP-18410 E2E | Remote Operations | Power On/Off from the mobile app
# PRECONDITIONS
#     There is a mobile device with Keurig app installed
#     Keurig account is logged in the mobile app
#     There is a brewer that linked to the Keurig account
#     Brewer is in Stand By
# STEPS
#     1. Start the mobile app and select the Brew tab -> Power toggle is in Powered Off state
#     2. Tap the Power toggle on the mobile app -> Brewer changes state to Idle.
#     3. Observe mobile app -> Power toggle is in Powered On state
#     4. Tap the Power toggle on the mobile app -> Brewer changes state to Stand By
#     5. Observe mobile app -> Power toggle is in Powered Off state

import pytest
from Config.MobileApp_Config import MOBILE_VERSION, E2E_USER_DEFAULT_LOGIN, \
    E2E_USER_DEFAULT_PASSWORD
from Lib.GLOBALS.CLOUD_EVENTS import AYLA_SOURCE, AYLA_STATUS_IDLE, AYLA_STATUS_STANDBY, AYLA_STATE_MODE_REQ_IDLE, \
    AYLA_STATE_MODE_REQ_STANDBY, AYLA_DEVICE_ON
from Lib.GLOBALS.CLI_RESPONSES import PRE_BE_STATE_STANDBY, PRE_BE_STATE_IDLE
import Lib.GLOBALS.CLI_COMMANDS as CLI
from Lib.AYLA.AylaAPIcaller import EventTypes
from Lib.MobileAppiumService.page_objects.brew_page import BrewPgHelper
from Lib.MobileAppiumService.page_objects.gate_page import SplashPgHelper
from Lib.MobileAppiumService.page_objects.settings_page import SettingsPgHelper
from Lib.MobileAppiumService.page_objects.sign_in_page import SignInPgHelper
from Tests.E2eTests import ayla

# python -m pytest test_e2e_smoke_power_on_off_from_mobile_app.py --testscope e2e_smoke_TM --platform Android \
# --dsn AC000W006144063 --connectivity_port COM15 --connectivity_baud 115200 --arenal_port COM16 --arenal_baud 9600 \
# --wifi_network KDP-Guest --wifi_password drinkwelldogood

@pytest.mark.TM_1692
def test_e2e_smoke_power_on_off(driver, xray, dsn, mobile_environment, serial_ar):
    assert ayla.get_device_status(dsn) == AYLA_DEVICE_ON

    # STEP 1: Open Splash page, check version, env
    gate_page = SplashPgHelper(driver)
    gate_page.check_if_the_sign_in_link_enabled()

    assert gate_page.get_version_text() == MOBILE_VERSION

    pytest.global_response = pytest.global_response.__add__('\nBuild: ' + MOBILE_VERSION + '\n')

    # STEP 3. Go to SIgn In page
    gate_page.click_on_the_sign_in_button()

    # STEP 4. Populate Sign In page with appropriate credentials and sign in
    sign_in_page = SignInPgHelper(driver)
    sign_in_page.enter_email(E2E_USER_DEFAULT_LOGIN)
    sign_in_page.enter_password(E2E_USER_DEFAULT_PASSWORD)
    sign_in_page.click_on_the_sign_in_button()

    pytest.global_response = pytest.global_response.__add__('\nUser: ' + E2E_USER_DEFAULT_LOGIN + '\n')
    pytest.global_response = pytest.global_response.__add__('\nBrewer DSN: ' + dsn + '\n')

    # STEP 5. Switch to Brew page and Cancel "Few first steps" view
    brew_page = BrewPgHelper(driver)
    brew_page.cancel_few_first_steps()

    # Step 6. Check that Power is OFF
    assert not serial_ar.send_receive_data(CLI.POWER_OFF,PRE_BE_STATE_STANDBY, 30)

    xray.post_screenshot(pytest.test_case_key, brew_page.get_screenshot())

    assert brew_page.check_if_power_off()

    # STEP 7. Switch Power to ON and check its changed
    brew_page.switch_power()

    req = ayla.get_device_event(dsn, EventTypes.REQ)
    assert req.isCmdEqual(AYLA_STATUS_IDLE)
    assert req.isSourceEqual(AYLA_SOURCE)

    xray.post_screenshot(pytest.test_case_key, brew_page.get_screenshot())

    assert serial_ar.read_data(PRE_BE_STATE_IDLE, 30)

    state = ayla.get_device_event(dsn, EventTypes.STATE)
    assert state.isModeEqual(AYLA_STATE_MODE_REQ_IDLE, req.id)
    assert brew_page.check_if_power_on()

    # STEP 8. Switch Power to OFF and check its changed
    brew_page.switch_power()

    assert serial_ar.read_data(PRE_BE_STATE_STANDBY, 30)

    req = ayla.get_device_event(dsn, EventTypes.REQ)
    assert req.isCmdEqual(AYLA_STATUS_STANDBY)
    assert req.isSourceEqual(AYLA_SOURCE)

    xray.post_screenshot(pytest.test_case_key, brew_page.get_screenshot())

    state = ayla.get_device_event(dsn, EventTypes.STATE)
    assert state.isModeEqual(AYLA_STATE_MODE_REQ_STANDBY, req.id)
    assert brew_page.check_if_power_off()

    # STEP 9. Log out from user account
    settings_page = SettingsPgHelper(driver)
    settings_page.click_settings_tab()
    settings_page.click_log_out_tab()
    settings_page.click_ok_to_confirm_log_out()
