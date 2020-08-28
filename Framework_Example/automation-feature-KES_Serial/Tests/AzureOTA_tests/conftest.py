import pytest


def pytest_addoption(parser):
    parser.addoption("--device_id", action="store", default="test-m01-010209009BE118BC54440139")


@pytest.fixture(scope="session")
def device_id(request):
    return request.config.getoption("--device_id")
