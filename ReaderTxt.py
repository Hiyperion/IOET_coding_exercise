'''
Created on sábado, 5 de marzo de 2022
@author: Fabricio Cordova

https://github.com/Hiyperion

Description:
    Class for generate a list of employees from a txt

'''


from Employee import Employee

def singleton(cls):
    instances = dict()
    def wrap(*args,**kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrap
@singleton
class ReaderTxt:
    def __init__(self, file_name) -> None:
        self.file_name = file_name
    def get_file_info(self) -> list:
        """Read the input txt file and process the string to get a list of employees
        Returns:
            list: each element is a Employee object
        """
        employe_list=[]
        with open(self.file_name) as file:#TODO: should convert the hour in 00:00 format to a decimal format
            for dat in file.readlines():
                employee_schedule=dict()
                dat_= dat.rstrip("\n")
                dat_= dat_.split("=")
                employee_name = dat_[0]
                for day_sched in dat_[1].split(","):
                    employee_schedule[day_sched[0:2]]=self.intervaleTolist(day_sched[2:])
                employee = Employee(name=employee_name,schedule=employee_schedule)
                employe_list.append(employee)


        return employe_list
    @staticmethod
    def intervaleTolist( day_sch:str) -> list:
        """Transform the employee schedule string into a list, each 00:00 hour is convert to a decimal representation
            10:30  =  10.5
        Args:
            day_sch (str): string with the schedule, similar to '10:30-11:45'

        Returns:
            list: has two elements, each element is the decimal representation of the hour in the day_sch
        """
        ll,ul = day_sch.split("-")
        ent,dec=[float(el) for el in ll.split(":")]
        ent_u,dec_u=[float(el) for el in ul.split(":")]
        return [round(ent+dec/60,2),round(ent_u+dec_u/60,2)]