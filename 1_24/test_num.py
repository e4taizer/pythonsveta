import  pytest
import logging

logging.basicConfig(
    level=logging.INFO,  # Уровень логирования
    format="%(asctime)s [%(levelname)s] %(message)s",  # Формат логов
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[

        logging.StreamHandler()  # Вывод в консоль
    ]
)

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



logger = logging.getLogger(__name__)

@pytest.mark.parametrize(

    "x,y,expected",
    [(3,4,True),
     (5,6,True),
     (150,100,False)

    ]
)
def test_compare(base_number,x, y,expected):
    logger.info(f"🔄 Запуск теста: x={x}, y={y}, base_number+x={base_number+x}")
    print(f"Тестируем с параметрами: {base_number+x}, {y}")
    try:
        result =  base_number+x >= y
        assert result == expected
        logger.info(f"✅ Тест пройден: {x+base_number} < {y} → {result} (ожидалось {expected})")

    except AssertionError:
        logger.error(f"❌ Ошибка: {x+base_number} < {y} → {result} (ожидалось {expected})")
        raise  # Поднимаем исключение для фиксации в pytest




