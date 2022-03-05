'''Created on viernes, 4 de marzo de 2022
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
            schedule (dict): emplee work schedule, days of the week are the keys and the value is a list of two elements,
                            the first element is the start hour the second element is the finish work hour, using 24h format  and only hours with decimals
        """
        self.name = name
        self.schedule = schedule
        self.week_days = ["MO","TU","WE","TH","FR"]
        self.weekend = ["SA","SU"]
        self.payment_table=[[0.02,9],[9.02,18],[18.02,24]]

    def calculate_payment(self) -> float:
        """Calculates the total pay for the employee

        Returns:
            float: the resulting payment calculated
        """
        for key,value in self.schedule.items():
            if key in self.week_days:
                pass
        # pass
    def getHoursPerSchedulePayment(self,partial_schedule:list) ->list:
        """Take one day schedule (known as partial_schedule) to process and obtain the number of worked hours
        in ech interval or payment rate in the payment table

        Args:
            partial_schedule (list): list of two elements, initial and final hour of work

        Returns:
            list: Three element list, each element is the number of hours worked in each interval
        """

        ll=partial_schedule[0]
        ul=partial_schedule[1]

        new_partial = [[0, 0], [0, 0], [0, 0]]
        
        for i in range(3):
            element=self.payment_table[i]
            if ll > element[0] and ll < element[1]:#TODO: comprobar los intervalos cerrados
                new_partial[i][0]=ll
            else:
                new_partial[i][0]=element[0]
            if ul > element[0] and ul < element[1]:
                new_partial[i][1]=ul
            else:
                new_partial[i][1]=element[1]
        print(new_partial)
