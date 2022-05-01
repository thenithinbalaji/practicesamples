## Topic : JSON
# Exercise 001

""" 
Problem Statement : 
Read the Employee.json from the file and print the employee details.

Approach :
Complete the following program and make sure the test cases in TestLab001.py passes successfully/

"""


import json


def readEmployeeFromJSONFile():
    # Write code to open the file
    f = open("Employee.json")
    
    # Load json data as python object.
    employee_data = json.load(f)

    # hint : explore json library
    f.close()
    
    return employee_data
