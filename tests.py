import unittest
from ref import (Manufacturer, Part, get_parts_and_manufacturers, get_manufacturers_and_employees, get_manufacturer_parts_count, ManufacturerEmployee, defaultdict, Employee)
class TestMyModule(unittest.TestCase):

    def test_get_parts_and_manufacturers(self):
        manufacturers = [Manufacturer(1, "Производитель А"), Manufacturer(2, "Производитель Б")]
        parts = [Part(1, "Деталь Аор", 1), Part(2, "Деталь Бор", 2), Part(3, "Деталь С", 1)]
        expected = [('Деталь Аор', 'Производитель А'), ('Деталь Бор', 'Производитель Б')]
        self.assertEqual(get_parts_and_manufacturers(parts, manufacturers), expected)

    def test_get_manufacturer_parts_count(self):
        parts = [Part(1, "Деталь 1", 1), Part(2, "Деталь 2", 1), Part(3, "Деталь 3", 2)]
        expected = defaultdict(int, {1: 2, 2: 1})
        self.assertEqual(get_manufacturer_parts_count(parts), expected)

    def test_get_manufacturers_and_employees(self):
        manufacturers = [Manufacturer(1, "К завод"), Manufacturer(2, "Технопром")]
        employees = [Employee(1, "Иван"), Employee(2, "Петр")]
        manufacturer_employees = [ManufacturerEmployee(1, 1), ManufacturerEmployee(2, 2)]
        expected = [('К завод', ['Иван'])]
        self.assertEqual(get_manufacturers_and_employees(manufacturers, employees, manufacturer_employees), expected)

if __name__ == '__main__':
    unittest.main()