# KP-16647 E2E | Cancel HOT WATER from IN PROGRESS state from mobile app
import pytest
import time
from Config.MobileApp_Config import MOBILE_VERSION, E2E_USER_DEFAULT_LOGIN, \
    E2E_USER_DEFAULT_PASSWORD
from Lib.AYLA.AylaAPIcaller import EventTypes
from Lib.GLOBALS.CLOUD_EVENTS import AYLA_SOURCE, AYLA_STATE_MODE_BREW, AYLA_STATE_MODE_BREW_IDLE, AYLA_STATUS_BREW, \
    AYLA_STATUS_CANCELLED, AYLA_STATUS_IN_PROGRESS, AYLA_REQ_RECIPE
from Lib.GLOBALS.MOBILE_APP_TEXT_ATTRIBUTES import HOT_WATER_LABEL, CANCEL_HOT_WATER_BUTTON, BREW_CANCELED_LABEL
from Lib.MobileAppiumService.page_objects.brew_page import BrewPgHelper
from Lib.MobileAppiumService.page_objects.gate_page import SplashPgHelper
from Lib.MobileAppiumService.page_objects.sign_in_page import SignInPgHelper
from Tests.E2eTests import ayla

@pytest.mark.unbound
# @pytest.mark.KP_16647
def test_e2e_cancel_hot_water_from_in_progress_state(driver, xray, dsn):
    # STEP 1: Open Splash page, check version, env
    gate_page = SplashPgHelper(driver)
    if gate_page.is_ios():
        gate_page.click_allow_notifications_ok_button()
    gate_page.check_if_the_sign_in_link_enabled()

    assert gate_page.get_version_text() == MOBILE_VERSION

    pytest.global_response = pytest.global_response.__add__('\nBuild: ' + MOBILE_VERSION + '\n')

    # STEP 3. Go to Sign In page
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
    brew_page.cancel_few_first_steps()
    brew_page.click_brew_tab()
    # brew_page.cancel_few_first_steps()

    # STEP 6. Check if Hot Water is shown
    # xray.post_screenshot(pytest.test_case_key, brew_page.get_screenshot())
    assert brew_page.get_hot_water_lable_text() == HOT_WATER_LABEL

    brew_page.click_8oz_button()

    # STEP 7. Start brewing
    brew_page.click_start_brewing()
    # xray.post_screenshot(pytest.test_case_key, brew_page.get_screenshot())

    # STEP 8 Optional. Confirm mug is settled
    if brew_page.check_if_continue_brew_shown():
        brew_page.click_check_your_mug_continue_brew()

    # TODO: Ayla integration - new req datpoint was created with
    # "cmd":"BREW"
    # "recipe":{"size":4,"brew_type":"HOT_WATER","flow_rate":7390,"temp":192,"enhanced":false,"recipe_category":"WATER}
    # "source":"MOBILE-APP"
    time.sleep(5)
    req = ayla.get_device_event(dsn, EventTypes.REQ)
    assert req.isCmdEqual(AYLA_STATUS_BREW)
    assert req.isRecipeEqual(AYLA_REQ_RECIPE)
    assert req.isSourceEqual(AYLA_SOURCE)

    # TODO: Ayla integration - new state datpoint was created with
    # "brewing_status":"BREW_IN_PROGRESS"
    # "recipe":{"size":"4","brew_type":"HOT_WATER","flow_rate":7390,"temp":192,"enhanced":false,"recipe_category":"WATER"}
    # "mode":{"current":"BREW","change_cause":"REMOTE_BREW_REQUEST","req_source":"MOBILE-APP"...}

    state = ayla.get_device_event(dsn, EventTypes.STATE)
    assert state.isBrewingStatusEqual(AYLA_STATUS_IN_PROGRESS)
    assert state.isRecipeEqual(AYLA_REQ_RECIPE)
    assert state.isModeEqual(AYLA_STATE_MODE_BREW, req.id)

    # STEP 9. Check that text of Brew button is changed to "Tap to cancel hot water" and Cancel Brewing
    if brew_page.check_if_tap_to_cancel_brew_button_shown():
        brew_page.click_cancel_brew()
    # xray.post_screenshot(pytest.test_case_key, brew_page.get_screenshot())

    # TODO: Ayla integration - new state datpoint was created with
    # "brewing_status":"BREW_CANCELLING"
    # Temporary unavailable due to existing defect

    assert brew_page.get_tap_to_cancel_hot_water_button_text() == CANCEL_HOT_WATER_BUTTON

    # STEP 10. Check Ayla that status is changing as planned
    # TODO:  Ayla integration - new state datpoint was created with
    #  "state":{"brewing_status":"BREW_CANCELLED"
    #  "current":"IDLE","change_cause":"BREW_COMPLETE_IDLE_REQUEST","req_source":"MOBILE-APP"
    state = ayla.get_device_event(dsn, EventTypes.STATE)
    assert state.isBrewingStatusEqual(AYLA_STATUS_CANCELLED)
    assert state.isModeEqual(AYLA_STATE_MODE_BREW_IDLE, req.id)

    # TODO: all datapoints above should contain the same "req_id". It ties the request to state changes and
    #  confirms we are comparing apples to apples - Done

    # STEP 11. Check that brewing is cancelled and Cancel Brew screen is shown
    assert brew_page.get_brew_cancelled_main_text() == BREW_CANCELED_LABEL
    # xray.post_screenshot(pytest.test_case_key, brew_page.get_screenshot())

    brew_page.click_brew_cancelled_ok_button()
    # xray.post_screenshot(pytest.test_case_key, brew_page.get_screenshot())

    # STEP 12. Check that main button with Keurig logo is returned
    assert brew_page.check_if_keurig_brew_button_shown()
