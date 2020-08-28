import time

from Lib.AZURE.AzureIoTHubConfigurationHelper import AzureIoTHuBHelper
from Lib.AZURE.GetIoTHubQuery import GetIoTHubQuery
from Lib.GLOBALS.CLOUD_EVENTS import AZURE_OTA_SUCCESS


class AzureOTAupdate:

    #"valik_ota_test", "test-m01-010209009BE118BC54440139"
    def __init__(self, config_id, device_id):
        self.azure = AzureIoTHuBHelper(config_id, device_id)
        self.getQuery = GetIoTHubQuery()
        self.device_id = device_id
        self.config_id = config_id
        #Apply OTA update
        print("Apply Config for OTA")
        self.azure.set_IoTHub_configuration()

    def check_desired_twin(self):
        print("Desired property checker")
        query = "SELECT properties.desired.c2dXfer_%s FROM devices where deviceId = '%s'" % (self.config_id,
                                                                                             self.device_id)
        return self.waiter(query, self.azure.data)

    def check_reported_twin(self):
        print("Reported property checker")
        query = "SELECT properties.reported.c2dXfer_%s FROM devices where deviceId = '%s'" % (self.config_id,
                                                                                              self.device_id)
        return self.waiter(query, AZURE_OTA_SUCCESS)

    def roll_back_azure_config(self):
        print("Clean up twin and Hub config")
        self.azure.remove_IoTHub_configuration()

    def waiter(self, query, expected):
        start_time = time.perf_counter()
        i = 1
        while True:
            print("Attempt #%s" % i)
            result = self.getQuery.get_query_result(query)
            if result is not None:
                print(result[0])
                if result[0] == expected:                     # Current implementation works with single brewer only
                    print("Match Found!")
                    return True
            elif (time.perf_counter() - start_time) >= 1200:
                print("Time Out Fail")
                return False
            i += 1
            time.sleep(20)

