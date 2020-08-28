import dlipower as dlipower
import pytest
import os
import threading
from InitializeSerialDevice import SerialInit
from UserInterfaceClasses import VerboseMessages
from File_Classes import JSON
import dlipower
import time
from SupportClasses.remote_access_classes import Rest_API_Class
import pprint, json

# import the module that reads and writes to jason file
# import the module that downloads the build locally to the latestBuild directory can be done over restapi.
# read the com version from json

# define pytest fixtures: com port, baud rate, time out, curVersion, targetVersion
js = JSON()
serial = js.get_json_paramter('premium', 'sandstone')
comport = serial['comport']
baudrate = int(serial['baudrate'])
timeout = int(serial['timeout'])
write_timeout = int(serial['write_timeout'])
# todo read it from the json file
package_name_initial = "programmingPackage"
package_name_target = "programmingPackage1"


def firmware_update(cmd_file_name, comport):
    os.system(("BrewerFWloadv0.42.py " + cmd_file_name + comport + package_name))


# read the current version from json
# read the target version from the build
# initialize connection and check if brewer is booted
ser = SerialInit(comport, baudrate, timeout, write_timeout)


def test_login():
    # todo if failed to boot fail all of the tests or make it a setup module/fixture
    assert ser.login_check() == True
    # ser.closeConnection()


# Initialize Connection and Check Current version (current version should match the one stored in the
# config <jason> file, then close connection
def test_current_version():
    # checks the the current version on the product is the version in the config file
    # read the correct uiVersion string from metadata.json
    readVersion = ser.readVersion()
    # close connection to the port
    ser.closeConnection()
    # read uiVersionString from jason cfg file
    curVersion = js.print_uiVersionString('premium')
    assert readVersion == curVersion


def test_rеflash_target():
    # todo there should be a look up table for DUT1->DSN_ID->{COM_PORT_SandStone:COMx, COM_PORT_Arenal_COMxx}
    # todo other than in the test_config.json to do later, when scaling out to multiple DUTs
    # rewrite the BrewerrFWload script in OOP manner
    # todo make BrewerFWload return true on successfull update and false on failed
    answer = os.system(("BrewerFWloadv0.42.py usb_flash_write_commands.txt " + comport + " " + package_name_target))
    if answer == 0:
        answer = True
    else:
        answer = False
    # #   Installation is complete when the following text appears: The End
    # #     instantiate a timer to see if the "The End" isn't encountered in n-minutes, fail the test, by using threading
    assert answer == True


# Init Connection and Check the Current version, compare the current version to the previous version if the version is different
# and matches the one in the name of the release <need to specify whcih version can I match, that exists in Sandstone and in
# Jenkins build, after the meeting with Ivan.


# pytest.mark.skip(reason="strange serial port behavior")
def test_target_version():
    # wait to compleet boot
    print("Waiting to complete boot cycle...")
    time.sleep(55)
    ser = SerialInit(comport, baudrate, timeout, write_timeout)
    # login check if logged in or attempt to login.  if failed to log in - fail the test.
    time.sleep(2)
    assert ser.login_check() == True
    # check if the readVersion method return the actual read version today as in the config file?
    time.sleep(5)
    curVersion = ser.readVersion()
    ser.closeConnection()
    # versions should match, if update is successful
    # firmware_reflash = js.get_json_paramter('premium','firmware_reflash')
    # todo populate target_uiVersionString with the entry from the build release metadata.json
    rac = Rest_API_Class(
        'http://nexusrepo.gmcr.com:9081/nexus/content/repositories/brewerReleases/premium/v1.1.1/Bld-96/SandStone/')
    # get the file from nexus
    metadata = rac.import_file('metadata.json')
    # print(type(metadata))
    # print(metadata.json())
    # convert the file to json format
    metadata_json = metadata.json()
    # pprint.pprint(metadata_json)
    # extract desired uiVersionString from the file
    target_uiVersionString = metadata_json['uiVersionString']
    #######temp_pull_from_cfg####################################################
    firmware_reflash_string = js.get_json_paramter("premium", "firmware_reflash")
    target_uiVersionString = firmware_reflash_string['target_uiVersionString']
    print(target_uiVersionString)

    # curl -X GET "http://nexusrepo.gmcr.com:9081/nexus/content/repositories/brewerReleases/premium/v1.1.1/Bld-96/SandStone/metadata.json" -o metadata.json
    # will download a file to a local directory as metadata.json
    # this should go into setup module
    # target_uiVersionString = firmware_reflash['target_uiVersionString']
    assert curVersion == target_uiVersionString

#     reflash back to initial version
def test_rеflash_initial():
    # todo there should be a look up table for DUT1->DSN_ID->{COM_PORT_SandStone:COMx, COM_PORT_Arenal_COMxx}
    # todo other than in the test_config.json to do later, when scaling out to multiple DUTs
    # rewrite the BrewerrFWload script in OOP manner
    # todo make BrewerFWload return true on successfull update and false on failed
    answer = os.system(("BrewerFWloadv0.42.py usb_flash_write_commands.txt " + comport + " " + package_name_initial))
    if answer == 0:
        answer = True
    else:
        answer = False
    # #   Installation is complete when the following text appears: The End
    # #     instantiate a timer to see if the "The End" isn't encountered in n-minutes, fail the test, by using threading
    assert answer == True

def test_initial_version():
    # tests that we had successfully reverted to initial version
    print("Waiting to complete boot cycle...")
    time.sleep(55)
    ser = SerialInit(comport, baudrate, timeout, write_timeout)
    # login check if logged in or attempt to login.  if failed to log in - fail the test.
    time.sleep(2)
    assert ser.login_check() == True
    # check if the readVersion method return the actual read version today as in the config file?
    time.sleep(5)
    curVersion = ser.readVersion()
    ser.closeConnection()
    # versions should match, if update is successful
    initial_version = js.print_uiVersionString('premium')
    assert initial_version == curVersion


def check_sup_checkpoint_log():
    # https://confluence.keurig.com/pages/viewpage.action?pageId=122959025
    pass


def setup_module(module):
    # todo set up the mounting of the usb-stick
    pass


def tear_down_module(module):
    # todo set up the unmounting of the usb-stick
    # close serial connection
    # ser.closeConnection()
    pass