import json
from Lib.RequestsWrapper import RequestsWrapper
from Config.Ayla_Config import OTA_URL, ICC_URL
from Lib.AYLA.AylaAPIcaller import AylaAPIcaller


class AylaOTA:
    """
    Class gathering all information needed to report to proper xray test plans/sets/cases/steps
    Step 0: Get Ayla auth token
    Step 1: Create a Host Image
    Step 2: Upload your image binary file
    Step 3: Create a Filter for target devices
    Step 4: Create a Job with the Filter you created
    Step 5: Set the OTA action to the Job (using the host image "version" and "type" you created in Step 1)
    Step 6: Start the Job
    """

    def __init__(self, dsn, version, model):
        """
        Class initialization
        """
        self.dsn = dsn
        self.version = version
        self.model = model
        self.oem = '1adffb61'
        self.requests_wrapper = RequestsWrapper()
        self.token = AylaAPIcaller().token
        self.filter_id = None
        self.job_id = None

    def start_ota(self, filepath):
        self.__create_host_image()
        self.__upload_image(filepath)
        self.__create_device_filter()
        self.__create_ota_job()
        self.__set_ota_action()
        self.__start_job()

    def clean_up_ota(self):
        self.__cancel_job()
        self.__delete_job()
        self.__delete_host_image()
        self.__delete_device_filter()


    def __create_host_image(self):
        """
        The method is creating Host MCU image
        """
        print("Function start: create_host_image") #Will be replaced by logger
        payload = json.dumps({"model": self.model,
                              "oem": self.oem,
                              "version": self.version,
                              "description": "God blesses brave automation!"})
        request = self.requests_wrapper.post_request(OTA_URL, payload, self.token)
        response = json.loads(request)
        print("""Response payload: %s \n
        Function finish: create_host_image""" % response) #Will be replaced by logger

    def __upload_image(self, filepath):
        """
        The method is loading Host MCU image file
        """
        print("Function start: upload_image") #Will be replaced by logger
        url = "{0}/{1}/image/upload?oem={2}&version={3}".format(OTA_URL, self.model, self.oem, self.version)
        files = [
            ('file', open(filepath, 'rb'))
        ]
        self.requests_wrapper.post_request_file(url, self.token, files)
        print("Function finish: upload_image") #Will be replaced by logger

    def __create_device_filter(self):
        """
        The method is creating a filter for devices what will be updated.
        """
        print("Function start: create_device_filter") #Will be replaced by logger
        url = "{0}filters".format(ICC_URL)
        payload = json.dumps({"name": "Test Automation Filter Name",
                                "oem_model": self.model,
                                "dsns": {
                                    "match": self.dsn
                                }
                            })
        request = self.requests_wrapper.post_request(url, payload, self.token)
        response = json.loads(request)
        self.filter_id = response["id"]
        print("""Response payload: %s \n
        Function finish: create_device_filter""" % response) #Will be replaced by logger

    def __create_ota_job(self):
        """
         The method create a Job with the Filter you created
        """
        print("Function start: create_ota_job") #Will be replaced by logger
        url = "{0}jobs".format(ICC_URL)
        payload = json.dumps({
                                "exec_method": "ONE_TIME",
                                "filter_id": self.filter_id,
                                "name": "OTA Test Automation job 1",
                                "type_id": 4
                            })
        request = self.requests_wrapper.post_request(url, payload, self.token)
        response = json.loads(request)
        self.job_id = response["id"]
        print("""Response payload: %s \n
        Function finish: create_ota_job""" % response) #Will be replaced by logger

    def __set_ota_action(self):
        """
         The method set the OTA action to the Job
        """
        print("Function start: set_ota_action") #Will be replaced by logger
        url = "{0}jobs/{1}/ota".format(ICC_URL, self.job_id)
        payload = json.dumps({
                            "type": "host",
                            "version": self.version,
                            "description": "God blesses brave actions!"
                        })
        request = self.requests_wrapper.post_request(url, payload, self.token)
        response = json.loads(request)
        print("""Response payload: %s \n
        Function finish: set_ota_action""" % response) #Will be replaced by logger

    def __start_job(self):
        """
        The method starts the OTA job
        """
        print("Function start: start_job") #Will be replaced by logger
        url = "{0}jobs/{1}/start".format(ICC_URL, self.job_id)
        payload = json.dumps({})
        self.requests_wrapper.post_request(url, payload, self.token)
        print("Function finish: start_job \n") #Will be replaced by logger

    def __cancel_job(self):
        """
        The method cancels the OTA job
        """
        print("Function start: cancel_job") #Will be replaced by logger
        url = "{0}jobs/{1}/cancel".format(ICC_URL, self.job_id)
        payload = json.dumps({})
        self.requests_wrapper.post_request(url, payload, self.token)
        print("Function finish: cancel_job \n") #Will be replaced by logger

    def __delete_job(self):
        """
        The method deletes stopped ota job
        """
        print("Function start: delete_job") #Will be replaced by logger
        url = "{0}jobs/{1}".format(ICC_URL, self.job_id)
        self.requests_wrapper.delete_request(url, self.token)
        print("Function finish: delete_job \n") #Will be replaced by logger

    def __delete_host_image(self):
        """
        The method is deleting Host MCU image
        """
        print("Function start: delete_host_image") #Will be replaced by logger
        url = "{0}{1}/image/upload?oem={2}&version={3}".format(OTA_URL, self.model, self.oem, self.version)
        self.requests_wrapper.delete_request(url, self.token)
        print("Function finish: delete_host_image") #Will be replaced by logger

    def __delete_device_filter(self):
        """
        The method is deleting a filter for devices what will be updated.
        """
        print("Function start: delete_device_filter") #Will be replaced by logger
        url = "{0}filters/{1}".format(ICC_URL, self.filter_id)
        self.requests_wrapper.delete_request(url, self.token)
        print("Function finish: delete_device_filter") #Will be replaced by logger