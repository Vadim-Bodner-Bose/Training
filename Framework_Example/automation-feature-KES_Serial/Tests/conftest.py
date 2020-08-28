import pytest
from Lib.JiraXrayIntegration import JiraInformation
from Config.Global_Config import TEST_SCOPE

unbound = "unbound"


def pytest_addoption(parser):
    parser.addoption("--testscope", action="store", default=unbound)


@pytest.fixture(scope="session")
def test_plan_lookup(request):
    var = request.config.getoption("--testscope")
    if var != unbound:
        scope = TEST_SCOPE.get(var, "Invalid test scope was passed as a parameter")
        if isinstance(scope, tuple):
            return scope
        else:
            raise ValueError(scope)
    else:
        return False


@pytest.fixture(scope="session")
def xray(test_plan_lookup):
    """
    Pass Xray object to test
    """
    if test_plan_lookup:
        pytest.xray_object = JiraInformation(*test_plan_lookup)
    else:
        pytest.xray_object = False
    return pytest.xray_object


# Skip Test_Cases not in the Test_Plan
# Format Returned by xray.test_cases is TM-2316, thus the test name should be named the same, the reason tm is there,
# We might have KP tests also as we are currently using both projects
# Also the fixture set python variables test_case_key and global_response
@pytest.fixture(autouse=True, scope="function")
def skip_by_platform(request, xray):
    flag = False
    pytest.global_response = ''
    if isinstance(xray, bool):
        case_list = (unbound,)
    else:
        case_list = xray.test_cases
    for test_case in case_list:
        marker = request.node.get_closest_marker(test_case.replace('-', '_'))
        if marker:
            pytest.test_case_key = test_case
            flag = True
    if not flag:
        pytest.skip("%s test is not in test plan scope" % request.node.name)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Test result handler:
    Once test is over it logs all the test comments and test status
    Also it cleaning all the tests logs before and after each test started
    """
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed and not isinstance(pytest.xray_object, bool):
        pytest.global_response = pytest.global_response.__add__('\nTEST FAILED: {}'.format(rep.longrepr))
        pytest.xray_object.set_test_status(pytest.test_case_key, "FAIL")
        pytest.xray_object.set_comment(pytest.test_case_key, pytest.global_response)
    elif rep.when == 'call' and not rep.failed and not isinstance(pytest.xray_object, bool):
        pytest.xray_object.set_test_status(pytest.test_case_key, "PASS")
        pytest.xray_object.set_comment(pytest.test_case_key, pytest.global_response)
