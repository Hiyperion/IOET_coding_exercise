'''
Created on sábado, 5 de marzo de 2022
@author: Fabricio Cordova

https://github.com/Hiyperion

Description:
    Test for text reader class
'''
import unittest
from Employee import Employee
from ReaderTxt import ReaderTxt

FILE_NAME = "input_data.txt"


class TestReader(unittest.TestCase):
    def setUp(self) -> None:
        self.reader = ReaderTxt(file_name=FILE_NAME)
    def test_return_type(self):
        self.assertIsInstance(self.reader.get_file_info(),list)
    def test_return_list_elements(self):
        for element in self.reader.get_file_info():
            self.assertIsInstance(element,Employee)
    def test_interval_to_schedule_list(self):
        self.assertEqual(self.reader.intervaleTolist("10:30-21:45"),[10.50,21.75])

if __name__ == "__main__":
    unittest.main()

