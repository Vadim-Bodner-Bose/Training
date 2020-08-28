import pytest

# python -m  pytest -s Tests\Test_Example\ --testplan TM-3179 --summary Test_Exec --exp 10
# pytest -s Tests\Test_Example\ --testscope example --exp 10
# pytest -s --testscope example --exp 10
# pytest -v -m unbound

@pytest.mark.TM_16
def test_method1_TM_16(example):
    pytest.global_response = pytest.global_response.__add__('Test string will be added to the jira comment #3 %s\n' %
                                                            pytest.test_case_key)
    pytest.global_response = pytest.global_response.__add__('Test string will be added to the jira \n')
    pytest.global_response = pytest.global_response.__add__('Test string will be added to the jira \n')
    pytest.global_response = pytest.global_response.__add__('Test string will be added to the jira \n')
    pytest.global_response = pytest.global_response.__add__('Test string will be added to the jira \n')
    assert 2 == 2
    assert int(example) == 10

@pytest.mark.TM_22
def test_method2_TM_22():
    pytest.global_response = pytest.global_response.__add__('Test string will be added to the jira comment #4 %s\n' %
                                                            pytest.test_case_key)
    assert 4 == 4

@pytest.mark.TM_2216
def test_method3_TM_2216(example2, example3, example):
    pytest.global_response = pytest.global_response.__add__('Test string will be added to the jira comment #4\n')
    assert 5 == 5