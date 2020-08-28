from Lib.Models.Log import Log
from Lib.Models.Req import Req
from Lib.Models.State import State


class EventParser:
    """
    The class distinguishes events and return parsed value.
    Ayla integration can return any type of events, this parser should help to identify the type and parse it properly.
    """
    event_type = ''

    def __init__(self, event):
        self.body = Struct(**Struct(**event).body)
        self.header = Struct(**Struct(**event).header)
        self.event_type = list(self.body.__dict__.keys())[0]

    def get_content(self):
        if self.event_type == "log":
            return Log(self.header, **self.body.log)
        elif self.event_type == "state":
            return State(self.header, **self.body.state)
        elif self.event_type == "req":
            return Req(self.header, **self.body.req)
        else:
            return False


class Struct:

    def __init__(self, **entries):
        self.__dict__.update(entries)