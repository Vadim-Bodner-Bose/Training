import pytest


def pytest_addoption(parser):

    parser.addoption("--test", action="store", default="Android")


@pytest.fixture
def test(request):

    return request.config.getoption("--test")

