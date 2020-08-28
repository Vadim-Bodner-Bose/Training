# KP-18483 E2E | Hot Water | Subsequent water brews can be performed without PM cycle
import pytest

from Config.MobileApp_Config import MOBILE_VERSION, E2E_USER_DEFAULT_LOGIN, \
    E2E_USER_DEFAULT_PASSWORD
from Lib.AYLA.AylaAPIcaller import EventTypes
from Lib.GLOBALS.CLI_RESPONSES import PRE_BREWING
from Lib.GLOBALS.CLOUD_EVENTS import AYLA_STATUS_BREW, AYLA_SOURCE, AYLA_REQ_RECIPE, AYLA_STATE_MODE_BREW, \
    AYLA_STATUS_SUCCESSFUL, AYLA_STATE_MODE_BREW_IDLE
from Lib.GLOBALS.MOBILE_APP_TEXT_ATTRIBUTES import HOT_WATER_LABEL, CANCEL_HOT_WATER_LABEL, CANCEL_BREW_LABEL
from Lib.MobileAppiumService.page_objects.brew_page import BrewPgHelper
from Lib.MobileAppiumService.page_objects.gate_page import SplashPgHelper
from Lib.MobileAppiumService.page_objects.sign_in_page import SignInPgHelper
from Tests.E2eTests import ayla


@pytest.mark.KP_18483
def test_e2e_subsequent_water_brews_wo_pm_cycle(driver, xray, serial_ar, dsn, mobile_environment):
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
    # TODO: Ayla integration - get brewer DSN and the log it to Xray
    pytest.global_response = pytest.global_response.__add__('\nBrewer DNS: ' + dsn + '\n')

    # STEP 5. Switch to Brew page and Cancel "Few first steps" view
    brew_page = BrewPgHelper(driver)
    brew_page.click_brew_tab()
    brew_page.cancel_few_first_steps()

    brew_page.click_8oz_button()

    for _ in range(3):
        # STEP 6. Check if Hot Water is shown
        xray.post_screenshot(pytest.test_case_key, brew_page.get_screenshot())

        assert brew_page.get_hot_water_lable_text() == HOT_WATER_LABEL

        # STEP 7. Start brewing
        brew_page.click_start_brewing()

        xray.post_screenshot(pytest.test_case_key, brew_page.get_screenshot())

        # STEP 8 Optional. Confirm mug is settled
        if brew_page.check_if_continue_brew_shown():
            brew_page.click_check_your_mug_continue_brew()

        xray.post_screenshot(pytest.test_case_key, brew_page.get_screenshot())

        # TODO: Arenal CLI integration - Check parameters of the brew corresponds to hot water recipe
        # run immediately after brew is initiated - before the ayla.
        assert serial_ar.read_data(PRE_BREWING, 40)

        # TODO: Ayla integration - new req datpoint was created with
        req = ayla.get_device_event(dsn, EventTypes.REQ)

        assert req.isCmdEqual(AYLA_STATUS_BREW)
        assert req.isRecipeEqual(AYLA_REQ_RECIPE)
        assert req.isSourceEqual(AYLA_SOURCE)

        # TODO: Ayla integration - new state datpoint was created with
        state = ayla.get_device_event(dsn, EventTypes.STATE)

        assert state.isRecipeEqual(AYLA_REQ_RECIPE)
        assert state.isModeEqual(AYLA_STATE_MODE_BREW, req.id)

        # STEP 9. Check that text of Brew button is changed to "Tap to cancel hot water"
        if brew_page.check_if_tap_to_cancel_hot_water_button_shown():
            button_text = brew_page.get_tap_to_cancel_hot_water_button_text()

            if button_text == CANCEL_HOT_WATER_LABEL:
                pass
            else:
                assert button_text == CANCEL_BREW_LABEL

        # STEP 10. Check Ayla that status is changed

        xray.post_screenshot(pytest.test_case_key, brew_page.get_screenshot())

        # TODO: Ayla integration - new state datpoint was created with
        state = ayla.get_device_event(dsn, EventTypes.STATE)

        assert state.isBrewingStatusEqual(AYLA_STATUS_SUCCESSFUL)
        assert state.isModeEqual(AYLA_STATE_MODE_BREW_IDLE, req.id)

        # TODO: all three datapoints above should contain the same "req_id". It ties the request to state changes and
        #  confirms we are comparing apples to apples - Done

        # STEP 11. Wait until brewing ends and check that main button became with Keurig logo
        assert brew_page.check_if_keurig_brew_button_shown()
