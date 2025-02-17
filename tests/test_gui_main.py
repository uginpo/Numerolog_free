from src.gui.gui_main import enter_data, validate_date
import unittest
from unittest.mock import patch
from datetime import datetime


# Теперь можно импортировать src


class TestGuiMain(unittest.TestCase):
    def test_validate_date_valid(self):
        """Тестирование валидации даты с корректными данными"""
        date_str = "01.01.2000"
        expected_date = datetime.strptime(date_str, '%d.%m.%Y').date()
        self.assertEqual(validate_date(date_str), expected_date)

    def test_validate_date_invalid(self):
        """Тестирование валидации даты с некорректными данными"""
        with self.assertRaises(ValueError):
            validate_date("invalid_date")

    @patch("tkinter.Tk")
    @patch("tkinter.Entry")
    @patch("tkinter.Label")
    @patch("tkinter.Button")
    def test_enter_data_valid_input(self, mock_button, mock_label, mock_entry, mock_tk):
        """Тестирование enter_data с корректными данными"""
        entry_date = mock_entry.return_value
        entry_name = mock_entry.return_value
        entry_date.get.return_value = "01.01.2000"
        entry_name.get.return_value = "John Doe"

        root = mock_tk.return_value
        root.mainloop.side_effect = lambda: root.quit()

        result = enter_data()
        self.assertEqual(result, ("John Doe", datetime(2000, 1, 1).date()))


if __name__ == "__main__":
    unittest.main()
