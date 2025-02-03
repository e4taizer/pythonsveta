import pytest

@pytest.fixture(scope='module')
def expected_result_5x5():
    return 25
@pytest.fixture
def base_number():
    return 10