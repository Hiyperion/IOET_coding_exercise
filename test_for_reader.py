'''
Created on sábado, 5 de marzo de 2022
@author: Fabricio Cordova

https://github.com/Hiyperion

Description:
    Test for text reader class
'''
import unittest
from ReaderTxt import ReaderTxt

FILE_NAME = "input_data.txt"


class TestReader(unittest.TestCase):
    def setUp(self) -> None:
        self.reader = ReaderTxt(file_name=FILE_NAME)
    def test_return_type(self):
        self.assertIsInstance(self.reader.readFile(),list)

if __name__ == "__main__":
    unittest.main()

