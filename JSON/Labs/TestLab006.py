
import unittest
from Lab006 import readEmployeeFromJSONFile


class TestLab006(unittest.TestCase):
    def test_Employee(self):
        employee_data = readEmployeeFromJSONFile()
        print(employee_data.name)
        # add for other fields also
        self.assertEqual(employee_data.name,
                         "Raj", "Employee Name not matching.")
        self.assertEqual(employee_data.age,
                         30, "Employee Age not matching.")
        self.assertEqual(employee_data.dept,
                         "IT", "Employee Dept not matching.")
        self.assertEqual(employee_data.id,
                         52896, "Employee ID  not matching.")

if __name__ == '__main__':
    unittest.main()
