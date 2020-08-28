from Config.MobileApp_Config import WIFI_NETWORK
from Lib.SerialConnection import SerialConnection
import pytest
import Lib.GLOBALS.CLI_COMMANDS as CLI
from Lib.GLOBALS.CLI_RESPONSES import PRE_BE_LOGGING_ON, AL_WIFI_PROFILE, SS_RESET
import Config.Brewer_Config as Brewer_Config


@pytest.fixture(scope='module')
def ser():
    """
    Ensures the serial connection is closed after a test runs
    """
    ser = SerialConnection(com_port=Brewer_Config.COM_PORT, baud_rate=Brewer_Config.BAUD_RATE, write_timeout=1)
    ser.establish_connection()
    yield ser
    ser.close_connection()


def test_sandstone_send_data(ser):
    """
    Simple test for sending data and getting response through sandstone

    """
    assert ser.send_receive_data(CLI.SS_RESET, SS_RESET)


def test_arenal_send_data(ser):
    """
    Simple test for sending data and getting response through arenal
    """

    assert ser.send_receive_data(CLI.PRINT_BE_ON, PRE_BE_LOGGING_ON)


def test_arenal_connection_failure():
    """
      This Test should fail and raise an assertion, when not enough parameters are passed, Arenal Port is omitted.
    """
    ser = SerialConnection(com_port=Brewer_Config.COM_PORT, baud_rate=Brewer_Config.BAUD_RATE, write_timeout=1)
    ser.establish_connection()
    assert ser.send_receive_data(CLI.PRINT_BE_ON, PRE_BE_LOGGING_ON)


def test_read_data(ser):
    """test the Serial Read Data Method and demo the usage"""
    ser.send_data(CLI.PRINT_BE_ON)
    # if the command comes from a source, other than a CLI, example: Mobile APP, Ayla API Call and you would to read
    # the output on Arenal
    ser.read_data(PRE_BE_LOGGING_ON)


def test_connectivity_setup():
    ser = SerialConnection(com_port=Brewer_Config.COM_PORT_1, baud_rate=Brewer_Config.BAUD_RATE_1, write_timeout=1)
    ser.establish_connection()
    assert ser.send_receive_data(CLI.AL_CURRENT_WIFI_STATUS, AL_WIFI_PROFILE.format(WIFI_NETWORK), 40)
