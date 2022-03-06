'''
Created on march 5, 2022
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
    """Tests for the Reader class
    """
    def setUp(self) -> None:
        self.reader = ReaderTxt(file_name=FILE_NAME)
    def test_return_type(self):
        """Test if the return fot the method is a list
        """
        self.assertIsInstance(self.reader.get_file_info(),list)
    def test_return_list_elements(self):
        """Test if each element in the list is a employee
        """
        for element in self.reader.get_file_info():
            self.assertIsInstance(element,Employee)
    def test_interval_to_schedule_list(self):
        """Test if the intervaleTolist method works correctly
        """
        self.assertEqual(self.reader.intervaleTolist("10:30-21:45"),[10.50,21.75])
    def test_interval_to_schedule_list_2(self):
        """Test if the intervaleTolist method works correctly for the case when 00:00 refers to the finish hour
        """
        self.assertEqual(self.reader.intervaleTolist("18:00-00:00"),[18.0,24.0])

if __name__ == "__main__":
    unittest.main()

