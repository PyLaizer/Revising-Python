#Exercise 11.3

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Test for Employee Class"""

    def setUp(self):
        self.employee_instance = Employee("Jack","William",87_000)
        # self.employee_instance.give_raise()

    def test_give_default_raise(self):
        self.assertEqual(self.employee_instance.give_raise(),92_000)

    def test_give_custom_raise(self):
        self.assertEqual(self.employee_instance.give_raise(10_000),97_000)    

if __name__ == '__main__':
    unittest.main()