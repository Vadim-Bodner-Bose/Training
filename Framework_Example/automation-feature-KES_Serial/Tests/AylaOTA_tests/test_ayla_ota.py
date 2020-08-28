import pytest
from Lib.AYLA.AylaOTAapi import AylaOTA
from Lib.AYLA.AylaEventParser import EventParser
from Lib.AYLA.WebsocketClient import WebsocketClient
from Lib.GLOBALS.CLOUD_EVENTS import AYLA_OTA_LOG

#pytest -s test_ayla_ota.py --testscope ayla_ota --dsn AC000W006145676 --ver v.1 --oem_model kpremiumus-reg --filePath C:/sup_K115_1.1.1.121_encrypted.run --socketid 59b7fde6fc174cf6a58b236899b94ceb

@pytest.mark.TM_414
def test_ayla_ota_update(dsn, ver, oem_model, filePath, socketid):
        dsns = dsn.split(',')
        ayla = AylaOTA(dsns, ver, oem_model)
        ayla.start_ota(filePath)

        socketConnection = WebsocketClient("log", AYLA_OTA_LOG, 3600)
        socketConnection.eventCaller(dsns, socketid)

        assert socketConnection.status == "PASS"

        """Function to print logs as a comment for Xray. TODO: Rebuild and unify """
        comment = ''
        for key, value in socketConnection.logdict.items():
                comment = comment + "Brewer " + key+":\n"
                for log in value:
                        e = EventParser(log)
                        if e.event_type == "log":
                                comment = comment + "Log event: " + log["header"]["timestamp"] + " : " + log["body"]["log"]["message"] + "\n"
        print(comment)
        pytest.global_response = pytest.global_response.__add__(comment)

        ayla.clean_up_ota()
