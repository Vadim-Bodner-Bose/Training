from Lib.JiraXrayIntegration import JiraInformation

xray = JiraInformation("TM-45", "SUMMARY")
""" 
Class constructor is creating new test execution
Link it with the test plan 
Add all cases from the plan to the test execution
And Gathers all Test Case keys and ID's needed for mapping tests results to tests being ran  
"""


def test_47():
    if 2 == 2:
        xray.set_test_status(xray.get_func_name(), "PASS")  # Reports Test Case result to corresponding Xray test case
    else:
        pass


def test_258():
    if 2 == 3:
        pass
    else:
        xray.set_test_status(xray.get_func_name(), "FAIL")
        xray.set_comment(xray.get_func_name(), "The answer to question M is: B")

