#pytest


# def test_5_x_5(expected_result_5x5):
#     assert  5*5 ==expected_result_5x5
#
# def test_6_x_6():
#     assert 6*6 == 35
#
# def test_7_x_7():
#     assert 7*7 == 49

import pytest
@pytest.mark.parametrize(
    ['name','expected'],
    [
        ('name1',1),
        ('name2',2)
    ]
)
def test_func(name,expected):
    assert int(name[-1]) == expected