'''Created on march 4, 2022
@author: Fabricio Cordova

https://github.com/Hiyperion

Description:
    Employee class for pay calculation
'''


class Employee:
    """
    ACME employee class representation
    """

    def __init__(self, name: str, schedule: dict) -> None:
        """employee initializer

        Args:
            name (str): employee name
            schedule (dict): Employee work schedule, days of the week are the keys and the value is a list of
                            wo elements. The first element is the start hour the second element is the finish
                            work hour, using 24h format and only hours with decimals.
        """
        self.name = name
        self.schedule = schedule
        self.week_days = ["MO", "TU", "WE", "TH", "FR"]
        self.weekend = ["SA", "SU"]
        self.payment_table = [[0, 9], [9, 18], [18, 24]]

    def calculate_payment(self) -> float:
        """Calculates the total pay for the employee

        Returns:
            float: The resulting payment calculated
        """
        sueldo = 0
        for key, value in self.schedule.items():
            h_worked = self.getHoursPerSchedulePayment(value)
            if key in self.week_days:
                sueldo += h_worked[0]*25.0+h_worked[1]*15.0+h_worked[2]*20.0
            if key in self.weekend:
                sueldo += h_worked[0]*30.0+h_worked[1]*20.0+h_worked[2]*25.0
        return round(sueldo, 2)

    def getHoursPerSchedulePayment(self, partial_schedule: list) -> list:
        """Take one day schedule (known as partial_schedule) to process and obtain the number of worked hours
        in ech interval or payment rate in the payment table

        Args:
            partial_schedule (list): list of two elements, initial and final hour of work

        Returns:
            list: Three element list, each element is the number of hours worked in each interval
        """

        ll = partial_schedule[0]
        ul = partial_schedule[1]
        added_ll = False
        new_partial = [[0, 9], [9, 18], [18, 24]]
        for i in range(3):
            element = self.payment_table[i]
            if ul<=element[0]:
                new_partial[i]=[0,0]
                continue
            if ul>element[0] and ul<=element[1]:
                new_partial[i][1]=ul
            if ll>=element[0] and ll<element[1]:
                new_partial[i][0]=ll
                added_ll = True
            if not added_ll:
                new_partial[i]=[0,0]
        hours_worked = [round(el[1]-el[0], 2) for el in new_partial]
        return hours_worked