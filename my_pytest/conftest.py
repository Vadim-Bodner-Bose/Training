import pytest


def pytest_addoption(parser):
    parser.addoption("--test", action="store")
    # , default="Android")


@pytest.fixture
def test(request):
    print("input paramter {}".format(request.config.getoption('--test')))
    return request.config.getoption("--test")

