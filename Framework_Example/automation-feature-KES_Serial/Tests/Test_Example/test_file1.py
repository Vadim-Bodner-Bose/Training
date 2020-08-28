import pytest


@pytest.mark.TM_14
def test_method1_TM_14(example):
    pytest.global_response = pytest.global_response.__add__('Test string will be added to the jira comment #1\n')
    assert True
    assert example == 10


@pytest.mark.TM_15
def test_method2_TM_15(example):
    pytest.global_response = pytest.global_response.__add__('Test string will be added to the jira comment #2\n')
    assert True
    assert example == 9


@pytest.mark.unbound
def test_method2_TM_242():
    assert True