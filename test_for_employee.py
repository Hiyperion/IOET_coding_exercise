'''
Created on viernes, 4 de marzo de 2022
@author: Fabricio Cordova

https://github.com/Hiyperion

Description:
    Test for the employee class

'''

# NAME = "RENE"
NAME = "KURT"
# SCHEDULE = {"MO":[10,12], "TU": [10,12],"TH":[1,3],"SA":[14,18],"SU":[20,21]}
SCHEDULE = {"MO":[1,10], "TU": [7,18],"WE":[10,22],"TH":[19,23],"FR":[8,21]}

import unittest
from Employee import Employee

class TestEmployeePayment(unittest.TestCase):
    """Test for the calculate_payment method in Employee
    """
    def setUp(self) -> None:
        self.empleado = Employee(name=NAME,schedule=SCHEDULE)
    def test_for_return_type(self):
        """Test if the return of the calculation is a float
        """
        self.assertIsInstance(self.empleado.calculate_payment(),float)
    def test_payment_calculation(self):
        """Test if the calculated payment is correct
        """
        self.assertEqual(self.empleado.calculate_payment(),900.0)

class TestEmployeePaymentRate(unittest.TestCase):
    def setUp(self) -> None:
        self.empleado = Employee(name=NAME,schedule=SCHEDULE)
    def test_for_return_type(self):
        """Test if the return of the hours por rate payment is a list
        """
        self.assertIsInstance(self.empleado.getHoursPerSchedulePayment([1,10]),list)
    def test_get_hours_per_schedule_payment(self):
        self.assertEqual(self.empleado.getHoursPerSchedulePayment([8,21]),[1,9,3])
if __name__ == "__main__":
    unittest.main()