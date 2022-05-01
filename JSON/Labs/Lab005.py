## Topic : JSON
# Exercise 005

""" 
Problem Statement : 
Ehnance the Employee.json with Project details as an ARRAY of objects inside Employee.
Each Project can have attributes as
1) name (String)
2) tenure (int)
3) is_internal (boolean)

# hint : this is based on Lab 004's solution.

Approach :
Complete the following program and make sure the test cases in TestLab005.py passes successfully/

"""

import json


def readEmployeeFromJSONFile():
    # Write code to open the file
    f = open("Employee.json")
    # Load json data as python object.
    employee_data = json.load(f)
    f.close()
    return employee_data