import pytest

@pytest.fixture(scope='module')
def expected_result_5x5():
    return 25
@pytest.fixture
def base_number():
    return 10

import logging

# def pytest_configure():
#     logging.basicConfig(
#         filename="pytest.log",
#         level=logging.INFO,
#         format="%(asctime)s - %(levelname)s - %(message)s",
#         datefmt="%Y-%m-%d %H:%M:%S",
#     )