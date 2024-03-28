import unittest
from utils.arrs import get, my_slice

class TestArrs(unittest.TestCase):

    def test_get(self):
        # Тестирование с валидным индексом
        self.assertEqual(get([1, 2, 3], 1), 2)
        # Тестирование с невалидным индексом
        self.assertEqual(get([1, 2, 3], 3), None)
        # Тестирование с отрицательным индексом (если поддерживается)
        self.assertEqual(get([1, 2, 3], -1), 3)


    def test_my_slice(self):
        # Тестирование с начальным и конечным индексами
        self.assertEqual(my_slice([1, 2, 3, 4, 5], 1, 3), [2, 3])
        # Тестирование с начальным индексом, но без конечного
        self.assertEqual(my_slice([1, 2, 3, 4, 5], 2), [3, 4, 5])
        # Тестирование с конечным индексом, но без начального
        self.assertEqual(my_slice([1, 2, 3, 4, 5], end=3), [1, 2, 3])
        # Тестирование с отрицательными индексами
        self.assertEqual(my_slice([1, 2, 3, 4, 5], -2, -1), [4])
        # Тестирование с пустым списком
        self.assertEqual(my_slice([]), [])
