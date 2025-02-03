import  pytest
import logging

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


@pytest.mark.parametrize(

    "x,y",
    [(3,4),
     (5,6),
     (3,3)

    ]
)
def test_compare(base_number,x, y):
    print(f"Тестируем с параметрами: {base_number+x}, {y}")
    assert base_number+y >= x


def test_example():
    logging.basicConfig(level=logging.INFO)  # Установите уровень логирования в INFO
    logging.info("Запущен тест test_example")
    logging.warning("Это предупреждение")
    logging.error("Ошибка")
    assert 2 + 2 == 5