
# IOET coding exercise solution

![Python Versions][pyversion-button]

[pyversion-button]: https://img.shields.io/badge/Python-3.9-brightgreen

This code is a solution for the applying process for the Python developer position at [ioet](https://www.ioet.com/about-us)

## How to run
To see the solution, only run the file main.py, there is the main class of the project. Inside this class, the program calls the other classes to obtain the desired results.  It is necessary that all files are in the same folder. 

## Classes description
- IOET_test.- the main class with one static method that is used to call the other classes and get the final result, this class is present in the main file. 
- ReaderTxt.- This class allows getting the employees' information from the input data. The singleton pattern is used to implement this class.  The principal method allows getting a list of Employees objects from the input_data.txt file
- Employee.- This class represents each employee, has two attributes, the employee name (string) and the employee schedule (dict). The keys in the schedule dict  are the weekdays and the values are lists with two elements, the first one is the start work hour and the second is the end work hour.  Also, Employee has one main method, calculated_payment, that returns the payment of the Employee. 

## Unit test description
The only external library used in this project is [unittest](https://docs.python.org/3/library/unittest.html).
This program was developed using TDD methodology. For that exist, two test files: test_for_employee.py and test_for_reader.py to test Employee and ReaderTxt classes. 

The   test_for_employee.py mainly allows testing the payment calculation output using an equal assert.  In this test exist 7 tests for the Employee's methods and input cases. 

test_for_reader.py allows testing the ReaderTxt methods. Mainly, the tests are focused on the return type and the correct function of the secondary methods.  Exist 4 Test in this section. 

## Solution Overview

First, it is necessary to obtain the data from the text file, for this the ReaderTxt class is used. Here the file is read line by line, each line corresponds to an employee. For each line, the name of the employee is separated from the schedule, both are strings. The schedule is processed separating it by days, the two first elements are the abbreviation that is used as the key of a new dictionary element. The value corresponding to that key is the return of "intervaleTolist", which takes a string of the type '10:30-11:45' and returns a list with the start and end time in decimal format, namely [10.5,11.75]. At the end of this process, each employee has a name and a schedule.
With the employee's name and schedule, I can create an instance of the Employee class and added it to a list of employees that will be returned.

In the main file, for each employee in the employee list, the algorithm calls the calculate_payment method.  Before making the payment calculation, first is necessary to get the number of hours that the employee works in each rate schedule  (cost table); for this, the getHoursPerSchedulePaument method is used.  This method takes the two elements list of day schedule and after a process, the algorithm gets a list of three elements, each element is the number of hours worked in the corresponding rate table. For example, if the input is [8,21] the output is [1,9,3], which means the employee work 1 hour at the 00:01 - 09:00  interval, 9 hours at 09:01 - 18:00  interval, and 3 hours at 18:01 - 00:00 interval.


After this, the algorithm just prints the output in the specified format.


