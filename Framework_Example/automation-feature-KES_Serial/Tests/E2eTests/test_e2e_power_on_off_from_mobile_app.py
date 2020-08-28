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
import logging

import pytest

from Config.MobileApp_Config import MOBILE_VERSION, E2E_USER_DEFAULT_LOGIN, \
    E2E_USER_DEFAULT_PASSWORD
from Lib.AYLA.AylaAPIcaller import EventTypes
import Lib.GLOBALS.CLI_COMMANDS as CLI
from Lib.GLOBALS.CLI_RESPONSES import PRE_BE_STATE_STANDBY, PRE_BE_STATE_IDLE
from Lib.GLOBALS.CLOUD_EVENTS import AYLA_STATE_MODE_REQ_IDLE, AYLA_STATUS_IDLE, AYLA_SOURCE, \
    AYLA_STATE_MODE_REQ_STANDBY, AYLA_STATUS_STANDBY
from Lib.MobileAppiumService.page_objects.brew_page import BrewPgHelper
from Lib.MobileAppiumService.page_objects.gate_page import SplashPgHelper
from Lib.MobileAppiumService.page_objects.sign_in_page import SignInPgHelper
from Tests.E2eTests import ayla


@pytest.mark.KP_18410
def test_e2e_remote_operations_power_on_off(driver, xray, serial_ar, dsn):
    # STEP 1: Open Splash page, check version, env
    gate_page = SplashPgHelper(driver)
    if gate_page.is_ios():
        gate_page.click_allow_notifications_ok_button()
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
    # TODO: Ayla CLI integration - get brewer DSN and the log it to Xray
    pytest.global_response = pytest.global_response.__add__('\nBrewer DNS: ' + dsn + '\n')

    # STEP 5. Switch to Brew page and Cancel "Few first steps" view
    brew_page = BrewPgHelper(driver)
    logging.warning("------------Switch to BREW page------------")
    brew_page.click_brew_tab()
    brew_page.cancel_few_first_steps()

    # TODO: check if brewer is ready for the test - Greeting text is on the screen (e.g. "Good Afternoon {username}!")

    # Step 6. Check that Power is OFF
    # TODO: Arenal CLI integration - Check brewer state is STANDBY
    assert not serial_ar.send_receive_data(CLI.POWER_OFF,PRE_BE_STATE_STANDBY, 30)
    xray.post_screenshot(pytest.test_case_key, brew_page.get_screenshot())

    assert brew_page.check_if_power_off()

    # STEP 7. Switch Power to ON and check its changed
    brew_page.switch_power()
    xray.post_screenshot(pytest.test_case_key, brew_page.get_screenshot())

    # TODO: Arenal CLI integration - Check brewer state is IDLE
    assert serial_ar.read_data(PRE_BE_STATE_IDLE, 10)

    # TODO: Ayla integration - new req datpoint was created with "cmd":"IDLE"
    req = ayla.get_device_event(dsn, EventTypes.REQ)
    assert req.isCmdEqual(AYLA_STATUS_IDLE)
    assert req.isSourceEqual(AYLA_SOURCE)

    # TODO: Ayla integration - new state datapoint was created with
    # "current":"IDLE","change_cause":"REMOTE_IDLE_REQUEST","req_source":"MOBILE-APP"
    state = ayla.get_device_event(dsn, EventTypes.STATE)
    assert state.isModeEqual(AYLA_STATE_MODE_REQ_IDLE, req.id)

    assert brew_page.check_if_power_on()

    # STEP 8. Switch Power to OFF and check its changed
    brew_page.switch_power()
    xray.post_screenshot(pytest.test_case_key, brew_page.get_screenshot())

    # TODO: Arenal CLI integration - Check brewer state is STANDBY
    # has to execute right after or even before presing the button, might require a thread.
    assert serial_ar.read_data(PRE_BE_STATE_STANDBY, 10)

    # TODO: Ayla integration - new req datpoint was created with "cmd":"STANDBY"
    req = ayla.get_device_event(dsn, EventTypes.REQ)
    assert req.isCmdEqual(AYLA_STATUS_STANDBY)
    assert req.isSourceEqual(AYLA_SOURCE)

    # TODO: Ayla integration - new state datapoint was created with
    # "current":"STANDBY","change_cause":"REMOTE_STANDBY_REQUEST","req_source":"MOBILE-APP"
    state = ayla.get_device_event(dsn, EventTypes.STATE)
    assert state.isModeEqual(AYLA_STATE_MODE_REQ_STANDBY, req.id)

    assert brew_page.check_if_power_off()
