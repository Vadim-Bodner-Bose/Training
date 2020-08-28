# Add image the location of the images as a parameter
# Connect to the brewer
# Establish that the app is present
# Execute the Image Recongtion app with the location parameter provided
# Parse the output for pass/fail assert that there no failed results when the tests should pass and nothing passed for negative tests.
# confluence page with info
# https://confluence.keurig.com/pages/viewpage.action?spaceKey=TRAV&title=Recognition+Toolset#RecognitionToolset-ImageRecognitionApplication
import pytest
from InitializeSerialDevice import SerialInit
import threading
import time
from File_Classes import JSON

# comport = 'COM7'
js = JSON()
serial = js.get_json_paramter('premium', 'sandstone')
comport = serial['comport']
# baudrate = 115200
baudrate = int(serial['baudrate'])
# timeout = 7
timeout = int(serial['timeout'])
write_timeout = int(serial['write_timeout'])

# pathToRecogApp = '/ImageRecognitionApplication'
image_recog_data = js.get_json_paramter('premium', 'image_recog')
pathToRecogApp = image_recog_data['pathToRecogApp']

# pathToImages = '/media/pod_images/'
pathToImages = image_recog_data['pathToImages']
# pathToMasterRecipe = '/sandstone_active/recipes/master_recipes.json'
pathToMasterRecipe = image_recog_data['pathToMasterRecipe']
# pathToBrandInfo = '/sandstone_active/recipes/master_brand_info.json'
pathToBrandInfo = image_recog_data['pathToBrandInfo']


class TestValueStorage:
    # identify a value response to store responses between the test methods
    # response.value to access what's stored
    response = None


# instantiate a serial connection
ser = SerialInit(comport, baudrate, timeout, write_timeout)


def test_connection():
    # instantiate connection
    # ser = SerialInit(comport, baudrate)
    # check if the logged in
    assert ser.login_check() == True
    # ser.closeConnection()


# response() is defined in conftest.py
def test_images():
    # todo mount usb stick to /media assume mounted for now?
    # execute a pattern
    # todo create a list of commands and write them in a for loop
    ser.writePattern('cd /media')
    # check the directory to be /media
    ser.writePattern('pwd')
    curDir = ser.readBytes(100)
    # print()
    # print(curDir)
    # print()
    # Build command string to execute recognition tool
    # ImageRecognitionString = '.' + pathToRecogApp + ' --imageDir ' + pathToImages + ' --masterRecipe ' + pathToMasterRecipe + ' --brandInfo ' + pathToBrandInfo + ' | grep -e PodPresent -e Processing\r\n'
    ImageRecognitionString = '.{0} --imageDir {1} --masterRecipe {2} --brandInfo {3} | grep -e PodPresent -e Processing'.format(
        pathToRecogApp, pathToImages, pathToMasterRecipe, pathToBrandInfo)
    # print(ImageRecognitionString)
    ser.writePattern(ImageRecognitionString)
    ser.change_read_timeout(0)
    time.sleep(2)
    # todo figure out how ot make sure everything is read, may be read line by line until '$' is encountered.
    # TestValueStorage.response = ser.readBytes(1400)
    TestValueStorage.response = ser.read_continuous('$')
    print("this is the response!!!!!:", TestValueStorage.response)
    # todo for now checking if the response is a list, later to look for pass, fail, identify which pod is failing etc...
    assert type(TestValueStorage.response) == list


def test_PdPresent():
    string_to_match = 'PodPresent: 0'
    response_list = [i for i in TestValueStorage.response if string_to_match in i]
    # print(response_list)
    # init response
    response = False
    # check if the list matched the string_to_match more than once
    if len(response_list) > 0:
        response = True
    # response = 'PodPresent: 0' in TestValueStorage.response
    assert response == False


def test_LogoAuthenticated():
    string_to_match = 'LogoAuthenticated: 0'
    response_list = [i for i in TestValueStorage.response if string_to_match in i]
    # init response
    response = False
    # check if the list matched the string_to_match more than once
    if len(response_list) > 0:
        response = True
    # response = 'LogoAuthenticated: 0' in TestValueStorage.response
    assert response == False


def test_DMRecognized():
    string_to_match = 'DMRecognized: 0'
    response_list = [i for i in TestValueStorage.response if string_to_match in i]
    # init response
    response = False
    # check if the list matched the string_to_match more than once
    if len(response_list) > 0:
        response = True
    # response = 'DMRecognized: 0' in TestValueStorage.response
    assert response == False

def setup_module(module):
    # todo mount the usb stick 'mount /dev/sda1 /media' try except

def teardown_module(module):

    # cleanup
    ser.closeConnection()
    # del ser, js
    print(" teardown module executed")