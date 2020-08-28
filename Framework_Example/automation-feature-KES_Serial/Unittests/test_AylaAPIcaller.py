import json
from Lib.AYLA.AylaAPIcaller import AylaAPIcaller, EventTypes


a = AylaAPIcaller()
log_message = json.dumps({"header": {"seq_id": 1, "timestamp": "1521730784;360;1"}, "body": {"log": {"message": "Error with ... ", "event_id":"1521730784;360;1", "level": "ERROR"}}})


def test_device_status():
    status = a.get_device_status("AC000W001692672")
    assert status == "Offline"


def test_sent_n_get_event():
    b = a.send_event("AC000W001692672", EventTypes.LOG, log_message)
    event = a.get_device_event("AC000W001692672", EventTypes.LOG)
    expected_message = json.loads(log_message)
    assert event.message == expected_message["body"]["log"]["message"]


def test_fail2():
    assert True
