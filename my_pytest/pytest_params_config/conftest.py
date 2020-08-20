import pytest
import my_pytest.pytest_params_config.BREWER_CONFIG
import configparser


# def pytest_configure(config, platform):
#     print("setup")
#     print (platform)
from my_pytest.pytest_params_config import BREWER_CONFIG


def pytest_addoption(parser):
    parser.addoption("--platform", action="store", default='test1')


@pytest.fixture
def platform(request):
    config = configparser.ConfigParser()
    config.read(BREWER_CONFIG)
    print(BREWER_CONFIG.sections())
    return request.config.getoption("--platform")
