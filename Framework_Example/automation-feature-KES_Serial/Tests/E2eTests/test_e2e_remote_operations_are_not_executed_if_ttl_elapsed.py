# KP-21507 E2E | Remote Operations | Remote operations are not executed if TTL has elapsed
import pytest

from Config.MobileApp_Config import MOBILE_VERSION, E2E_USER_DEFAULT_LOGIN, \
    E2E_USER_DEFAULT_PASSWORD
from Lib.GLOBALS.CLI_RESPONSES import PRE_BREW_COMPLETE
from Lib.GLOBALS.MOBILE_APP_TEXT_ATTRIBUTES import POD_RECOG_TITLE, POD_RECOG_VARIETY
from Lib.MobileAppiumService.page_objects.brew_page import BrewPgHelper
from Lib.MobileAppiumService.page_objects.gate_page import SplashPgHelper
from Lib.MobileAppiumService.page_objects.sign_in_page import SignInPgHelper
from Utils.DateTime import DateTime as Time


@pytest.mark.KP_21507
def test_e2e_remote_operations_are_not_executed_if_TTL_has_elapsed(driver, xray, serial_ar, dsn):
    gate_page = SplashPgHelper(driver)

    # STEP 1: Open Splash page, check version, env
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

    # STEP 6. Check title and variety names of pod
    assert brew_page.get_pod_recognition_title_text() == POD_RECOG_TITLE
    assert brew_page.get_pod_recognition_variety_text() == POD_RECOG_VARIETY

    # STEP 7. Switch off network connection on brewer
    # TODO: Ayla CLI integration - switch off network connection on brewer

    # STEP 8. Tap BREW button
    brew_page.click_start_brewing()

    # STEP 8.1 Optional. Confirm mug is settled
    if brew_page.check_if_continue_brew_shown():
        brew_page.click_check_your_mug_continue_brew()
    # TODO: Ayla integration - new req datpoint was created with
    xray.post_screenshot(pytest.test_case_key, brew_page.get_screenshot())

    # STEP 9. Wait 30 sec
    Time.explicit_wait(30)

    # STEP 10. Switch on network connection on brewer
    # TODO: Ayla CLI integration - switch on network connection on brewer

    # STEP 11.
    # TODO: Ayla integration - no new state datapoint was created

    # STEP 12.
    # TODO: Arenal CLI integration - no brew has happened
    # needs to be kicked off immediately after start brewing is pressed
    assert serial_ar.read_data(PRE_BREW_COMPLETE, 80)

    # STEP 13. Check that BREW button is returned to default state
    assert brew_page.check_if_keurig_brew_button_shown()
    xray.post_screenshot(pytest.test_case_key, brew_page.get_screenshot())
