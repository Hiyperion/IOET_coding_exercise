'''
Created on on march 4, 2022
@author: Fabricio Cordova

https://github.com/Hiyperion

Description:
    Test for the employee class

'''
import unittest
from Employee import Employee

NAME = "RENE"
SCHEDULE = {"MO":[10,12], "TU": [10,12],"TH":[1,3],"SA":[14,18],"SU":[20,21]}




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
        self.assertEqual(self.empleado.calculate_payment(),215.0)

class TestEmployeePaymentRate(unittest.TestCase):
    def setUp(self) -> None:
        self.empleado = Employee(name=NAME,schedule=SCHEDULE)
    def test_for_return_type(self):
        """Test if the return of the hours por rate payment is a list
        """
        self.assertIsInstance(self.empleado.getHoursPerSchedulePayment([1,10]),list)
    def test_get_hours_per_schedule_payment(self):
        """First case, when the work schedule is in the first interval [0.02, 9]
        """
        self.assertEqual(self.empleado.getHoursPerSchedulePayment([1,8]),[7,0,0])
    def test_get_hours_per_schedule_payment_1(self):
        """Second case, when the work schedule is in the first 2 interval [0.02, 9] [9.02,18]
        """
        self.assertEqual(self.empleado.getHoursPerSchedulePayment([1,10]),[8,1,0])
    def test_get_hours_per_schedule_payment_2(self):
        """Third case, when the work schedule is in the last interval [18.02,24]
        """
        self.assertEqual(self.empleado.getHoursPerSchedulePayment([19,23]),[0,0,4])
    def test_get_hours_per_schedule_payment_3(self):
        """Fourth case, when the work schedule is in all interval [0.02, 9] [9.02,18][18.02,24]
        """
        self.assertEqual(self.empleado.getHoursPerSchedulePayment([8,21]),[1,9,3])
if __name__ == "__main__":
    unittest.main()