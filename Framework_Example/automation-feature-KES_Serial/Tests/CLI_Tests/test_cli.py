"""
Test suite holds all CLI tests under regression for any product
"""

import Lib.GLOBALS.FVT_COMMANDS as FVT
import Lib.GLOBALS.CLI_COMMANDS as CLI
import time
import pytest

@pytest.mark.unknown
def test_fvt(serial):
    serial.send_receive_data("POWER OFF", "POWER state is OFF")
    serial.send_receive_data("????????", "TESTMODE/TESTVER")

@pytest.mark.TM_306
def test_ttl_script(serial):

    print("\nMaster Relay")
    assert serial.send_receive_data(FVT.K2500_DIGIO_LEVEL_SET_2_H, "ACK") is True
    time.sleep(1)
    assert serial.send_receive_data(FVT.K2500_DIGIO_LEVEL_SET_2_L, "ACK") is True
    time.sleep(1)
    print("Inlet Valve")
    assert serial.send_receive_data(FVT.K2500_DIGIO_LEVEL_SET_3_H, "ACK") is True
    time.sleep(1)
    assert serial.send_receive_data(FVT.K2500_DIGIO_LEVEL_SET_3_L, "ACK") is True
    time.sleep(1)
    print("Water Pump")
    assert serial.send_receive_data(FVT.K2500_DIGIO_PWM_SET_0, "ACK") is True
    time.sleep(1)
    assert serial.send_receive_data(FVT.K2500_DIGIO_PWM_SET_0_0, "ACK") is True
    time.sleep(1)
    print("Air Pump")
    assert serial.send_receive_data(FVT.K2500_DIGIO_PWM_SET_1_500, "ACK") is True
    time.sleep(1)
    assert serial.send_receive_data(FVT.K2500_DIGIO_PWM_SET_1_0, "ACK") is True
    time.sleep(1)
    assert serial.send_receive_data(FVT.K2500_DIGIO_PWM_SET_1_1000, "ACK") is True
    time.sleep(1)
    assert serial.send_receive_data(FVT.K2500_DIGIO_PWM_SET_1_0, "ACK") is True
    time.sleep(1)
    print("CWT Sensor")
    assert serial.send_receive_data(FVT.K2500_DIGIO_LEVEL_5_H, "ACK") is True
    time.sleep(1)
    assert serial.send_receive_data(FVT.K2500_DIGIO_LEVEL_SET_5_L, "ACK") is True
    time.sleep(1)
    assert serial.send_receive_data(FVT.K2500_ADC_GET_ADC_1, range(0, 1023))
    time.sleep(1)
    print("HWT Sensor")
    assert serial.send_receive_data(FVT.K2500_DIGIO_LEVEL_SET_6_H, "ACK") is True
    time.sleep(1)
    assert serial.send_receive_data(FVT.K2500_DIGIO_LEVEL_SET_DIO_6_L, "ACK") is True
    time.sleep(1)
    assert serial.send_receive_data(FVT.K2500_ADC_GET_ADC_3, range(0, 1023))
    time.sleep(1)
    print("Internal CWT Sensor")
    assert serial.send_receive_data(FVT.K2500_DIGIO_LEVEL_SET_DIO_7_H, "ACK") is True
    time.sleep(1)
    assert serial.send_receive_data(FVT.K2500_DIGIO_LEVEL_SET_DIO_7_L, "ACK") is True
    time.sleep(1)
    assert serial.send_receive_data(FVT.K2500_ADC_GET_ADC_4, range(0, 1023))
    time.sleep(1)
    print("PM")
    assert serial.send_receive_data(FVT.K2500_DIGIO_LEVEL_SET_DIO_4_H, "ACK") is True
    time.sleep(1)
    assert serial.send_receive_data(FVT.K2500_DIGIO_LEVEL_SET_DIO_4_L, "ACK") is True
    time.sleep(1)
    print("Heater Triac")
    assert serial.send_receive_data(FVT.K2500_DIGIO_LEVEL_SET_2_H, "ACK") is True
    time.sleep(1)
    assert serial.send_receive_data(FVT.K2500_DIGIO_LEVEL_SET_1_H, "ACK") is True
    time.sleep(1)
    val1 = serial.send_receive_data(FVT.K2500_ADC_GET_ADC_2, range(0, 3000))
    time.sleep(5)
    val2 = serial.send_receive_data(FVT.K2500_ADC_GET_ADC_2, range(0, 3000))
    assert serial.send_receive_data(FVT.K2500_DIGIO_LEVEL_SET_2_L, "ACK") is True
    assert serial.send_receive_data(FVT.K2500_DIGIO_LEVEL_SET_1_L, "ACK") is True
    assert val1 < val2
    time.sleep(1)
    print("HWT Relay")
    assert serial.send_receive_data(FVT.K2500_DIGIO_LEVEL_SET_2_H, "ACK") is True
    time.sleep(1)
    assert serial.send_receive_data(FVT.K2500_DIGIO_LEVEL_SET_0_H, "ACK") is True
    time.sleep(1)
    val1 = serial.send_receive_data(FVT.K2500_ADC_GET_ADC_2, range(0, 3000))
    time.sleep(5)
    val2 = serial.send_receive_data(FVT.K2500_ADC_GET_ADC_2, range(0, 3000))
    assert serial.send_receive_data(FVT.K2500_DIGIO_LEVEL_SET_2_L, "ACK") is True
    assert serial.send_receive_data(FVT.K2500_DIGIO_LEVEL_SET_0_L, "ACK") is True
    assert val1 < val2
    time.sleep(1)
    print("Plumb Configuration")
    assert serial.send_receive_data(FVT.K2500_DIGIO_LEVEL_SET_10_H, "ACK") is True
    time.sleep(1)
    assert serial.send_receive_data(FVT.K2500_DIGIO_LEVEL_SET_10_L, "ACK") is True
    time.sleep(1)


@pytest.mark.TM_356
def test_auto_brew(serial):
    assert serial.send_receive_data(CLI.PRINT_BE_ON, "PRINT_BE is ON") is True
    assert serial.send_receive_data(CLI.POWER_OFF, "POWER state is OFF") is True
    assert serial.send_receive_data(CLI.BREW_TEMP_194, "Temp=") is True
    assert serial.send_receive_data(CLI.BREW_TYPE_NORMAL, "BREW TYPE = Normal") is True
    # TODO: handle edge case for recipes
    assert serial.send_receive_data(CLI.RECIPE_4OZ_ROBUST_HIGH, "SIZE=4 oz") is True
    assert serial.send_receive_data(CLI.AUTO_BREW, "AUTO BREW: COUNT=3, DELAY=5 SECS, SIZE=4 OZ, TYPE=NORMAL") is True
    assert serial.send_receive_data(CLI.POWER_ON, "POWER state is ON") is True
    # TODO: handle post brew logging

