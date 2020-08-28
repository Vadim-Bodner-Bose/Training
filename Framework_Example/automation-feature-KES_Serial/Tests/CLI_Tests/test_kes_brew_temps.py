"""
KES Brewing Temperature Tests - From Basic Brewing Test Set
"""

import pytest
import Lib.GLOBALS.CLI_COMMANDS as CLI_COMMANDS
import Lib.GLOBALS.CLI_RESPONSES as CLI_RESPONSES
import time


# python -m  pytest -s Tests\Test_Example\ --testplan TM-3107 --summary Test_Exec
# pytest -s Tests\Test_Example\ --testscope kes_reg
# pytest -s --testscope kes_reg


@pytest.mark.TM_1825
def test_1825(serial):
    """
    Perform a 160 degF brew - spec 157deg-163deg
    """

    response = serial.send_receive_data(CLI_COMMANDS.POWER_OFF, CLI_RESPONSES.KES_POWER_IS_OFF)
    time.sleep(2)
    if response is True:
        pytest.global_response = pytest.global_response.__add__('\nSet POWER OFF\n' + str(response))
    else:
        response = serial.send_receive_data(CLI_COMMANDS.POWER_OFF, CLI_RESPONSES.KES_POWER_IS_OFF)
        pytest.global_response = pytest.global_response.__add__('\nSet POWER OFF\n' + str(response))

    response = serial.send_receive_data(CLI_COMMANDS.KES_BE_STATE, CLI_RESPONSES.KES_BE_STATE_STANDBY)
    time.sleep(2)
    if response is True:
        pytest.global_response = pytest.global_response.__add__('\nCheck BE_STATE\n' + str(response))
    else:
        response = serial.send_receive_data(CLI_COMMANDS.KES_BE_STATE, CLI_RESPONSES.KES_BE_STATE_STANDBY)
        pytest.global_response = pytest.global_response.__add__('\nCheck BE_STATE\n' + str(response))

    print("\nSet recipe 160 7.5 4")
    response = serial.send_receive_data(CLI_COMMANDS.KES_RECIPE_160_75_4, CLI_RESPONSES.KES_160_TEMP)
    time.sleep(2)
    if response is True:
        pytest.global_response = pytest.global_response.__add__('\nSet 160deg recipe\n' + str(response))
    else:
        response = serial.send_receive_data(CLI_COMMANDS.KES_RECIPE_160_75_4, CLI_RESPONSES.KES_160_TEMP)
        pytest.global_response = pytest.global_response.__add__('\nSet 160deg recipe\n' + str(response))

    response = serial.send_receive_data(CLI_COMMANDS.POWER_ON, CLI_RESPONSES.KES_POWER_IS_ON)
    time.sleep(2)
    if response is True:
        pytest.global_response = pytest.global_response.__add__('\nSet POWER ON\n' + str(response))
    else:
        response = serial.send_receive_data(CLI_COMMANDS.POWER_ON, CLI_RESPONSES.KES_POWER_IS_ON)
        pytest.global_response = pytest.global_response.__add__('\nSet POWER ON\n' + str(response))

    response = serial.send_receive_data(CLI_COMMANDS.KES_BE_STATE, CLI_RESPONSES.KES_BE_STATE_IDLE)
    time.sleep(2)
    if response is True:
        pytest.global_response = pytest.global_response.__add__('\nCheck BE_STATE\n' + str(response))
    else:
        response = serial.send_receive_data(CLI_COMMANDS.KES_BE_STATE, CLI_RESPONSES.KES_BE_STATE_IDLE)
        pytest.global_response = pytest.global_response.__add__('\nCheck BE_STATE\n' + str(response))

    response = serial.send_receive_data(CLI_COMMANDS.PRINT_BE_ON, CLI_RESPONSES.KES_PRINT_BE_IS_ON)
    time.sleep(2)
    if response is True:
        pytest.global_response = pytest.global_response.__add__('\nSet PRINT ON\n' + str(response))
    else:
        response = serial.send_receive_data(CLI_COMMANDS.PRINT_BE_ON, CLI_RESPONSES.KES_PRINT_BE_IS_ON)
        pytest.global_response = pytest.global_response.__add__('\nSet PRINT ON\n' + str(response))

    response = serial.send_receive_data(CLI_COMMANDS.VERBOSE_ON, CLI_RESPONSES.KES_VERBOSE_IS_ON)
    time.sleep(2)
    if response is True:
        pytest.global_response = pytest.global_response.__add__('\nVERBOSE is ON\n' + str(response))
    else:
        response = serial.send_receive_data(CLI_COMMANDS.VERBOSE_ON, CLI_RESPONSES.KES_VERBOSE_IS_ON)
        pytest.global_response = pytest.global_response.__add__('\nVERBOSE is ON\n' + str(response))

    print("Start brew")
    response_list = serial.continuous_send_receive_data(CLI_COMMANDS.START_BREW, CLI_RESPONSES.KES_SUCCESSFUL_BREW, lines_to_read= 600)
    for response in response_list:
        response1 = any("T=71 C" in elem for elem in response_list)
        pytest.global_response = pytest.global_response.__add__('\nBrew recipe temp\n' + str(response))
        assert response1

        response2 = any("T,164" in elem for elem in response_list)
        pytest.global_response = pytest.global_response.__add__('\nbrew temperature\n' + str(response))
        assert response2 is False

        response3 = any(CLI_RESPONSES.KES_SUCCESSFUL_BREW in elem for elem in response_list)
        pytest.global_response = pytest.global_response.__add__('\nBREW SUCCESSFUL\n' + str(response))
        assert response3

    pytest.global_response = pytest.global_response.__add__('\nResponse List\n' + str(response_list))

    response = serial.send_receive_data(CLI_COMMANDS.PRINT_BE_OFF, CLI_RESPONSES.KES_PRINT_BE_IS_OFF)
    pytest.global_response = pytest.global_response.__add__('\nSet PRINT OFF\n' + str(response))
    time.sleep(2)

    response = serial.send_receive_data(CLI_COMMANDS.VERBOSE_OFF, CLI_RESPONSES.KES_VERBOSE_IS_OFF)
    pytest.global_response = pytest.global_response.__add__('\nVERBOSE is OFF\n' + str(response))

    time.sleep(30)

@pytest.mark.TM_1826
def test_1826(serial):
    """
    Perform a 187 degF brew - spec 184deg-190deg
    """

    response = serial.send_receive_data(CLI_COMMANDS.POWER_OFF, CLI_RESPONSES.KES_POWER_IS_OFF)
    time.sleep(2)
    if response is True:
        pytest.global_response = pytest.global_response.__add__('\nSet POWER OFF\n' + str(response))
    else:
        response = serial.send_receive_data(CLI_COMMANDS.POWER_OFF, CLI_RESPONSES.KES_POWER_IS_OFF)
        pytest.global_response = pytest.global_response.__add__('\nSet POWER OFF\n' + str(response))

    response = serial.send_receive_data(CLI_COMMANDS.KES_BE_STATE, CLI_RESPONSES.KES_BE_STATE_STANDBY)
    time.sleep(2)
    if response is True:
        pytest.global_response = pytest.global_response.__add__('\nCheck BE_STATE\n' + str(response))
    else:
        response = serial.send_receive_data(CLI_COMMANDS.KES_BE_STATE, CLI_RESPONSES.KES_BE_STATE_STANDBY)
        pytest.global_response = pytest.global_response.__add__('\nCheck BE_STATE\n' + str(response))

    print("\nSet recipe 187 7.5 4")
    response = serial.send_receive_data(CLI_COMMANDS.KES_RECIPE_187_75_4, CLI_RESPONSES.KES_187_TEMP)
    time.sleep(2)
    if response is True:
        pytest.global_response = pytest.global_response.__add__('\nSet 187deg recipe\n' + str(response))
    else:
        response = serial.send_receive_data(CLI_COMMANDS.KES_RECIPE_187_75_4, CLI_RESPONSES.KES_187_TEMP)
        pytest.global_response = pytest.global_response.__add__('\nCheck BE_STATE\n' + str(response))

    response = serial.send_receive_data(CLI_COMMANDS.POWER_ON, CLI_RESPONSES.KES_POWER_IS_ON)
    time.sleep(2)
    if response is True:
        pytest.global_response = pytest.global_response.__add__('\nSet POWER ON\n' + str(response))
    else:
        response = serial.send_receive_data(CLI_COMMANDS.POWER_ON, CLI_RESPONSES.KES_POWER_IS_ON)
        pytest.global_response = pytest.global_response.__add__('\nCheck BE_STATE\n' + str(response))

    response = serial.send_receive_data(CLI_COMMANDS.KES_BE_STATE, CLI_RESPONSES.KES_BE_STATE_IDLE)
    time.sleep(2)
    if response is True:
        pytest.global_response = pytest.global_response.__add__('\nCheck BE_STATE\n' + str(response))
    else:
        response = serial.send_receive_data(CLI_COMMANDS.KES_BE_STATE, CLI_RESPONSES.KES_BE_STATE_IDLE)
        pytest.global_response = pytest.global_response.__add__('\nCheck BE_STATE\n' + str(response))

    response = serial.send_receive_data(CLI_COMMANDS.PRINT_BE_ON, CLI_RESPONSES.KES_PRINT_BE_IS_ON)
    time.sleep(2)
    if response is True:
        pytest.global_response = pytest.global_response.__add__('\nSet PRINT ON\n' + str(response))
    else:
        response = serial.send_receive_data(CLI_COMMANDS.PRINT_BE_ON, CLI_RESPONSES.KES_PRINT_BE_IS_ON)
        pytest.global_response = pytest.global_response.__add__('\nSet PRINT ON\n' + str(response))

    response = serial.send_receive_data(CLI_COMMANDS.VERBOSE_ON, CLI_RESPONSES.KES_VERBOSE_IS_ON)
    time.sleep(2)
    if response is True:
        pytest.global_response = pytest.global_response.__add__('\nVERBOSE is ON\n' + str(response))
    else:
        response = serial.send_receive_data(CLI_COMMANDS.VERBOSE_ON, CLI_RESPONSES.KES_VERBOSE_IS_ON)
        pytest.global_response = pytest.global_response.__add__('\nVERBOSE is ON\n' + str(response))

    print("Start brew")
    response_list = serial.continuous_send_receive_data(CLI_COMMANDS.START_BREW, CLI_RESPONSES.KES_SUCCESSFUL_BREW, lines_to_read= 700)
    for response in response_list:
        response1 = any("T=86 C" in elem for elem in response_list)
        pytest.global_response = pytest.global_response.__add__('\nBrew recipe temp\n' + str(response))
        assert response1

        response2 = any("T,191" in elem for elem in response_list)
        pytest.global_response = pytest.global_response.__add__('\nbrew temperature\n' + str(response))
        assert response2 is False

        response3 = any(CLI_RESPONSES.KES_SUCCESSFUL_BREW in elem for elem in response_list)
        pytest.global_response = pytest.global_response.__add__('\nBREW SUCCESSFUL\n' + str(response))
        assert response3

    pytest.global_response = pytest.global_response.__add__('\nResponse List\n' + str(response_list))

    response = serial.send_receive_data(CLI_COMMANDS.PRINT_BE_OFF, CLI_RESPONSES.KES_PRINT_BE_IS_OFF)
    pytest.global_response = pytest.global_response.__add__('\nSet PRINT OFF\n' + str(response))
    time.sleep(2)

    response = serial.send_receive_data(CLI_COMMANDS.VERBOSE_OFF, CLI_RESPONSES.KES_VERBOSE_IS_OFF)
    pytest.global_response = pytest.global_response.__add__('\nVERBOSE is OFF\n' + str(response))

    time.sleep(30)

@pytest.mark.TM_1827
def test_1827(serial):
    """
    Perform a 191 degF brew - spec 188deg-190deg
    """

    response = serial.send_receive_data(CLI_COMMANDS.POWER_OFF, CLI_RESPONSES.KES_POWER_IS_OFF)
    time.sleep(2)
    if response is True:
        pytest.global_response = pytest.global_response.__add__('\nSet POWER OFF\n' + str(response))
    else:
        response = serial.send_receive_data(CLI_COMMANDS.POWER_OFF, CLI_RESPONSES.KES_POWER_IS_OFF)
        pytest.global_response = pytest.global_response.__add__('\nSet POWER OFF\n' + str(response))

    response = serial.send_receive_data(CLI_COMMANDS.KES_BE_STATE, CLI_RESPONSES.KES_BE_STATE_STANDBY)
    time.sleep(2)
    if response is True:
        pytest.global_response = pytest.global_response.__add__('\nCheck BE_STATE\n' + str(response))
    else:
        response = serial.send_receive_data(CLI_COMMANDS.KES_BE_STATE, CLI_RESPONSES.KES_BE_STATE_STANDBY)
        pytest.global_response = pytest.global_response.__add__('\nCheck BE_STATE\n' + str(response))

    print("\nSet recipe 191 7.5 4")
    response = serial.send_receive_data(CLI_COMMANDS.KES_RECIPE_191_75_4, CLI_RESPONSES.KES_191_TEMP)
    time.sleep(2)
    if response is True:
        pytest.global_response = pytest.global_response.__add__('\nSet 191deg recipe\n' + str(response))
    else:
        response = serial.send_receive_data(CLI_COMMANDS.KES_RECIPE_191_75_4, CLI_RESPONSES.KES_191_TEMP)
        pytest.global_response = pytest.global_response.__add__('\nSet 191deg recipe\n' + str(response))

    response = serial.send_receive_data(CLI_COMMANDS.POWER_ON, CLI_RESPONSES.KES_POWER_IS_ON)
    time.sleep(2)
    if response is True:
        pytest.global_response = pytest.global_response.__add__('\nSet POWER ON\n' + str(response))
    else:
        response = serial.send_receive_data(CLI_COMMANDS.POWER_ON, CLI_RESPONSES.KES_POWER_IS_ON)
        pytest.global_response = pytest.global_response.__add__('\nSet POWER ON\n' + str(response))

    response = serial.send_receive_data(CLI_COMMANDS.KES_BE_STATE, CLI_RESPONSES.KES_BE_STATE_IDLE)
    time.sleep(2)
    if response is True:
        pytest.global_response = pytest.global_response.__add__('\nCheck BE_STATE\n' + str(response))
    else:
        response = serial.send_receive_data(CLI_COMMANDS.KES_BE_STATE, CLI_RESPONSES.KES_BE_STATE_IDLE)
        pytest.global_response = pytest.global_response.__add__('\nCheck BE_STATE\n' + str(response))

    response = serial.send_receive_data(CLI_COMMANDS.PRINT_BE_ON, CLI_RESPONSES.KES_PRINT_BE_IS_ON)
    time.sleep(2)
    if response is True:
        pytest.global_response = pytest.global_response.__add__('\nSet PRINT ON\n' + str(response))
    else:
        response = serial.send_receive_data(CLI_COMMANDS.PRINT_BE_ON, CLI_RESPONSES.KES_PRINT_BE_IS_ON)
        pytest.global_response = pytest.global_response.__add__('\nSet PRINT ON\n' + str(response))

    response = serial.send_receive_data(CLI_COMMANDS.VERBOSE_ON, CLI_RESPONSES.KES_VERBOSE_IS_ON)
    time.sleep(2)
    if response is True:
        pytest.global_response = pytest.global_response.__add__('\nVERBOSE is ON\n' + str(response))
    else:
        response = serial.send_receive_data(CLI_COMMANDS.VERBOSE_ON, CLI_RESPONSES.KES_VERBOSE_IS_ON)
        pytest.global_response = pytest.global_response.__add__('\nVERBOSE is ON\n' + str(response))

    print("Start brew")
    response_list = serial.continuous_send_receive_data(CLI_COMMANDS.START_BREW, CLI_RESPONSES.KES_SUCCESSFUL_BREW, lines_to_read=700)
    for response in response_list:
        response1 = any("T=88 C" in elem for elem in response_list)
        pytest.global_response = pytest.global_response.__add__('\nBrew recipe temp\n' + str(response))
        assert response1

        response2 = any("T,195" in elem for elem in response_list)
        pytest.global_response = pytest.global_response.__add__('\nbrew temperature\n' + str(response))
        assert response2 is False

        response3 = any(CLI_RESPONSES.KES_SUCCESSFUL_BREW in elem for elem in response_list)
        pytest.global_response = pytest.global_response.__add__('\nBREW SUCCESSFUL\n' + str(response))
        assert response3

    pytest.global_response = pytest.global_response.__add__('\nResponse List\n' + str(response_list))

    response = serial.send_receive_data(CLI_COMMANDS.PRINT_BE_OFF, CLI_RESPONSES.KES_PRINT_BE_IS_OFF)
    pytest.global_response = pytest.global_response.__add__('\nSet PRINT OFF\n' + str(response))
    time.sleep(2)
    response = serial.send_receive_data(CLI_COMMANDS.VERBOSE_OFF, CLI_RESPONSES.KES_VERBOSE_IS_OFF)
    pytest.global_response = pytest.global_response.__add__('\nVERBOSE is OFF\n' + str(response))

    time.sleep(30)

@pytest.mark.TM_1828
def test_1828(serial):
    """
    Perform a 194 degF brew - spec 191deg-197deg
    """

    response = serial.send_receive_data(CLI_COMMANDS.POWER_OFF, CLI_RESPONSES.KES_POWER_IS_OFF)
    time.sleep(2)
    if response is True:
        pytest.global_response = pytest.global_response.__add__('\nSet POWER OFF\n' + str(response))
    else:
        response = serial.send_receive_data(CLI_COMMANDS.POWER_OFF, CLI_RESPONSES.KES_POWER_IS_OFF)
        pytest.global_response = pytest.global_response.__add__('\nSet POWER OFF\n' + str(response))

    response = serial.send_receive_data(CLI_COMMANDS.KES_BE_STATE, CLI_RESPONSES.KES_BE_STATE_STANDBY)
    time.sleep(2)
    if response is True:
        pytest.global_response = pytest.global_response.__add__('\nCheck BE_STATE\n' + str(response))
    else:
        response = serial.send_receive_data(CLI_COMMANDS.KES_BE_STATE, CLI_RESPONSES.KES_BE_STATE_STANDBY)
        pytest.global_response = pytest.global_response.__add__('\nCheck BE_STATE\n' + str(response))

    print("\nSet recipe 194 7.5 4")
    response = serial.send_receive_data(CLI_COMMANDS.KES_RECIPE_194_75_4, CLI_RESPONSES.KES_194_TEMP)
    time.sleep(2)
    if response is True:
        pytest.global_response = pytest.global_response.__add__('\nSet 194deg recipe\n' + str(response))
    else:
        response = serial.send_receive_data(CLI_COMMANDS.KES_RECIPE_194_75_4, CLI_RESPONSES.KES_194_TEMP)
        pytest.global_response = pytest.global_response.__add__('\nSet 194deg recipe\n' + str(response))

    response = serial.send_receive_data(CLI_COMMANDS.POWER_ON, CLI_RESPONSES.KES_POWER_IS_ON)
    time.sleep(2)
    if response is True:
        pytest.global_response = pytest.global_response.__add__('\nSet POWER ON\n' + str(response))
    else:
        response = serial.send_receive_data(CLI_COMMANDS.POWER_ON, CLI_RESPONSES.KES_POWER_IS_ON)
        pytest.global_response = pytest.global_response.__add__('\nSet POWER ON\n' + str(response))

    response = serial.send_receive_data(CLI_COMMANDS.KES_BE_STATE, CLI_RESPONSES.KES_BE_STATE_IDLE)
    time.sleep(2)
    if response is True:
        pytest.global_response = pytest.global_response.__add__('\nCheck BE_STATE\n' + str(response))
    else:
        response = serial.send_receive_data(CLI_COMMANDS.KES_BE_STATE, CLI_RESPONSES.KES_BE_STATE_IDLE)
        pytest.global_response = pytest.global_response.__add__('\nCheck BE_STATE\n' + str(response))

    response = serial.send_receive_data(CLI_COMMANDS.PRINT_BE_ON, CLI_RESPONSES.KES_PRINT_BE_IS_ON)
    time.sleep(2)
    if response is True:
        pytest.global_response = pytest.global_response.__add__('\nSet PRINT ON\n' + str(response))
    else:
        response = serial.send_receive_data(CLI_COMMANDS.PRINT_BE_ON, CLI_RESPONSES.KES_PRINT_BE_IS_ON)
        pytest.global_response = pytest.global_response.__add__('\nSet PRINT ON\n' + str(response))

    response = serial.send_receive_data(CLI_COMMANDS.VERBOSE_ON, CLI_RESPONSES.KES_VERBOSE_IS_ON)
    time.sleep(2)
    if response is True:
        pytest.global_response = pytest.global_response.__add__('\nVERBOSE is ON\n' + str(response))
    else:
        response = serial.send_receive_data(CLI_COMMANDS.VERBOSE_ON, CLI_RESPONSES.KES_VERBOSE_IS_ON)
        pytest.global_response = pytest.global_response.__add__('\nVERBOSE is ON\n' + str(response))

    print("Start brew")
    response_list = serial.continuous_send_receive_data(CLI_COMMANDS.START_BREW, CLI_RESPONSES.KES_SUCCESSFUL_BREW, lines_to_read=700)
    for response in response_list:
        response1 = any("T=90 C" in elem for elem in response_list)
        pytest.global_response = pytest.global_response.__add__('\nBrew recipe temp\n' + str(response))
        assert response1

        response2 = any("T,198" in elem for elem in response_list)
        pytest.global_response = pytest.global_response.__add__('\nbrew temperature\n' + str(response))
        assert response2 is False

        response3 = any(CLI_RESPONSES.KES_SUCCESSFUL_BREW in elem for elem in response_list)
        pytest.global_response = pytest.global_response.__add__('\nBREW SUCCESSFUL\n' + str(response))
        assert response3

    pytest.global_response = pytest.global_response.__add__('\nResponse List\n' + str(response_list))

    response = serial.send_receive_data(CLI_COMMANDS.PRINT_BE_OFF, CLI_RESPONSES.KES_PRINT_BE_IS_OFF)
    pytest.global_response = pytest.global_response.__add__('\nSet PRINT OFF\n' + str(response))
    time.sleep(2)

    response = serial.send_receive_data(CLI_COMMANDS.VERBOSE_OFF, CLI_RESPONSES.KES_VERBOSE_IS_OFF)
    pytest.global_response = pytest.global_response.__add__('\nVERBOSE is OFF\n' + str(response))

    time.sleep(30)

@pytest.mark.TM_1829
def test_1829(serial):
    """
    Perform a 196 degF brew - spec 193deg-199deg
    """

    response = serial.send_receive_data(CLI_COMMANDS.POWER_OFF, CLI_RESPONSES.KES_POWER_IS_OFF)
    time.sleep(2)
    if response is True:
        pytest.global_response = pytest.global_response.__add__('\nSet POWER OFF\n' + str(response))
    else:
        response = serial.send_receive_data(CLI_COMMANDS.POWER_OFF, CLI_RESPONSES.KES_POWER_IS_OFF)
        pytest.global_response = pytest.global_response.__add__('\nSet POWER OFF\n' + str(response))

    response = serial.send_receive_data(CLI_COMMANDS.KES_BE_STATE, CLI_RESPONSES.KES_BE_STATE_STANDBY)
    time.sleep(2)
    if response is True:
        pytest.global_response = pytest.global_response.__add__('\nCheck BE_STATE\n' + str(response))
    else:
        response = serial.send_receive_data(CLI_COMMANDS.KES_BE_STATE, CLI_RESPONSES.KES_BE_STATE_STANDBY)
        pytest.global_response = pytest.global_response.__add__('\nCheck BE_STATE\n' + str(response))

    print("\nSet recipe 196 7.5 4")
    response = serial.send_receive_data(CLI_COMMANDS.KES_RECIPE_196_75_4, CLI_RESPONSES.KES_196_TEMP)
    time.sleep(2)
    if response is True:
        pytest.global_response = pytest.global_response.__add__('\nSet 196deg recipe\n' + str(response))
    else:
        response = serial.send_receive_data(CLI_COMMANDS.KES_RECIPE_196_75_4, CLI_RESPONSES.KES_196_TEMP)
        pytest.global_response = pytest.global_response.__add__('\nSet 196deg recipe\n' + str(response))

    response = serial.send_receive_data(CLI_COMMANDS.POWER_ON, CLI_RESPONSES.KES_POWER_IS_ON)
    time.sleep(2)
    if response is True:
        pytest.global_response = pytest.global_response.__add__('\nSet POWER ON\n' + str(response))
    else:
        response = serial.send_receive_data(CLI_COMMANDS.POWER_ON, CLI_RESPONSES.KES_POWER_IS_ON)
        pytest.global_response = pytest.global_response.__add__('\nSet POWER ON\n' + str(response))

    response = serial.send_receive_data(CLI_COMMANDS.KES_BE_STATE, CLI_RESPONSES.KES_BE_STATE_IDLE)
    time.sleep(2)
    if response is True:
        pytest.global_response = pytest.global_response.__add__('\nCheck BE_STATE\n' + str(response))
    else:
        response = serial.send_receive_data(CLI_COMMANDS.KES_BE_STATE, CLI_RESPONSES.KES_BE_STATE_IDLE)
        pytest.global_response = pytest.global_response.__add__('\nCheck BE_STATE\n' + str(response))

    response = serial.send_receive_data(CLI_COMMANDS.PRINT_BE_ON, CLI_RESPONSES.KES_PRINT_BE_IS_ON)
    time.sleep(2)
    if response is True:
        pytest.global_response = pytest.global_response.__add__('\nSet PRINT ON\n' + str(response))
    else:
        response = serial.send_receive_data(CLI_COMMANDS.PRINT_BE_ON, CLI_RESPONSES.KES_PRINT_BE_IS_ON)
        pytest.global_response = pytest.global_response.__add__('\nSet PRINT ON\n' + str(response))

    response = serial.send_receive_data(CLI_COMMANDS.VERBOSE_ON, CLI_RESPONSES.KES_VERBOSE_IS_ON)
    time.sleep(2)
    if response is True:
        pytest.global_response = pytest.global_response.__add__('\nVERBOSE is ON\n' + str(response))
    else:
        response = serial.send_receive_data(CLI_COMMANDS.VERBOSE_ON, CLI_RESPONSES.KES_VERBOSE_IS_ON)
        pytest.global_response = pytest.global_response.__add__('\nVERBOSE is ON\n' + str(response))

    print("Start brew")
    response_list = serial.continuous_send_receive_data(CLI_COMMANDS.START_BREW, CLI_RESPONSES.KES_SUCCESSFUL_BREW, lines_to_read=700)
    for response in response_list:
        response1 = any("T=91 C" in elem for elem in response_list)
        pytest.global_response = pytest.global_response.__add__('\nBrew recipe temp\n' + str(response))
        assert response1

        response2 = any("T,200" in elem for elem in response_list)
        pytest.global_response = pytest.global_response.__add__('\nbrew temperature\n' + str(response))
        assert response2 is False

        response3 = any(CLI_RESPONSES.KES_SUCCESSFUL_BREW in elem for elem in response_list)
        pytest.global_response = pytest.global_response.__add__('\nBREW SUCCESSFUL\n' + str(response))
        assert response3

    pytest.global_response = pytest.global_response.__add__('\nResponse List\n' + str(response_list))

    response = serial.send_receive_data(CLI_COMMANDS.PRINT_BE_OFF, CLI_RESPONSES.KES_PRINT_BE_IS_OFF)
    pytest.global_response = pytest.global_response.__add__('\nSet PRINT OFF\n' + str(response))
    time.sleep(2)

    response = serial.send_receive_data(CLI_COMMANDS.VERBOSE_OFF, CLI_RESPONSES.KES_VERBOSE_IS_OFF)
    pytest.global_response = pytest.global_response.__add__('\nVERBOSE is OFF\n' + str(response))

    time.sleep(30)

@pytest.mark.TM_1830
def test_1830(serial):
    """
    Perform a 200 degF brew - spec 197deg-203deg
    """

    response = serial.send_receive_data(CLI_COMMANDS.POWER_OFF, CLI_RESPONSES.KES_POWER_IS_OFF)
    time.sleep(2)
    if response is True:
        pytest.global_response = pytest.global_response.__add__('\nSet POWER OFF\n' + str(response))
    else:
        response = serial.send_receive_data(CLI_COMMANDS.POWER_OFF, CLI_RESPONSES.KES_POWER_IS_OFF)
        pytest.global_response = pytest.global_response.__add__('\nSet POWER OFF\n' + str(response))

    response = serial.send_receive_data(CLI_COMMANDS.KES_BE_STATE, CLI_RESPONSES.KES_BE_STATE_STANDBY)
    time.sleep(2)
    if response is True:
        pytest.global_response = pytest.global_response.__add__('\nCheck BE_STATE\n' + str(response))
    else:
        response = serial.send_receive_data(CLI_COMMANDS.KES_BE_STATE, CLI_RESPONSES.KES_BE_STATE_STANDBY)
        pytest.global_response = pytest.global_response.__add__('\nCheck BE_STATE\n' + str(response))

    print("\nSet recipe 200 7.5 4")
    response = serial.send_receive_data(CLI_COMMANDS.KES_RECIPE_200_75_4, CLI_RESPONSES.KES_200_TEMP)
    time.sleep(2)
    if response is True:
        pytest.global_response = pytest.global_response.__add__('\nSet 200deg recipe\n' + str(response))
    else:
        response = serial.send_receive_data(CLI_COMMANDS.KES_RECIPE_200_75_4, CLI_RESPONSES.KES_200_TEMP)
        pytest.global_response = pytest.global_response.__add__('\nSet 200deg recipe\n' + str(response))

    response = serial.send_receive_data(CLI_COMMANDS.POWER_ON, CLI_RESPONSES.KES_POWER_IS_ON)
    time.sleep(2)
    if response is True:
        pytest.global_response = pytest.global_response.__add__('\nSet POWER ON\n' + str(response))
    else:
        response = serial.send_receive_data(CLI_COMMANDS.POWER_ON, CLI_RESPONSES.KES_POWER_IS_ON)
        pytest.global_response = pytest.global_response.__add__('\nSet POWER ON\n' + str(response))

    response = serial.send_receive_data(CLI_COMMANDS.KES_BE_STATE, CLI_RESPONSES.KES_BE_STATE_IDLE)
    time.sleep(2)
    if response is True:
        pytest.global_response = pytest.global_response.__add__('\nCheck BE_STATE\n' + str(response))
    else:
        response = serial.send_receive_data(CLI_COMMANDS.KES_BE_STATE, CLI_RESPONSES.KES_BE_STATE_IDLE)
        pytest.global_response = pytest.global_response.__add__('\nCheck BE_STATE\n' + str(response))

    response = serial.send_receive_data(CLI_COMMANDS.PRINT_BE_ON, CLI_RESPONSES.KES_PRINT_BE_IS_ON)
    time.sleep(2)
    if response is True:
        pytest.global_response = pytest.global_response.__add__('\nSet PRINT ON\n' + str(response))
    else:
        response = serial.send_receive_data(CLI_COMMANDS.PRINT_BE_ON, CLI_RESPONSES.KES_PRINT_BE_IS_ON)
        pytest.global_response = pytest.global_response.__add__('\nSet PRINT ON\n' + str(response))

    response = serial.send_receive_data(CLI_COMMANDS.VERBOSE_ON, CLI_RESPONSES.KES_VERBOSE_IS_ON)
    time.sleep(2)
    if response is True:
        pytest.global_response = pytest.global_response.__add__('\nVERBOSE is ON\n' + str(response))
    else:
        response = serial.send_receive_data(CLI_COMMANDS.VERBOSE_ON, CLI_RESPONSES.KES_VERBOSE_IS_ON)
        pytest.global_response = pytest.global_response.__add__('\nVERBOSE is ON\n' + str(response))

    print("Start brew")
    response_list = serial.continuous_send_receive_data(CLI_COMMANDS.START_BREW, CLI_RESPONSES.KES_SUCCESSFUL_BREW, lines_to_read=700)
    for response in response_list:
        response1 = any("T=93 C" in elem for elem in response_list)
        pytest.global_response = pytest.global_response.__add__('\nBrew recipe temp\n' + str(response))
        assert response1

        response2 = any("T,204" in elem for elem in response_list)
        pytest.global_response = pytest.global_response.__add__('\nbrew temperature\n' + str(response))
        assert response2 is False

        response3 = any(CLI_RESPONSES.KES_SUCCESSFUL_BREW in elem for elem in response_list)
        pytest.global_response = pytest.global_response.__add__('\nBREW SUCCESSFUL\n' + str(response))
        assert response3

    pytest.global_response = pytest.global_response.__add__('\nResponse List\n' + str(response_list))

    response = serial.send_receive_data(CLI_COMMANDS.PRINT_BE_OFF, CLI_RESPONSES.KES_PRINT_BE_IS_OFF)
    pytest.global_response = pytest.global_response.__add__('\nSet PRINT OFF\n' + str(response))
    time.sleep(2)

    response = serial.send_receive_data(CLI_COMMANDS.VERBOSE_OFF, CLI_RESPONSES.KES_VERBOSE_IS_OFF)
    pytest.global_response = pytest.global_response.__add__('\nVERBOSE is OFF\n' + str(response))

    time.sleep(30)

@pytest.mark.TM_1831
def test_1831(serial):
    """
    Perform a 204 degF brew - spec 201deg-207deg
    """

    response = serial.send_receive_data(CLI_COMMANDS.POWER_OFF, CLI_RESPONSES.KES_POWER_IS_OFF)
    time.sleep(2)
    if response is True:
        pytest.global_response = pytest.global_response.__add__('\nSet POWER OFF\n' + str(response))
    else:
        response = serial.send_receive_data(CLI_COMMANDS.POWER_OFF, CLI_RESPONSES.KES_POWER_IS_OFF)
        pytest.global_response = pytest.global_response.__add__('\nSet POWER OFF\n' + str(response))

    response = serial.send_receive_data(CLI_COMMANDS.KES_BE_STATE, CLI_RESPONSES.KES_BE_STATE_STANDBY)
    time.sleep(2)
    if response is True:
        pytest.global_response = pytest.global_response.__add__('\nCheck BE_STATE\n' + str(response))
    else:
        response = serial.send_receive_data(CLI_COMMANDS.KES_BE_STATE, CLI_RESPONSES.KES_BE_STATE_STANDBY)
        pytest.global_response = pytest.global_response.__add__('\nCheck BE_STATE\n' + str(response))

    print("\nSet recipe 204 7.5 4")
    response = serial.send_receive_data(CLI_COMMANDS.KES_RECIPE_204_75_4, CLI_RESPONSES.KES_204_TEMP)
    time.sleep(2)
    if response is True:
        pytest.global_response = pytest.global_response.__add__('\nSet 204deg recipe\n' + str(response))
    else:
        response = serial.send_receive_data(CLI_COMMANDS.KES_RECIPE_204_75_4, CLI_RESPONSES.KES_204_TEMP)
        pytest.global_response = pytest.global_response.__add__('\nSet 204deg recipe\n' + str(response))

    response = serial.send_receive_data(CLI_COMMANDS.POWER_ON, CLI_RESPONSES.KES_POWER_IS_ON)
    time.sleep(2)
    if response is True:
        pytest.global_response = pytest.global_response.__add__('\nSet POWER ON\n' + str(response))
    else:
        response = serial.send_receive_data(CLI_COMMANDS.POWER_ON, CLI_RESPONSES.KES_POWER_IS_ON)
        pytest.global_response = pytest.global_response.__add__('\nSet POWER ON\n' + str(response))

    response = serial.send_receive_data(CLI_COMMANDS.KES_BE_STATE, CLI_RESPONSES.KES_BE_STATE_IDLE)
    time.sleep(2)
    if response is True:
        pytest.global_response = pytest.global_response.__add__('\nCheck BE_STATE\n' + str(response))
    else:
        response = serial.send_receive_data(CLI_COMMANDS.KES_BE_STATE, CLI_RESPONSES.KES_BE_STATE_IDLE)
        pytest.global_response = pytest.global_response.__add__('\nCheck BE_STATE\n' + str(response))

    response = serial.send_receive_data(CLI_COMMANDS.PRINT_BE_ON, CLI_RESPONSES.KES_PRINT_BE_IS_ON)
    time.sleep(2)
    if response is True:
        pytest.global_response = pytest.global_response.__add__('\nSet PRINT ON\n' + str(response))
    else:
        response = serial.send_receive_data(CLI_COMMANDS.PRINT_BE_ON, CLI_RESPONSES.KES_PRINT_BE_IS_ON)
        pytest.global_response = pytest.global_response.__add__('\nSet PRINT ON\n' + str(response))

    response = serial.send_receive_data(CLI_COMMANDS.VERBOSE_ON, CLI_RESPONSES.KES_VERBOSE_IS_ON)
    time.sleep(2)
    if response is True:
        pytest.global_response = pytest.global_response.__add__('\nVERBOSE is ON\n' + str(response))
    else:
        response = serial.send_receive_data(CLI_COMMANDS.VERBOSE_ON, CLI_RESPONSES.KES_VERBOSE_IS_ON)
        pytest.global_response = pytest.global_response.__add__('\nVERBOSE is ON\n' + str(response))

    print("Start brew")
    response_list = serial.continuous_send_receive_data(CLI_COMMANDS.START_BREW, CLI_RESPONSES.KES_SUCCESSFUL_BREW, lines_to_read=700)
    for response in response_list:
        response1 = any("T=95 C" in elem for elem in response_list)
        pytest.global_response = pytest.global_response.__add__('\nBrew recipe temp\n' + str(response))
        assert response1

        response2 = any("T,208" in elem for elem in response_list)
        pytest.global_response = pytest.global_response.__add__('\nbrew temperature\n' + str(response))
        assert response2 is False

        response3 = any(CLI_RESPONSES.KES_SUCCESSFUL_BREW in elem for elem in response_list)
        pytest.global_response = pytest.global_response.__add__('\nBREW SUCCESSFUL\n' + str(response))
        assert response3

    pytest.global_response = pytest.global_response.__add__('\nResponse List\n' + str(response_list))

    response = serial.send_receive_data(CLI_COMMANDS.PRINT_BE_OFF, CLI_RESPONSES.KES_PRINT_BE_IS_OFF)
    pytest.global_response = pytest.global_response.__add__('\nSet PRINT OFF\n' + str(response))
    time.sleep(2)

    response = serial.send_receive_data(CLI_COMMANDS.VERBOSE_OFF, CLI_RESPONSES.KES_VERBOSE_IS_OFF)
    pytest.global_response = pytest.global_response.__add__('\nVERBOSE is OFF\n' + str(response))

    time.sleep(30)