from RestRef import *
import requests
import unittest
from types import SimpleNamespace
'''
Problem Statement : 
Call the REST API to GET the Employee details and print all the employee details in json format.

Approach :
Complete the code to fetch all employees data by calling the GET employees API.
And make sure the test case passes successfully.
Hints:
Use json, requests modules.
Refer RestRef file for code usage & references
'''


def getAllEmployees():

    # Use request module to call a GET REST API for employees
    response = requests.get("http://localhost:8080/employees")
    # print the response content
    print(response)
    # use json.dumps to convert response into string
    print(json.dumps(response.json(), indent=4))
    # refer reference to convert json string into a python object
    employeeObject = json.loads(json.dumps(response.json()), object_hook=lambda d: SimpleNamespace(**d))
    # print all employee details
    # for example like response._embedded.employees[0].firstName
    print(employeeObject._embedded.employees[0].firstName)
    print(employeeObject._embedded.employees[1].firstName)
    # return the object
    return employeeObject


class TestLab09(unittest.TestCase):

    def test_AllEmployees(self):
        employee_data = getAllEmployees()
        print(len(employee_data._embedded.employees))
        self.assertEqual(len(employee_data._embedded.employees),
                         2, "Employee list length not matching.")


if __name__ == '__main__':
    unittest.main()
