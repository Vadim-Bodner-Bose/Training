import pytest


def pytest_addoption(parser):
    parser.addoption("--dsn", action="store", default="AC000W006145676")
    parser.addoption("--ver", action="store", default="fake_update")
    parser.addoption("--oem_model", action="store", default="kpremiumus-reg")
    parser.addoption("--filePath", action="store", default="C:/sup_K115_1.1.1.121_encrypted.run")
    parser.addoption("--socketid", action="store", default="86760494d2d34d4f92d145274f975637")


@pytest.fixture(scope="module")
def dsn(request):
    return request.config.getoption("--dsn")


@pytest.fixture(scope="module")
def ver(request):
    return request.config.getoption("--ver")


@pytest.fixture(scope="module")
def oem_model(request):
    return request.config.getoption("--oem_model")


@pytest.fixture(scope="module")
def filePath(request):
    return request.config.getoption("--filePath")


@pytest.fixture(scope="module")
def socketid(request):
    return request.config.getoption("--socketid")

