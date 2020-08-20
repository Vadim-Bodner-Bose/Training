# content of conftest.py
import pytest
class params:
    platform = "Android1"
    dsn = 'A12345'

def pytest_addoption(parser):
    parser.addoption("--platform", action="store", default=params.platform)
    parser.addoption("--dsn", action="store", default=params.dsn)



@pytest.fixture
def platform(request):
    return request.config.getoption("--platform")

@pytest.fixture
def dsn(request):
    return request.config.getoption("--dsn")