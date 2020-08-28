"""
KES Smoke Automation test
"""

import pytest
import Lib.GLOBALS.CLI_COMMANDS as CLI
import time


# pytest -s test_kes_smoke.py --PRODUCT=KES --BOARD_TYPE=Arenal --ARENAL_PORT=COM4 --ARENAL_BAUD=115200 --WRITE_TIMEOUT=1

#reset, then start brew
@pytest.mark.TM_695
def test_695(ser):
    """
    test_695: reset, then start brew
    """
    print("\nSet PRINT_BE ON")
    response = ser.send_receive_data(CLI.PRINT_BE_ON, "PRINT_BE ON")
    pytest.global_response = pytest.global_response.__add__('\nSet PRINT ON\n' + str(response))
    # assert response is True
    time.sleep(2)
    if (response):
        pytest.global_response = pytest.global_response.__add__('\nSet PRINT ON\n' + str(response))
    else:
        response = ser.send_receive_data(CLI.PRINT_BE_ON, "PRINT_BE ON")
    
    print("\nCheck SW_VERSION")
    response = ser.send_receive_data(CLI.SW_VERSION, "K-Elite Smart, Gen2 Brewer DUI MAIN PCB ")    # TODO update the test, threre is no parameter in the config
    
    print("\n Reset")
    # TODO: response = ser.send_receive_data("RESET", "Gen2 Brewer DUI MAIN PCB 1.1.0 starting up")
    # TODO: will implement a better way to handle the output of reset later
    list_of_responses = ser.continuous_send_receive_data("RESET", "Gen2 Brewer DUI MAIN PCB ", lines_to_read=20)
    
    pytest.global_response = pytest.global_response.__add__('\nRESET\n' + str(list_of_responses))    
    if (not list_of_responses):
        print("Failed to RESET")
        status = "Fail"
        return status 
    print(list_of_responses)  
    
    time.sleep(5)
    print("\nSet PRINT_BE ON")
    response = ser.send_receive_data(CLI.PRINT_BE_ON, "PRINT_BE ON")
    pytest.global_response = pytest.global_response.__add__('\nSet PRINT ON\n' + str(response))
    
    print("\nSet POWER OFF")
    response = ser.send_receive_data(CLI.POWER_OFF, "POWER state is OFF")
    pytest.global_response = pytest.global_response.__add__('\nSet POWER OFF\n' + str(response))
    if (not response):
        print("Failed to Set POWER OFF")
        status = "Fail"
        return status 
  
    time.sleep(2)
    print("\nset RECIPE 194 7.5 4")
    response = ser.send_receive_data(CLI.RECIPE_194_75_4, "Custom Recipe: 19400 F") # TODO update the test, threre is no parameter in the config
    pytest.global_response = pytest.global_response.__add__('\nCustom Recipe: 19400 F\n' + str(response))
    # assert response is True
    if (not response):
        print("Failed to Set RECIPE")
        status = "Fail"
        return status 
        
    time.sleep(2)
    print("\nSet POWER ON")
    response = ser.send_receive_data(CLI.POWER_ON, "POWER state is ON")
    pytest.global_response = pytest.global_response.__add__('\nSet POWER state ON\n' + str(response))
    # assert response is True
    if (not response):
        print("Failed to Set POWER ON")
        status = "Fail"
        return status 
        
    time.sleep(2)
    print("\nCheck the state ")
    response = ser.send_receive_data("BE_STATE", "BE State = IDLE")
    time.sleep(5)
    print("\nPERFORM A BREW USING 'START BREW'")
    list_of_responses = ser.continuous_send_receive_data(CLI.START_BREW, 'BREW_SUCCESSFUL', lines_to_read=200)
    if (not list_of_responses):
        print("Failed to START_BREW")
        status = "Fail"
        return status 
    # convert the list with responses to a string for xray upload
    print(list_of_responses)
    for item in list_of_responses:
        pytest.global_response = pytest.global_response.__add__('\n' + item)
    response1 = any("BE brew status BREW_IN_PROGRESS" in elem for elem in list_of_responses)
    response2 = any("BE brew status BREW_SUCCESSFUL" in elem for elem in list_of_responses)
    if (response1 and response2):
        status = "PASS"
    else:
        status = "Fail"
    #status = "PASS" if response is True else "FAIL"
    print(status)
    assert status == "PASS"

#brew after power cycle
@pytest.mark.TM_696
def test_696(ser):
    """
    test_696: brew after power cycle
    """
    print("\nSet PRINT_BE ON")
    response = ser.send_receive_data(CLI.PRINT_BE_ON, "PRINT_BE ON")
    pytest.global_response = pytest.global_response.__add__('Set PRINT ON\n' + str(response))
    # assert response is True
    time.sleep(2)
    if (response):
        pytest.global_response = pytest.global_response.__add__('\nSet PRINT ON\n' + str(response))
    else:
        response = ser.send_receive_data(CLI.PRINT_BE_ON, "PRINT_BE ON")
    
    print("\nShow Version")
    # TODO: will implement a better way to handle the output of sw_version later
    response = ser.send_receive_data(CLI.SW_VERSION, "K-Elite Smart, Gen2 Brewer DUI MAIN PCB ")  # TODO update the test, threre is no parameter in the config
    pytest.global_response = pytest.global_response.__add__('\nK-Elite Smart, Gen2 Brewer DUI MAIN PCB \n' + str(response))
    time.sleep(2)
    print("\nSet POWER OFF")
    response = ser.send_receive_data(CLI.POWER_OFF, "POWER state is OFF")
    pytest.global_response = pytest.global_response.__add__('\nSet POWER OFF\n' + str(response))
    if (not response):
        print("Failed to Set POWER OFF")
        status = "Fail"
        return status 
    time.sleep(2)
    print("\nCheck the state ")
    response = ser.send_receive_data("BE_STATE", "BE State = STANDBY")
    pytest.global_response = pytest.global_response.__add__('\nBE State = STANDBY\n' + str(response))
    if (not response):
        print("Failed to Check the state")
        status = "Fail"
        return status 
    time.sleep(2)
    print("\nSet POWER ON")
    response = ser.send_receive_data(CLI.POWER_ON, "POWER state is ON")
    pytest.global_response = pytest.global_response.__add__('\nSet POWER ON\n' + str(response))
    if (not response):
        print("Failed to Set POWER ON")
        status = "Fail"
        return status 
    time.sleep(2)
    print("\nCheck the state ")
    response = ser.send_receive_data("BE_STATE", "BE State = IDLE")
    pytest.global_response = pytest.global_response.__add__('\nBE State = IDLE\n' + str(response))
    time.sleep(2)
    print("\nSet POWER OFF")
    response = ser.send_receive_data(CLI.POWER_OFF, "POWER state is OFF")
    pytest.global_response = pytest.global_response.__add__('\nSet POWER OFF\n' + str(response))
    if (not response):
        print("Failed to Set POWER OFF")
        status = "Fail"
        return status 
  
    time.sleep(2)
    print("\nset RECIPE 194 7.5 8")
    response = ser.send_receive_data("RECIPE 194 7.5 8", "Custom Recipe: 19400 F")
    pytest.global_response = pytest.global_response.__add__('\nCustom Recipe: 194 7.5 8\n' + str(response))
    # assert response is True
    if (not response):
        print("Failed to Set RECIPE")
        status = "Fail"
        return status 
        
    time.sleep(2)
    print("\nSet POWER ON")
    response = ser.send_receive_data(CLI.POWER_ON, "POWER state is ON")
    pytest.global_response = pytest.global_response.__add__('\nSet POWER state ON\n' + str(response))
    # assert response is True
    if (not response):
        print("Failed to Set POWER ON")
        status = "Fail"
        return status 
        
    time.sleep(2)
    print("\nCheck the state ")
    response = ser.send_receive_data("BE_STATE", "BE State = IDLE")
    pytest.global_response = pytest.global_response.__add__('\nBE State = IDLE\n' + str(response))
    
    time.sleep(5)
    print("\nPERFORM A BREW USING 'START BREW'")
    list_of_responses = ser.continuous_send_receive_data(CLI.START_BREW, 'BREW_SUCCESSFUL', lines_to_read=200)
    if (not list_of_responses):
        print("Failed to START_BREW")
        status = "Fail"
        return status 
    
    print(list_of_responses)
    for item in list_of_responses:
        pytest.global_response = pytest.global_response.__add__('\n' + item)
    response1 = any("BE brew status BREW_IN_PROGRESS" in elem for elem in list_of_responses)
    response2 = any("BE brew status BREW_SUCCESSFUL" in elem for elem in list_of_responses)
    if (response1 and response2):
        status = "PASS"
    else:
        status = "Fail"
    print (status)
    assert status == "PASS"

@pytest.mark.TM_624
def test_624(ser):
    """
    test_624: power off and on
    """
    print("\nSet PRINT_BE ON")
    response = ser.send_receive_data(CLI.PRINT_BE_ON, "PRINT_BE ON")
    pytest.global_response = pytest.global_response.__add__('Set PRINT ON\n' + str(response))
    # assert response is True
    time.sleep(2)
    if (response):
        pytest.global_response = pytest.global_response.__add__('\nSet PRINT ON\n' + str(response))
    else:
        response = ser.send_receive_data(CLI.PRINT_BE_ON, "PRINT_BE ON")
    
    print("\nShow Version")
    # TODO: will implement a better way to handle the output of sw_version later
    response = ser.send_receive_data(CLI.SW_VERSION, "K-Elite Smart, Gen2 Brewer DUI MAIN PCB ")    # TODO update the test, threre is no parameter in the config
    pytest.global_response = pytest.global_response.__add__('\nK-Elite Smart, Gen2 Brewer DUI MAIN PCB \n' + str(response))
    time.sleep(2)
    print("\nSet POWER OFF")
    response = ser.send_receive_data(CLI.POWER_OFF, "POWER state is OFF")
    pytest.global_response = pytest.global_response.__add__('\nSet POWER OFF\n' + str(response))
    if (not response):
        print("Failed to Set POWER OFF")
        status = "Fail"
        return status 
    time.sleep(2)
    print("\nCheck the state ")
    response = ser.send_receive_data("BE_STATE", "BE State = STANDBY")
    pytest.global_response = pytest.global_response.__add__('\nBE State = STANDBY\n' + str(response))
    if (not response):
        print("Failed to Check the state")
        status = "Fail"
        return status 
    time.sleep(3)
    print("\nSet POWER ON")
    response = ser.send_receive_data(CLI.POWER_ON, "POWER state is ON")
    pytest.global_response = pytest.global_response.__add__('\nSet POWER ON\n' + str(response))
    if (not response):
        print("Failed to Set POWER ON")
        status = "Fail"
        return status 
    time.sleep(2)
    print("\nCheck the state ")
    response = ser.send_receive_data("BE_STATE", "BE State = IDLE")
    pytest.global_response = pytest.global_response.__add__('\nBE State = IDLE\n' + str(response))
    
    status = "PASS" if response is True else "FAIL"
    print (status)
    assert status == "PASS"

@pytest.mark.TM_625
def test_625(ser):
    """
    test_625: PM open and close
    """
    print("\nSet PRINT_BE ON")
    response = ser.send_receive_data(CLI.PRINT_BE_ON, "PRINT_BE ON")
    pytest.global_response = pytest.global_response.__add__('\nSet PRINT ON\n' + str(response))
    # assert response is True
    time.sleep(2)
    if (response):
        pytest.global_response = pytest.global_response.__add__('\nSet PRINT ON\n' + str(response))
    else:
        response = ser.send_receive_data(CLI.PRINT_BE_ON, "PRINT_BE ON")
    print("\nShow Version")
    #will implement a better way to handle the output of sw_version later
    response = ser.send_receive_data(CLI.SW_VERSION, "K-Elite Smart, Gen2 Brewer DUI MAIN PCB ")  # TODO update the test, threre is no parameter in the config
    pytest.global_response = pytest.global_response.__add__('\nK-Elite Smart, Gen2 Brewer DUI MAIN PCB \n' + str(response))
    time.sleep(2)
    print("\nSet POWER OFF")                         
    response = ser.send_receive_data(CLI.POWER_OFF, "POWER state is OFF")
    pytest.global_response = pytest.global_response.__add__('\nSet POWER OFF\n' + str(response))
    if (not response):
        print("Failed to Set POWER OFF")
        status = "Fail"
        return status 
    time.sleep(2)
    print("\nCheck the state ")
    response = ser.send_receive_data("BE_STATE", "BE State = STANDBY")
    pytest.global_response = pytest.global_response.__add__('\nBE State = STANDBY\n' + str(response))
    if (not response):
        print("Failed to Set POWER OFF")
        status = "Fail"
        return status 
    time.sleep(2)
    print("\nPM Open")
    response = ser.send_receive_data("PM OPEN", "PM state = OPEN")
    pytest.global_response = pytest.global_response.__add__('\nPM Open\n' + str(response))
    if (not response):
        print("Failed to Open PM")
        status = "Fail"
        return status 
    
    time.sleep(2)
    print("\nCheck the state ")
    response = ser.send_receive_data("BE_STATE", "BE State = STANDBY")
    pytest.global_response = pytest.global_response.__add__('\nBE State = STANDBY\n' + str(response))
    if (not response):
        print("Failed at check the state")
        status = "Fail"
        return status 
    time.sleep(3)    
    print("\nPM Close")
    response = ser.send_receive_data("PM CLOSE", "PM state = CLOSE")
    pytest.global_response = pytest.global_response.__add__('\nPM state = CLOSE\n' + str(response))
    if (not response):
        print("Failed to Close PM")
        status = "Fail"
        return status 
    print("\nCheck the state ")
    response = ser.send_receive_data("BE_STATE", "BE State = IDLE")
    pytest.global_response = pytest.global_response.__add__('\nBE State = IDLE\n' + str(response))   
    status = "PASS" if response is True else "FAIL"
    print (status)
    assert status == "PASS"
    
@pytest.mark.TM_626
def test_626(ser):
    """
    test_626: back to back brews
    """
    print("\nSet PRINT_BE ON")
    response = ser.send_receive_data(CLI.PRINT_BE_ON, "PRINT_BE ON")
    pytest.global_response = pytest.global_response.__add__('\nSet PRINT ON\n' + str(response))
    # assert response is True
    time.sleep(2)
    if (response):
        pytest.global_response = pytest.global_response.__add__('\nSet PRINT ON\n' + str(response))
    else:
        response = ser.send_receive_data(CLI.PRINT_BE_ON, "PRINT_BE ON")
    print("Show version")
    #will implement a better way to handle the output of sw_version later
    response = ser.send_receive_data(CLI.SW_VERSION, "K-Elite Smart, Gen2 Brewer DUI MAIN PCB ")  # TODO update the test, threre is no parameter in the config
    
    print("\nSet POWER OFF")
    response = ser.send_receive_data(CLI.POWER_OFF, "POWER state is OFF")
    pytest.global_response = pytest.global_response.__add__('\nSet POWER OFF\n' + str(response))
    # assert response is True
    if (not response):
        print("Failed to Set POWER OFF")
        status = "Fail"
        return status 
    #print("\nOPEN PM-not currently not supported")

    print("\nset RECIPE 194 7.5 4")
    response = ser.send_receive_data(CLI.RECIPE_194_75_4, "Custom Recipe: 19400 F")
    pytest.global_response = pytest.global_response.__add__('\nCustom Recipe: 19400 F\n' + str(response))
    # assert response is True
    if (not response):
        print("Failed to Set RECIPE")
        status = "Fail"
        return status 
    time.sleep(2)
    print("\nSet POWER ON")
    response = ser.send_receive_data(CLI.POWER_ON, "POWER state is ON")
    pytest.global_response = pytest.global_response.__add__('\nSet POWER state ON\n' + str(response))
    # assert response is True
    if (not response):
        print("Failed to Set POWER ON")
        status = "Fail"
        return status 
        
    time.sleep(2)
    print("\nPERFORM A BREW USING 'START BREW'")
    list_of_responses = ser.continuous_send_receive_data(CLI.START_BREW, 'BREW_SUCCESSFUL', lines_to_read=200)
    if (not list_of_responses):
        print("Failed to START_BREW")
        status = "Fail"
        return status 
        
    # TODO: convert the list with responses to a string for xray upload
    print(list_of_responses)
    for item in list_of_responses:
        pytest.global_response = pytest.global_response.__add__('\n' + item)
    response1 = any("BE brew status BREW_IN_PROGRESS" in elem for elem in list_of_responses)
    response2 = any("BE brew status BREW_SUCCESSFUL" in elem for elem in list_of_responses)
    if (response1 and response2):
        print("wait for 10 seconds...")
        time.sleep(30)
        print("\nSet POWER OFF")
        response = ser.send_receive_data(CLI.POWER_OFF, "POWER state is OFF")
        pytest.global_response = pytest.global_response.__add__('\nSet POWER OFF\n' + str(response))
        if (not response):
            print("Failed to Set POWER OFF")
            status = "Fail"
            return status 
        print("\nset RECIPE 194 7.5 6")
        response = ser.send_receive_data("RECIPE 194 7.5 6", "Custom Recipe: 19400 F")
        pytest.global_response = pytest.global_response.__add__('\nCustom Recipe: 19400 F\n' + str(response))
        # assert response is True
        if (not response):
            print("Failed to Set RECIPE 194 7.5 6")
            status = "Fail"
            return status 
        time.sleep(2)
        print("\nSet POWER ON")
        response = ser.send_receive_data(CLI.POWER_ON, "POWER state is ON")
        pytest.global_response = pytest.global_response.__add__('\nSet POWER state ON\n' + str(response))
        # assert response is True
        if (not response):
            print("Failed to Set POWER ON")
            status = "Fail"
            return status 
        time.sleep(2)
        print("\nPERFORM A BREW USING 'START BREW'")
        list_of_responses = ser.continuous_send_receive_data(CLI.START_BREW, 'BREW_SUCCESSFUL', lines_to_read=200)
        if (not list_of_responses):
            print("Failed to START_BREW")
            status = "Fail"
            return status 
        # convert the list with responses to a string for xray upload
        print(list_of_responses)
        for item in list_of_responses:
            pytest.global_response = pytest.global_response.__add__('\n' + item)
        response3 = any("BE brew status BREW_IN_PROGRESS" in elem for elem in list_of_responses)
        response4 = any("BE brew status BREW_SUCCESSFUL" in elem for elem in list_of_responses)
        if (response3 and response4):
            status = "PASS"
        else:
            status = "Fail"
            
    else:
        status = "Fail"
    
    print(status)
    assert status == "PASS"

@pytest.mark.TM_627
def test_627(ser):
    """
    test_627: brew cancel
    """
    print("\nSet PRINT_BE ON")
    response = ser.send_receive_data(CLI.PRINT_BE_ON, "PRINT_BE ON")
    pytest.global_response = pytest.global_response.__add__('\nSet PRINT_STATE ON\n' + str(response))
    # assert response is True
    time.sleep(2)
    if (response):
        pytest.global_response = pytest.global_response.__add__('\nSet PRINT_STATE ON\n' + str(response))
    else:
        response = ser.send_receive_data(CLI.PRINT_BE_ON, "PRINT_BE ON")
    print("Show version")
    # TODO: will implement a better way to handle the output of sw_version later
    response = ser.send_receive_data(CLI.SW_VERSION, "K-Elite Smart, Gen2 Brewer DUI MAIN PCB ")  # TODO update the test, threre is no parameter in the config
    
    print("\nSet POWER OFF")
    response = ser.send_receive_data(CLI.POWER_OFF, "POWER state is OFF")
    pytest.global_response = pytest.global_response.__add__('\nSet POWER OFF\n' + str(response))
    # assert response is True
    if (not response):
        print("Failed to Set POWER OFF")
        status = "Fail"
    #print("\nOPEN PM-not currently not supported")

    print("\nset RECIPE 194 7.5 8")
    response = ser.send_receive_data("RECIPE 194 7.5 8", "Custom Recipe: 19400 F")
    pytest.global_response = pytest.global_response.__add__('\nCustom Recipe: 19400 F\n' + str(response))
    # assert response is True
    if (not response):
        print("Failed to Set RECIPE ")
        status = "Fail"
        return status 
    time.sleep(2)
    print("\nSet BREW ENGINE LOGGING ON")
    response = ser.send_receive_data(CLI.POWER_ON, "POWER state is ON")
    pytest.global_response = pytest.global_response.__add__('\nSet POWER ON\n' + str(response))
    if (not response):
        print("Failed to Set RECIPE ")
        status = "Fail"
        return status 
    # assert response is True
    time.sleep(2)
    print("\nPERFORM A BREW USING 'START BREW'")
    list_of_responses = ser.continuous_send_receive_data(CLI.START_BREW, 'BREW_IN_PROGRESS', lines_to_read=200)
    if (not list_of_responses):
        print("Failed to START_BREW")
        status = "Fail"
        return status 
        
    print(list_of_responses)
    time.sleep(5)
    print("\nPERFORM CANCEL BREW...")
    list_of_responses = ser.continuous_send_receive_data("CANCEL_BREW", "BREW_CANCELLED", lines_to_read=200)
    pytest.global_response = pytest.global_response.__add__('\nBREW_CANCELLED\n' + str(response))
    if (not list_of_responses):
        print("Failed to CANCEL_BREW")
        status = "Fail"
    else:
        status = "PASS"
    print(list_of_responses)
    print (status)
    assert status == "PASS"
