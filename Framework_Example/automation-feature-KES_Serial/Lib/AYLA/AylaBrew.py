"""
Library handles remote brewing through Ayla
"""

import json
import time
from datetime import datetime
from Lib.AYLA.AylaAPIcaller import AylaAPIcaller, EventTypes

class AylaRemoteBrew:
    """
    Class is a wrapper for requests calls for reporting to Xray.
    """

    def __init__(self):
        """
        Class initialization
        """
        self.aylaAPI = AylaAPIcaller()

    def execute_req(self, dsn, cmd):
        timestamp = str(datetime.timestamp(datetime.now()))
        if cmd == "Brew":
            data = json.dumps({"datapoint": {"value": {"body": {"req": {"id": 1564169424,"cmd": "BREW", "recipe":
                {"size": 4, "brew_type": "NORMAL", "temp": 160, "flow_rate": 7390, "enhanced": "false",
                 "recipe_category": "MASTER"}}}}, "header":
                {"timestamp": timestamp + ";-240;1", "source": "MOBILE-APP"}}})
        elif cmd == "Cancel":
            data = json.dumps({"datapoint": {"value": {"body": {"req": {"id": 1564169424, "cmd": "CANCEL_BREW", "recipe":{"size": 12, "brew_type": "NORMAL", "temp": 160, "flow_rate": 7390, "enhanced": "false", "recipe_category": "MASTER"}}}, "header": {"timestamp": timestamp + ";-240;1", "source": "MOBILE-APP"}}}})
        elif cmd == "PowerOff":
            data = json.dumps({"datapoint": {"value": {"body": {"req": {"id":1584971682,"cmd": "STANDBY"},
                                            "header": {"timestamp": timestamp + ";-240;1", "source": "MOBILE-APP"}}}}})
        elif cmd == "PowerOn":
            data = json.dumps({"datapoint":{"value": {"body": {"req": {"id":1584971682, "cmd": "IDLE"},
                                            "header": {"timestamp": timestamp + ";-240;1", "source": "MOBILE-APP"}}}}})
        else:
            raise AssertionError("Command not recognized... (TODO: give list of proper commands in error message)")
        response = self.aylaAPI.send_event(dsn, EventTypes.REQ, data)
        print(response)
        time.sleep(10)
        ret_state = self.aylaAPI.get_device_event(dsn, EventTypes.STATE)
        return ret_state

    def execute_brew(self, dsn):
        ret_state = self.execute_req(dsn, "Brew")
        if ret_state is None:
            # print("Cannot get the state for Brew")
            status = "Fail"
        else:
            if "BREW_IN_PROGRESS" in str(ret_state):
                # print("brew in BREW_IN_PROGRESS state as expected")
                time.sleep(60)
                ret_state = self.aylaAPI.get_device_event(dsn, EventTypes.STATE)
                if ret_state is None:
                    # print("Cannot get the state for Brew")
                    status = "Fail"
                else:
                    if "BREW_SUCCESSFUL" in str(ret_state):
                        # print("brew in BREW_SUCCESSFUL state as expected")
                        status = "Pass"
                    else:
                        status = "Fail"
            else:
                status = "Fail"
        return status

    def execute_brew_cancel(self, dsn):
        ret_state = self.execute_req(dsn, "Brew")
        if ret_state is None:
            # print("Cannot get the state for Brew")
            status = "Fail"
        else:
            if "BREW_IN_PROGRESS" in str(ret_state):
                # print("brew in BREW_IN_PROGRESS state as expected")
                # print("waiting for 20 seconds...")
                time.sleep(20)
                ret_state = self.execute_req(dsn, "Cancel")
                time.sleep(60)
                ret_state = self.aylaAPI.get_device_event(dsn, EventTypes.STATE)
                if ret_state is None:
                    # print("Cannot get the state for Brew")
                    status = "Fail"
                else:
                    if "BREW_CANCELLED" in str(ret_state):
                        # print("brew in BREW_SUCCESSFUL state as expected")
                        status = "Pass"
                    else:
                        status = "Fail"
            else:
                status = "Fail"
        return status

    def execute_power_on_off(self, dsn):
        ret_state = self.execute_req(dsn, "PowerOff")
        if ret_state is None:
            # print("Cannot get the state for Power off")
            status = "Fail"
        else:
            if "STANDBY" in str(ret_state):
                # print("PASSED: brewer in Standby state as expected")
                ret_state = self.execute_req(dsn, "PowerOn")
                if ret_state is None:
                    # print("Cannot get the state for Power on")
                    status = "Fail"
                else:
                    if "IDLE" in str(ret_state):
                        # print("PASSED: brewer in Idle state as expected")
                        status = "Pass"
                    else:
                        status = "Fail"
            else:
                status = "Fail"
        return status