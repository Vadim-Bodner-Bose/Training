import pytest


def pytest_addoption(parser):
    parser.addoption("--exp", action="store", default="5")


@pytest.fixture(scope='function')
def example(request):
    # specific precondition can be passed here
    example_var = request.config.getoption("--exp")
    print(" \n function beginning")
    yield example_var
    print(" \n function finalizing")


@pytest.fixture(scope='session')
def example2(request):
    # specific precondition can be passed here
    print(" \n session beginning")

    def fin():                 # Finalizing statement implementation #1
        print(" \n session finalizing")
    request.addfinalizer(fin)


@pytest.fixture(scope='module')
def example3(request):
    # specific precondition can be passed here
    print(" \n module beginning")
    yield                       # Finalizing statement implementation #2
    print(" \n module finalizing")
