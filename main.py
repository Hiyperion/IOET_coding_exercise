from Employee import Employee
from ReaderTxt import ReaderTxt


class IOET_test():
    @staticmethod
    def run_exercise():
        """Static method for execute the each part of the aplication IOET exercise
        """
        reader = ReaderTxt("input_data.txt")
        employees_list = reader.get_file_info()
        for employee in employees_list:
            employee_pay = employee.calculate_payment()
            print(f"The amount to pay {employee.name} is: {employee_pay} USD")


if __name__ == "__main__":
    IOET_test.run_exercice()