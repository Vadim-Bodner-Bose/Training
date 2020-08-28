"""
Library wrapper used for all things Xray/Jira.

"""
import json
import ast
import base64
import inspect
import os
import datetime
import logging

from Config.Global_Config import URL, AUTH

from Lib.RequestsWrapper import RequestsWrapper
from Utils.DateTime import DateTime as Time


class JiraInformation:
    """
    Class gathering all information needed to report to proper xray test plans/sets/cases/steps
    """
    def __init__(self, test_plan, summary):
        """
        Class initialization
        Constructor creates new test execution. Link it with passed test plan
        And adds all test cases from the test plan to the test execution.
        """
        summary += ' %s' % str(datetime.datetime.now())

        self.requests_wrapper = RequestsWrapper()
        self.test_case_id = {}
        self.test_exec_key = None
        self.test_cases = []
        self.__create_test_exec(summary, test_plan)
        self.__add_exec_to_plan(test_plan)
        self.__get_all_cases_from_test_plan(test_plan)
        self.__get_test_case_id()

    # Private method
    def __create_test_exec(self, summary, test_plan):
        """
        Sends POST request to get test execution ID

        """
        project_id = ""
        if "TM" in test_plan:
            project_id = "15201"    # TM project id. It is static value for the project
        elif "KP" in test_plan:
            project_id = "13000"    # KP project id

        logging.warning("Create Test execution")
        url = "%s/rest/api/2/issue" % URL
        payload = json.dumps({"fields": {"project": {"id": project_id}, "summary": summary,
                                         "description": "Test Automation Execution", "issuetype": {"id": "13104"}}})
        request = self.requests_wrapper.post_request(url, payload, AUTH)
        response = json.loads(request.decode('utf-8'))
        self.test_exec_key = response["key"]
        logging.warning(response)
        logging.warning("Test execution has been created, key: %s" % self.test_exec_key)

    # Private method
    def __add_test_cases(self, test_cases):
        """
        Sends a POST request to xray to create test set and get the ID

        """
        logging.warning("Assign test cases to the test execution")
        url = "%s/rest/raven/1.0/api/testexec/%s/test" % (URL, self.test_exec_key)
        payload = json.dumps({"add": test_cases})
        request = self.requests_wrapper.post_request(url, payload, AUTH)
        logging.warning(request.decode("utf-8"))

    # Private method
    def __add_exec_to_plan(self, test_plan):
        """
        Add test execution to test plan

        """
        logging.warning("Link Test execution with Test plan")
        url = "%s/rest/raven/1.0/api/testplan/%s/testexecution" % (URL, test_plan)
        payload = json.dumps({"add": ["%s" % self.test_exec_key]})
        request = self.requests_wrapper.post_request(url, payload, AUTH)
        response = json.loads(request.decode('utf-8'))
        logging.warning(response)

    # Private method
    def __get_all_cases_from_test_plan(self, test_plan):
        """
        Get All test cases from the test plan
        """
        logging.warning("Get all test cases from the test plan")
        url = "%s/rest/raven/1.0/api/testplan/%s/test" % (URL, test_plan)
        request = self.requests_wrapper.get_request(url, AUTH)
        response = json.loads(request.decode('utf-8'))
        for i in response:
            self.test_cases.append(i['key'])
        self.__add_test_cases(self.test_cases)
        logging.warning(self.test_cases)

    # Private method
    def __get_test_case_id(self):
        """
        sends a GET request to xray to get test case ID
        Each test cases in test execution has two ID's
        Test case KEY - static value like 'TM-410'
        Test case ID - dynamic value is unique for each test execution. It is used for test result reporting.
        """
        logging.warning("Collect all test case ID's from the test execution")
        url = "%s/rest/raven/1.0/api/testexec/%s/test" % (URL, self.test_exec_key)
        request = self.requests_wrapper.get_request(url, AUTH)
        response = request.decode('utf-8')
        test_list = ast.literal_eval(response)
        for i in test_list:
            data = dict(i)
            self.test_case_id[data["key"]] = data["id"]
        logging.warning(self.test_case_id)

    def set_test_status(self, test_case_key, status):
        """
        Sets the test case status in xray
        """
        logging.warning("Set test status = %s for test case = %s" % (status, test_case_key))
        for key in self.test_case_id:
            if test_case_key in key:
                test_case_id = self.test_case_id[key]
                break
            else:
                continue

        url = "%s/rest/raven/1.0/api/testrun/%s/status?status=%s" % \
              (URL, test_case_id, status)
        payload = {}
        response = self.requests_wrapper.put_request(url, payload, AUTH)

    def set_comment(self, test_case_key, comment):
        """
        Sends comment for test case to  xray
        """
        logging.warning("Post a comment for test case %s" % test_case_key)
        for key in self.test_case_id:
            if test_case_key in key:
                test_case_id = self.test_case_id[key]
                break
            else:
                continue

        url = "%s/rest/raven/1.0/api/testrun/%s/comment" % (URL, test_case_id)
        req = self.requests_wrapper.put_request(url, comment, AUTH)
        response = req.decode('utf-8')

    def post_screenshot(self, test_case_key, image):
        """
        Send screenshot in base64 format to xray
        """
        logging.warning("Post a screenshot for test case %s" % test_case_key)
        if os.path.exists(image):
            with open(image, "rb") as image_file:
                image_base64 = base64.b64encode(image_file.read())
                image.close()
        else:
            image_base64 = image
            image = 'image_' + Time.get_current_datetime()

        for key in self.test_case_id:
            if test_case_key in key:
                test_case_id = self.test_case_id[key]
                break
            else:
                continue
        url = "%s/rest/raven/1.0/api/testrun/%s/attachment" % (URL, test_case_id)
        payload = json.dumps({"data": image_base64, "filename": image, "contentType": "image/png"})
        try:
            response = self.requests_wrapper.post_request(url, payload, AUTH)
        except Exception as ex:
            logging.warning("Oops! Screenshot is not posted to Xray!!!")
            logging.warning("Exception: " + repr(ex))

    @staticmethod
    def get_func_name():
        test_case = inspect.stack()[1].function
        test_case_num = "TM-" + test_case.strip("test_")
        return test_case_num
