import dlipower
import time

class Web_Power_Switch():
    def __init__(self, hostname, userid, password):
        # initialize connection to the switch: hostname, userid and password come from the test_config_json
        self.hostname = hostname
        self.userid = userid
        self.password = password
        try:
            self.switch = dlipower.PowerSwitch(hostname= self.hostname, userid=self.userid, password=self.password)
        except:
            print("Connection to the switch cannot be established")

    def switch_on(self, port, time_to_sleep):
        # define the port to turn on and delay (s) after the switch is on.
        print('Turning on outlet {}'.format(port))
        self.switch.on(port)
        time.sleep(time_to_sleep)

    def switch_off(self, port, time_to_sleep):
        # define the port to turn on and delay (s) after the switch is on.
        print('Turning off the outlet {}'.format(port))
        self.switch.off(port)
        time.sleep(time_to_sleep)


# # test
# hostname = '192.168.0.100'
# userid = 'admin'
# password = '1234'
#
# wps = Web_Power_Switch(hostname, userid, password)
#
# wps.switch_on(port=1,time_to_sleep=2)
# wps.switch_off(port=1,time_to_sleep=0)
# print("Done")