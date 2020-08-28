import json
import time
import logging

from Lib.AYLA.AylaEventParser import EventParser
from Lib.RequestsWrapper import RequestsWrapper
from Config.Ayla_Config import API_URL, APP_ID, APP_SECRET, EMAIL, PASSWORD, LOGIN_URL


class EventTypes(enumerate):
    STATE = "state"
    REQ = "req"
    LID_RECOG = "lid_recog"
    HOST_V = "host_v"
    IMG_RECOG = "img_recog"
    LOG = "log"
    SW_INFO = "sw_info"


class AylaAPIcaller():
    requests_wrapper = RequestsWrapper()
    token = None

    def __init__(self):
        """         Ayla authetication        """
        payload = json.dumps({"user": {"password": PASSWORD,
                                       "application": {"app_id": APP_ID, "app_secret": APP_SECRET}, "email": EMAIL}})
        request = self.requests_wrapper.post_request(LOGIN_URL, payload, None)
        response = json.loads(request)
        self.token = response["access_token"]

    def get_device_status(self, dsn):
        """       The method returns current connectivity status        """
        url = API_URL + dsn
        request = self.requests_wrapper.get_request(url, self.token)
        return json.loads(request)["device"]["connection_status"]

    def get_device_event(self, dsn, event):
        """    The method returns the latest event    """
        time.sleep(2)
        url = API_URL + dsn + "/properties/" + event
        request = self.requests_wrapper.get_request(url, self.token)
        event = json.loads(json.loads(request)["property"]["value"])
        logging.warning("event is: {}".format(event))
        return EventParser(event).get_content()

    def send_event(self, dsn, event, data):
        """   The method posts event to ayla datapoint   """
        url = API_URL + dsn + "/properties/" + event + "/datapoints"
        payload = json.dumps({
            "datapoint": {
                "value": str(data)
            }
        })
        return self.requests_wrapper.post_request(url, payload, self.token)
