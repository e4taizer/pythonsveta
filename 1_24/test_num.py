import  pytest
import logging
logging.basicConfig(level=logging.DEBUG)
# def test_addition():
#     assert 2 + 2 == 4
#
#
# def test_subtraction():
#     assert 5 - 3 == 2
#
#
# def test_6_x_6():
#     assert 6 * 6 == 35
#
#
# def test_7_x_7():
#     assert 7 * 7 == 49



def test_my_function(caplog):
    logger = logging.getLogger(__name__)
    logger.warning("Это предупреждение!")

    # Проверка, что предупреждение было записано
    assert "Это предупреждение!" in caplog.text

@pytest.mark.parametrize(

    "x,y",
    [(3,4),
     (5,6),
     (150,100)

    ]
)
def test_compare(base_number,x, y):
    print(f"Тестируем с параметрами: {base_number+x}, {y}")
    assert base_number+y >= x

logger = logging.getLogger(__name__)

@pytest.mark.parametrize("x, y", [(1, 2), (3, 4)])
def test_example(x, y):
    logger.info(f"Тестируем с параметрами: {x}, {y}")
    assert x < y
