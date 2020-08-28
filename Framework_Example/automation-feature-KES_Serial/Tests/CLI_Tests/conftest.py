import pytest
import Config.Brewer_Config as BREWER
from Lib.SerialConnection import SerialConnection

def pytest_addoption(parser):
    parser.addoption("--com_port", action="store", default=BREWER.COM_PORT)
    parser.addoption("--baud_rate", action="store", default=BREWER.BAUD_RATE)
    parser.addoption("--write_timeout", action="store", type=int, default=1)

# return the serial object to the test and tear down the serial at the end.
@pytest.fixture(scope='module')
def serial(request):
    # Keys <example:board_type - must match the property names in the lib>
    serial = SerialConnection(write_timeout=request.config.getoption("--write_timeout"),
                              com_port=request.config.getoption("--com_port"),
                              baud_rate=request.config.getoption("--baud_rate"))
    serial.establish_connection()
    yield serial
    serial.close_connection()