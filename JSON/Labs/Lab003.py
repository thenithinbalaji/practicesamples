## Topic : JSON
# Exercise 003

""" 
Problem Statement : 
Read the Employee.json from the file and print the employee details.
Try to add another attributes
1)   "manager" with any String value
2)   "yearsofexp" with any integer value


Approach :
Complete the following program and make sure the test cases in TestLab003.py passes successfully/

"""


import json


def readEmployeeFromJSONFile():
    # Write code to open the file
    f = open("Employee.json")
    
    # Load json data as python object.
    employee_data = json.load(f)
    
    # hint : explore json library
    employee_data['manager'] = 'Alice'
    employee_data['yearsofexp'] = 5

    # update dictionary to have new attributes
    #employee_data = dict.copy()
    f.close()
    
    return employee_data
