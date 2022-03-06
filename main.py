'''
Created on march 5, 2022
@author: Fabricio Cordova

https://github.com/Hiyperion

Descripcion:
    Main code for the IOET test solution
'''
from Employee import Employee
from ReaderTxt import ReaderTxt


class IOET_test():
    """Main class
    """
    @staticmethod
    def run_exercise():
        """Static method for executing each part of the application IOET exercise
        """
        reader = ReaderTxt("input_data.txt")
        employees_list = reader.get_file_info()
        for employee in employees_list:
            employee_pay = employee.calculate_payment()
            print(f"The amount to pay {employee.name} is: {employee_pay} USD")


if __name__ == "__main__":
    IOET_test.run_exercise()