from Lib.JiraXrayIntegration import JiraInformation

"""
Initialize Xray object, Create test execution and link it with plan and cases.
Check test cases list 
"""


def test_create_exec_with_all_tc():
    xray = JiraInformation("TM-2000", "Test Execution Summary")
    assert xray.test_cases == ['TM-414', 'TM-436']

