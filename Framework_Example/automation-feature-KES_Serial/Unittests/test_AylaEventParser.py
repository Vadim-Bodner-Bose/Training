import json

from Lib.AYLA.AylaAPIcaller import AylaAPIcaller, EventTypes
from Lib.AYLA.AylaEventParser import EventParser

log_message = json.loads('{ "header":{"seq_id":1, "timestamp":"1521730784;360;1"}, '
                         '"body":{"log":{ "message":"Error with ... ","event_id":"1521730784;360;1",'
                         '"level":"ERROR"}} '
                         '}')

state_message = json.loads('{"header": { "brew_id": 1, "seq_id": 1, "timestamp": "1521730784;360;1" }, "body": { '
                           '"state": { "brew_status": "BREW_SUCCESSFUL", "dispensed":4, "mode": { "current": '
                           '"IDLE", "change_cause": "BREW_COMPLETE_IDLE_REQUEST", "req_source": "MOBILE-APP", '
                           '"req_id": 1521730784 }}}}')

a = AylaAPIcaller()


def test_event_type():
    e = EventParser(log_message)
    assert e.event_type == "log"


def test_log_message():
    e = EventParser(log_message)
    log = e.get_content()
    assert log.message == "Error with ... "


def test_log_level():
    e = EventParser(log_message)
    log = e.get_content()
    assert log.level == "ERROR"


def test_event_type_state():
    e = EventParser(state_message)
    assert e.event_type == "state"


def test_state():
    state = a.get_device_event("AC000W001692672", EventTypes.STATE)
    assert state.brewing_status == 'BREW_SUCCESSFUL'


def test_req():
    req = a.get_device_event("AC000W001692672", EventTypes.REQ)
    assert req.cmd == 'BREW'
    assert req.recipe == {'size': 10, 'flow_rate': 7390, 'temp': 194, 'brew_type': 'NORMAL',
                          'recipe_category': 'GENERIC', 'enhanced': False}
    assert req.header.source == 'MOBILE-APP'
