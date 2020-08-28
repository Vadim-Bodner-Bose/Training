#######################################
# BrewerFWload.py
# version 0.40
#######################################
import re
import sys
import serial
import threading 
import time
import os
import dlipower
from Automation_Tools_Hardware.Web_Power_Switch import Web_Power_Switch
from File_Classes import JSON

stopRun = False
def callTimeout():
    global stopRun
    stopRun = True
    logMsg("exit by timeout, rebooting the brewer")
    # power_switch_cycle()
    wps.switch_off(port=1, time_to_sleep=5)
    wps.switch_on(port=1, time_to_sleep=0)
    os._exit(1)  #kill the main thread

# # # # # # # # # # # # # #
# todo read this from the json later if we decide to use this switch for now ok to leave hardcoded
js = JSON()
power_switch = js.get_json_paramter('premium', 'power_switch')
hostname = power_switch['hostname']
userid = power_switch['userid']
password = power_switch['password']

# hostname = '192.168.0.100'
# userid = 'admin'
# password = '1234'

wps = Web_Power_Switch(hostname, userid, password)
# # # # # # # # # # # # # #


# def power_switch_cycle():
#     # power cycle the brewer
#     print('Connecting to a DLI PowerSwitch at 192.168.0.100')
#     switch = dlipower.PowerSwitch(hostname="192.168.0.100", userid="admin", password='1234')
#
#     print('Turning off the first outlet')
#     switch.off(1)
#     time.sleep(5)
#     print('Turning on the first outlet')
#     switch.on(1)
    

#-----------------------------------------------------
#  Function: terminateScript()
#  Desc: Consistant controled exit from script
#-----------------------------------------------------
def terminateScript(exitCode):
    logMsg("====================================================\n");
    logMsg("ending " + sys.argv[0] + " script\n")
    # removing logging
    # logFile.close()
    sys.exit(exitCode)

#-----------------------------------------------------
#  Function: logMsg()
#  Desc: Provides feedback in the form of screen and
#        logfile messages.
#-----------------------------------------------------
pythonfilename = sys.argv[0]
logfilename = pythonfilename.replace('.py', '_') + time.strftime('%Y%m%d') + time.strftime('%H%M%S') + '.log'

# removing logging
# try:
#     logFile = open(logfilename,"w")
# except Exception as e:
#     print ("Exception: Opening Logs.txt: " + str(e))
#     terminateScript(1)
    

def logMsg(feedback):
    print(feedback)
    # # removing logging
    # logFile.write(feedback + "\n")

logMsg("Starting " + sys.argv[0] + " script\n")
logMsg("====================================================\n");
#-----------------------------------------------------
#  Function: trapErrors()
#  Desc: Detects & responds to errors in strline based
#        upon those defined for errorType
#-----------------------------------------------------
def trapErrors(strline, errorType):
    print(str(errorType) + " " + strline)

def verifyReply(cmdType, command, rdData):
    #process the output in readData
    readData = str(rdData)
    if (cmdType =="single") and "New Mode: Quad I/O Read Mode (4-byte Addr)" in readData:
        logMsg("Complete execute " + command)
        return
    #elif (cmdType == "usb_enable") and "scanning bus 0 for devices... 3 USB Device(s) found" in readData:
    elif (cmdType == "usb_enable") and "3 USB Device(s) found" in readData:
        logMsg("Complete execute " + command)
        return
    elif (cmdType == "usb") and "reading " in readData:
        logMsg("Complete execute " + command)
        return
    elif (cmdType == "probe") and "SF: Detected " in readData:
        logMsg("Complete execute " + command)
        return
    elif (cmdType == "erase") and "Erased: OK" in readData:
        logMsg("Complete execute " + command)
        return
    elif (cmdType == "write" ) and "Written: OK" in readData:
        logMsg("Complete execute " + command)
        return
    else:
        logMsg("output data:   ")
        logMsg(str(readData))
        logMsg("Error: uncomplete execute " + command) 
        #trapErrors(strline, errorType)
        exit(1)
#-----------------------------------------------------
#  Function: sendCmnd()
#  Desc: Writes the command argument out to the 
#        usbPort and waits on "=>\n"
#        All output between the command echo 'til
#        the "=>\n" is logged.
#
# Note:    The following error was observed 11/13 JMG
#    "=> 
#      qspi@single
#     Unknown command 'qspi@single' - try 'help'
#     =>"
#       The script was ran again without change and
#     the proper qspi single command was sent and 
#     processed correctly.
#-----------------------------------------------------
def sendCmnd(command):
    # replace the package name with the name passed from test_Update script
    command = command.replace("programmingPackage", sys.argv[3])
    global stopRun
    if usbPort.isOpen() != True:
        try:
            logMsg("*** re-openning usbPort ***")
            usbPort.open()
        except Exception as e:
            logMsg("Exception: Opening serial port: " + str(e))
            sys.exit(1)

    logMsg("**** Sending |" + command + "|")
    cmndType = ("-----", "usb_enable", "probe", "erase", "write")
    cmndReply = ""
    # todo add if command is run usb_enable cycle the drop for the usb hub
    for index in range(0, len(cmndType)):
        if cmndType[index] in command:
            errorType = index
            break
        else:
            errorType = 0
        if command == 'run usb_enable':
            # cycle usb port
            # power cycle the usb-hub
            wps.switch_off(port=2, time_to_sleep=5)
            wps.switch_on(port=2, time_to_sleep=7)
        else:
            break

    try:
        for char in command:
            # print(char)
            usbPort.write(char.encode('ascii'))
            time.sleep(0.05) #too quick to cause mistranslte?
        usbPort.write("\r".encode('ascii'))
    except Exception as e:
        logMsg("Error sending command " + command + ": " + str(e))
        sys.exit(1)
    words = command.split() # convert the command to a list
    _, currentcmdType, *_ = words  #unpacking 
    strline = " "
    usbPort.timeout = 100
    readData = []
    timer = threading.Timer(200.0, callTimeout) #200 seconds for timeout
    timer.start() 
    while True:
        try:
            charRet = usbPort.read(1)
            if (len(charRet) < 1):
                logMsg("No Char?")
                print(bool(stopRun))
                if (stopRun) :
                    logMsg("exit here")
                    sys.exit(1)
                continue
            cmndReply = cmndReply + str(charRet.decode("utf-8"))
        except  Exception as e:
            logMsg("Exception: During read :")
            logMsg("Exception Msg: " + str(e))
            logMsg("On command: " + command)
            # sys.exit(1)    Rather than exit on an exception during a read
            #              insert a '~' and proceed
            #                If the command going out was affected then you
            #              should be able to trap than in trapError()
            #              ...and if it wasn't then the commands have been 
            #              sent out correctly and there's no reason to stop
            cmndReply = cmndReply + chr(0x7E)
        prompt = chr(61)                        # '='
        prompt = prompt + str(chr(62) + " ")    # '>' 
        
        if (len(cmndReply) != 0):
            if cmndReply.endswith("\r\n"):
                #readData.append(cmndReply)
                strline = cmndReply.rstrip(chr(13)) # trim trailing '/n'
                strline = cmndReply.rstrip(chr(10)) # trim trailing '/r'
                readData.append(strline)
                #print("strline...")
                logMsg(strline)
                #trapErrors(strline, errorType)
                strline = ""
                cmndReply = ""            
                #timer.cancel()  
            timer.cancel()  
            if (len(cmndReply) == 3):
                if (prompt[0] == cmndReply[0]) and (prompt[1] == cmndReply[1]) and (prompt[2] == cmndReply[2]):
                #if (cmndReply == "=> "):
                    verifyReply(currentcmdType, command, readData)
                    break
            timer = threading.Timer(200.0, callTimeout) #200 seconds for timeout
            timer.start()
#-----------------------------------------------------
# Make sure that the user invoked the script correctly
#-----------------------------------------------------
if len(sys.argv) != 4:
    print ("\n\n\n\n\n\n\n\n\n\n")
    print ("     Usage:                                                 ")
    print ("             BrewerFWload <command file name> <serial port> <package name>")
    print ("                                                            ")
    print ("     eg:     BrewerFWload commands.txt COM1 programmingPackage                 ")
    print ("\n\n\n\n\n\n\n\n\n\n")
    print ("====================================================\n");
    print ("ending " + sys.argv[0] + " script\n")
    sys.exit(1)
#  print ("")

#-----------------------------------------------------
# Open the file to use as a log file
#-----------------------------------------------------
# try:
    # logFile = open("Logs.txt","w")
# except Exception as e:
    # print ("Exception: Opening Logs.txt: " + str(e))
    # terminateScript(1)



for index in range(0, len(sys.argv)):                 # index from 0 to index < len(sys.argv)
  logMsg("Argument[" + str(index) + "]: " + sys.argv[index])
#  print("Argument[", index, "]: ", sys.argv[index])

#-----------------------------------------------------
# Open command file and read commands
# sys.argv[1] - path to the file with the file name
#-----------------------------------------------------
def loadInputFile():

    try:
        fileObj = open (sys.argv[1], "r")
    except Exception as e:
        logMsg("Exception: Opening command file: " + str(e))
        terminateScript(1)

    fcontent = fileObj.read()
    fileObj.close()          # Close the file you're done with
    

#-----------------------------------------------------
# Process command file and construct commands list
#-----------------------------------------------------
    index = 0
    start = index
    cmndCount = 0
    commands = []
    for char in fcontent:      # Step through the file char by char
        if (char == chr(10)):    # Split the data by '/n' characters, chr(10) returns '/n'
            subStr = fcontent[start:index];
            start = index + 1
            #-----------------------------------------------------
            # Eliminate lines that start with '#' (comment lines)
            # Eliminate lines that are just whitespace characters
            # Eliminate zero length lines
            #-----------------------------------------------------
            if ((subStr[0:1] != "#") and (subStr.isspace() != True) and (len(subStr)!=0)):
                subStr = subStr.rstrip()              # Remove trailing spaces
                if (subStr !=  "run xsa_boot"):        #exclude command line run xsa_boot
                    commands.append(subStr)               # load commands List
                    cmndCount = cmndCount + 1
        index = index + 1
    
    logMsg("There are " + str(cmndCount) + " commands in the list.")
    logMsg("------------------------------------------------------\n");
    for index in range(0,cmndCount):
        logMsg(str(index+1) + ") " + commands[index])
    logMsg("------------------------------------------------------\n");
    return cmndCount, commands

cmndCount, commands = loadInputFile()


def openThePort(port):

    logMsg("\nOpennig Serial Port " + sys.argv[2] + ".")

######################################################
# Openning Serial port to the brewer
######################################################
    usbPort = serial.Serial(port, 115200)

#-----------------------------------------------------
# Configure for 8/None/and 1 config.   No flow control
#-----------------------------------------------------
    usbPort.bytesize   = serial.EIGHTBITS       #number of bits per bytes
    usbPort.parity     = serial.PARITY_NONE     #set parity check: no parity
    usbPort.stopbits   = serial.STOPBITS_ONE    #number of stop bits
    usbPort.xonxoff    = False                  #disable software flow control
    usbPort.rtscts     = False                  #disable hardware (RTS/CTS) flow control
    usbPort.dsrdtr     = False                  #disable hardware (DSR/DTR) flow control

#-----------------------------------------------------
# Timeouts
#-----------------------------------------------------
    usbPort.timeout      = 120                             #set a 2 min read
    usbPort.writeTimeout = 1                               #timeout for write

#-----------------------------------------------------
#   Make sure the serial port is closed before you 
# try to open it.
#-----------------------------------------------------
    try:
        usbPort.close()
    except Exception as e:
        logMsg("Exception: Base lining serial port: " + str(e))
        terminateScript(1)
    
    try:
        usbPort.open()
    except Exception as e:
        logMsg("Exception: Opening serial port: " + str(e))
        terminateScript(1)
    return usbPort

port = sys.argv[2]
usbPort = openThePort(port)

# cycle usb port
# power cycle the usb-hub
# wps.switch_off(port=2,time_to_sleep=5)
# wps.switch_on(port=2,time_to_sleep=5)
# power cycle
wps.switch_off(port=1,time_to_sleep=5)
wps.switch_on(port=1,time_to_sleep=0)

def setBootMood(usbPort):
#response = " "
#-----------------------------------------------------
# Drop to boot mode
#-----------------------------------------------------
    if usbPort.isOpen():
        try:
            usbPort.flushInput()
            usbPort.flushOutput()
            numberOfLine = 0                             # Weak approach
            while True:
                response = " "
                try:
                    response = usbPort.readline().decode('ascii')
                    usbPort.timeout = 1
                except  Exception as e:       # Captures the static on the line
                    msg = str(e)[0:31]        # when the brewer is first powered on.
                    if (msg == "'ascii' codec can't decode byte"):
                       logMsg(chr(0x7E))
                    else:
                       logMsg(msg)
                strline = response.rstrip(chr(10)) # trim any trailing '/n'
                logMsg(strline)
                retval = usbPort.write(" ".encode('ascii'))
                prompt = chr(61)                        # '='
                prompt = prompt + str(chr(62) + " ")    # '>'
                if (response[0] == '='):
                    if (prompt[0] == response[0]) and (prompt[1] == response[1]) and (prompt[2] == response[2]):
                        break
                numberOfLine = numberOfLine + 1
                if (numberOfLine >= 100):
                    break
            if (numberOfLine >= 100):
                logMsg("Error: Failed to drop to BOOT mode.")
                terminateScript(1)
        except Exception as e:
            logMsg("Error communicating...: " + str(e))
            terminateScript(1)
    else:
        logMsg("Cannot open serial port.")
        terminateScript(1)

setBootMood(usbPort)
#-----------------------------------------------------
#-----------------------------------------------------
for index in range(0, cmndCount):
    sendCmnd(commands[index])

#-----------------------------------------------------
#-----------------------------------------------------
logMsg("\n" + "The End")


time.sleep(5)
# close the serial connection power cycle the usb-hub
usbPort.close()
wps.switch_off(port=2,time_to_sleep=5)
wps.switch_on(port=2,time_to_sleep=5)
time.sleep(5)
# cycle the brewer
# power_switch_cycle()
wps.switch_off(port=1,time_to_sleep=5)
wps.switch_on(port=1,time_to_sleep=5)

# exit the script
terminateScript(0)


