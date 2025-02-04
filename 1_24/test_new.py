import pytest
import logging

# Настройка логирования в файл и консоль
logging.basicConfig(
    level=logging.INFO,  # Уровень логирования
    format="%(asctime)s [%(levelname)s] %(message)s",  # Формат логов
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler("test_log.txt"),  # Запись в файл
        logging.StreamHandler()  # Вывод в консоль
    ]
)

# Создаем логгер
logger = logging.getLogger(__name__)


@pytest.mark.parametrize(
    "x, y, expected",
    [
        (2, 3, True),
        (5, 1, False),
        (10, 10, False),
        (7, 8, True)
    ]
)
def test_compare(x, y, expected):
    """Проверяет, что x меньше y"""

    logger.info(f"🔄 Запуск теста: x={x}, y={y}, expected={expected}")

    try:
        result = x < y
        assert result == expected
        logger.info(f"✅ Тест пройден: {x} < {y} → {result} (ожидалось {expected})")
    except AssertionError:
        logger.error(f"❌ Ошибка: {x} < {y} → {result} (ожидалось {expected})")
        raise  # Поднимаем исключение для фиксации в pytest