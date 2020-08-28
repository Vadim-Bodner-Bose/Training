#ToDo set up parameters for the baud rate and devType, as well as the waitDelay - T to wait for output
import serial
import sys
import time
import threading
import re

# declare a desired version to compare to the one read from the metadata.json
# this should come from a config file on the jenkins server or a repo in bitbucket
uiVersionString = "1.2.x.482"
latestVersion = '"version": "1.1.X"'

class SerialInit():
    def __init__(self, DevName="COM7", BaudRate=115200, TimeOut=2, Write_TimeOut=1):
        # Serial takes these two parameters: serial device and baudrate
        self.DevName = DevName
        self.BaudRate = BaudRate
        self.TimeOut = TimeOut
        self.Write_TimeOut = Write_TimeOut
    # def initConnection(self):
        # initializes connection to the port passed, when the object is instantiated
        #if port isn't accsible exception is raised
        try:
            self.ser = serial.Serial(self.DevName, self.BaudRate)
            self.ser.timeout = self.TimeOut
            self.ser.write_timeout = self.Write_TimeOut
            # flash input output buffers
            self.ser.flushInput()
            self.ser.flushOutput()

        except:
            print("SerialException occurred, could not access {}, exiting application".format(self.DevName))
            sys.exit()
        print(self.DevName, self.BaudRate, self.TimeOut, self.Write_TimeOut, self.ser)

    def change_read_timeout(self,TimeOut):
        self.ser.timeout = int(TimeOut)

    def change_write_timeout(self, write_timeout):
        self.ser.timeout = int(write_timeout)

    def readUntil(self, parameter):
        # flash input output buffers
        self.ser.flushInput()
        self.ser.flushOutput()
        response = self.ser.read_until(parameter).decode('ascii')
        print(response)
        return response

    def readSingleLine(self):
        # flash input output buffers
        self.ser.flushInput()
        self.ser.flushOutput()
        input=self.ser.write(b'ls\r\n')
        # time.sleep(1)
        # response = self.ser.read(1000)
        response = self.ser.read_until(b'goal').decode('ascii')
        # response=response.rstrip()
        # line=self.ser.readline()
        # line=self.ser.read_until(b"\r")
        print(response)
        # self.ser.close()

    def readVersion(self):
        # returns the version from metadata.json on sandstone
        # flash input output buffers
        self.ser.flushInput()
        self.ser.flushOutput()
        input = self.ser.write(b'cd /sandstone/etc/\r\n')
        input = self.ser.write(b'pwd\n\r')
        response=self.ser.read(20).decode('ascii')
        # todo cat it to dictionary possible?
        input = self.ser.write(b'grep "uiVersionString" metadata.json\r\n')
        # todo need to pass the expected version after the update as in new version as a paramter or from config json file
        # todo read until uiVersionString: and n characters required to parse the version out
        # todo have some python scripts on a usb stick that may parse the metadata.json and output the version or use bash commands in .sh scripts
        time.sleep(.5)
        response = str(self.ser.read_all().decode('ascii'))
        match_response = re.search('"uiVersionString":', response)
        but_version = response[match_response.end() + 2:match_response.end() + 11]
        return but_version


    def login_check(self):
        # if the command prompt displaying login:
        # enter 'root\r\n' to loginto

        i=0
        # possible prompts for login prompt
        loginPrompts = ['login', 'Password']
        for i in range(3):
            # flash input output buffers
            # print("currently in buffer {} ".format(self.ser.inWaiting()))
            self.ser.flushInput()
            self.ser.flushOutput()
            # input <enter>
            self.ser.write(b'\r\n')
            response = self.ser.read(120).decode('ascii')
            print("this is the response:",response)
            # check if any of the login prompts declared above list are in the response string
            if any(x in response for x in loginPrompts):
                self.ser.write(b'root\r\n')
                status = True
                break
            elif ('$' in response):
                # already logged in
                print("already logged in")
                status = True
                break
            else:
                i+=1
                time.sleep(1)
                status = False
        return status
    def writePattern(self, pattern):
    #     write somethign to the port
        self.ser.flushInput()
        self.ser.flushOutput()
        self.ser.write(str(pattern+'\r\n').encode('ascii'))

    def readPattern(self, pattern, timeToWait=1):
        #     read everything until you see a pattern - a string, return True
        self.ser.flushInput()
        self.ser.flushOutput()
        # instantiate time to wait timer print timer expired if the pattern isn't found during timeToWait
        t1=threading.Timer(timeToWait, print("Timer expired"))
        t1=threading.Timer(timeToWait, print("Timer expired"))
        # keep reading line by line and checking if the pattern is present while the timer is alive
        while (True and t1.is_alive()):
            # todo may have to send enter to see the output???
            response = self.ser.readline.decode('ascii')
            if pattern in response:

                return True
                break
            else:
                return False
                pass

    def readBytes(self,byte):
        # reads specific number of bytes
        response = self.ser.read(byte).decode('ascii')
        return response

    def read_continuous(self, read_until):
        # flash the output to get rid off data in the buffer
        self.ser.flushOutput()
        # create an empty list
        data_list = []
        while True:
            time.sleep(0.01)
            if (self.ser.inWaiting()>0):
                data_str = self.ser.read(self.ser.inWaiting()).decode('ascii')
                print(data_str, end='')
                #     populate the list with every item read and append to the end of the list
                data_list.append(str(data_str))
                # check if '$' is present in the data_str - means the processing is complete todo double check this
                if read_until in data_str:
                    print('termination character is encountered, read is aborted {}'.format(data_str))
                    break
                    # continue
        return data_list



    def logOut(self):
        # exit to the login: screen
        input = self.ser.write(b'exit\r\n')
        response = self.ser.read(20).decode('ascii')


    def closeConnection(self):
        # closes the serial connection
        self.ser.close()


# # TestMethods
# serialI=SerialInit()
# # serialI.writePattern('./ImageRecognitionApplication --imageDir /media/pod_images --masterRecipe /sandstone_active/recipes/master_recipes.json --brandInfo /sandstone_active/recipes/master_brand_info.json | grep -e PodPresent -e Processing')
# # serialI.read_continuous('$')
# # # serialI.initConnection()
# # # serialI.readSingleLine()
# # serialI.login_check()
# version = serialI.readVersion()
# print(version)
# # # serialI.logOut()

