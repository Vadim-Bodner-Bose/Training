import pytest
from Lib.GLOBALS import CLI_COMMANDS as CLI
from Lib.GLOBALS.CLI_RESPONSES import PRE_BE_LOGGING_ON, PRE_BE_POWER_STATE_OFF
from Lib.MobileAppiumService.appium_helper import AppiumUtils
from Lib.MobileAppiumService.appium_helper import get_config, get_mobile_arguments
from Lib.SerialConnection import SerialConnection
import Config.Brewer_Config as Brewer_Config
import Config.MobileApp_Config as MobileApp_Config


def pytest_addoption(parser):
    """
    Parse command line --platform parameters
    """
    parser.addoption("--platform", action="store", default="Android")
    parser.addoption("--dsn", action="store", default=Brewer_Config.dsn)
    parser.addoption("--mobile_environment", action="store", default=MobileApp_Config.MOBILE_ENVIRONMENT)
    parser.addoption("--connectivity_port", action="store", default=Brewer_Config.COM_PORT_1)
    parser.addoption("--connectivity_baud", action="store", default=Brewer_Config.BAUD_RATE_1)
    parser.addoption("--arenal_port", action="store", default=Brewer_Config.COM_PORT)
    parser.addoption("--arenal_baud", action="store", default=Brewer_Config.BAUD_RATE)
    parser.addoption("--wifi_network", action="store", default=MobileApp_Config.WIFI_NETWORK)
    parser.addoption("--wifi_password", action="store", default=MobileApp_Config.WIFI_PASSWORD)

    appium_config = get_mobile_arguments()
    for key in appium_config:
        parser.addoption('--' + key, action="store", default=appium_config[key])


@pytest.fixture(scope="session")
def dsn(request):
    """
    Return DSN of the brewer to be tested
    """
    return request.config.getoption("--dsn")


@pytest.fixture(scope="session")
def mobile_environment(request):
    """
    Return Mobile Environment to be tested
    """
    return request.config.getoption("--mobile_environment")


@pytest.fixture(scope="session")
def wifi_network(request):
    """
    Return Wifi Network for Mobile Phone to connect

    """
    return request.config.getoption("--wifi_network")


@pytest.fixture(scope="session")
def wifi_password(request):
    """
    Return Wifi Network for Mobile Phone to connect
    """
    return request.config.getoption("--wifi_password")


@pytest.fixture(scope="session")
def serial_con(request):
    """
    Connectivity Board Serial Connection

    """
    com_port = request.config.getoption('--connectivity_port')
    baud_rate = request.config.getoption('--connectivity_baud')
    serial_con = SerialConnection(write_timeout=1, com_port=com_port, baud_rate=baud_rate)
    serial_con.establish_connection()
    yield serial_con
    serial_con.close_connection()


@pytest.fixture(scope="session")
def serial_ar(request):
    """
    Arenal Serial Connection

    """
    com_port = request.config.getoption('--arenal_port')
    baud_rate = request.config.getoption('--arenal_baud')
    serial_ar = SerialConnection(write_timeout=1, com_port=com_port, baud_rate=baud_rate)
    serial_ar.establish_connection()
    # Enable Brew Engine Logging
    serial_ar.send_receive_data(CLI.PRINT_BE_ON, PRE_BE_LOGGING_ON)
    yield serial_ar
    serial_ar.send_receive_data(CLI.POWER_OFF, PRE_BE_POWER_STATE_OFF)
    serial_ar.close_connection()


@pytest.fixture(scope="session")
def driver(request, pytestconfig):
    """
    Create Appium driver
    """
    appium_configs = get_config(request.config.getoption("--platform"), pytestconfig.option)
    driver = AppiumUtils(appium_configs).driver
    yield driver
    driver.quit()
