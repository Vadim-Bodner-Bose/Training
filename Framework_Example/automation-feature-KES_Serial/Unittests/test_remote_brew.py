"""
Unittests to test the Ayla remote brew process
"""

from Lib.AYLA.AylaBrew import AylaRemoteBrew as ayla
from Lib.AYLA.AylaAPIcaller import AylaAPIcaller, EventTypes
from Config import Brewer_Config as brewer

remote_brew = ayla()
aylaAPI = AylaAPIcaller()


def test_check_state():
    aylaAPI.get_device_event(brewer.dsn, EventTypes.STATE)

def test_get_version():
    aylaAPI.get_device_event(brewer.dsn, EventTypes.SW_INFO)


def test_execute_req():
    # remote_brew.execute_req("Brew")
    remote_brew.execute_req("Cancel", brewer.dsn)


def test_execute_brew():
    remote_brew.execute_brew(brewer.dsn)


def test_execute_on_off():
    remote_brew.execute_power_on_off(brewer.dsn)

