import asyncio
import datetime
import json
import time
import websockets
from Lib.AYLA.AylaEventParser import EventParser
from Config.Ayla_Config import WSS_URL
"""
The class connects to existing socket on Ayla side and collect log events for selected devices. 
"""


class WebsocketClient:
    def __init__(self, property, expected, timer):
        self.logdict = {}
        self.status = ''
        self.property = property
        self.expected = expected
        self.timer = timer

    async def eventCollector(self, dsn, streamKey):
        """
        Prepare dictionary of result logs. Each dsn has array of json events
        """
        for x in dsn:
            self.logdict = {x: []}
            flag = {x: 0}
        startTime = time.perf_counter()
        launchTime = datetime.datetime(*time.gmtime(time.time())[:6])
        url = WSS_URL + streamKey
        """
        Open socket connection and collecting events, one by one.
        """
        async with websockets.connect(url) as websocket:
            while True:
                response = await websocket.recv()
                if '|Z' in response:
                    await websocket.send('Z')
                else:
                    print(response)
                    event = json.loads(response.split('|', 2)[1])
                    self.timesliser(event, launchTime)
                    """
                    This part checks status for all brewers. Socket connection will be closed in two cases:
                    1. Test received expected event for All brewers
                    2. Or Time limit will be exceeded. 
                    """
                    for key, value in self.logdict.items():
                        for event in value:
                            e = EventParser(event)
                            if e.event_type == self.property:
                                if e.get_content().message == self.expected:
                                    flag[key] = 1
                    if sum(flag.values()) == len(flag):
                        self.status = 'PASS'
                        break
                if (time.perf_counter() - startTime) >= self.timer:
                    self.status = 'FAIL'
                    print("Time Out Fail")
                    break

    """Method Runner"""
    def eventCaller(self, dsn, streamKey):
        asyncio.get_event_loop().run_until_complete(self.eventCollector(dsn, streamKey))

    """  The logic collects All events generated after test start. """
    def timesliser(self,event, launchTime):
        if datetime.datetime.strptime(event["datapoint"]["created_at"], '%Y-%m-%dT%H:%M:%SZ') > launchTime:
            data = json.loads(event["datapoint"]["value"])
            self.logdict[event["metadata"]["dsn"]].append(data)