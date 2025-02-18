import unittest
from datetime import datetime
from src.gui.gui_main import process_input


class TestGuiMain(unittest.TestCase):
    def test_process_input_valid(self):
        """Тестирование process_input с корректными данными"""
        result = process_input("John Doe", "01.01.2000")
        self.assertEqual(result, ("John Doe", datetime(2000, 1, 1).date()))

    def test_process_input_invalid_date(self):
        """Тестирование process_input с некорректной датой"""
        with self.assertRaises(ValueError):
            process_input("John Doe", "invalid_date")

    def test_process_input_empty_name(self):
        """Тестирование process_input с пустым именем"""
        with self.assertRaises(ValueError):
            process_input("", "01.01.2000")


if __name__ == "__main__":
    unittest.main()
