import unittest
from customer import Customer
from employee import Employee

class CustomerTest(unittest.TestCase):
    def setUp(self):
        self.c=Customer(123, 'Will', 'william.anderson2@seattle.colleges.edu')

    def test_Id(self):
            self.assertEqual(self.c.get_Customerid(), 123)
    
    def test_name(self):
            self.assertEqual(self.c.get_Customername(), 'Will' )

    def test_email(self):
            self.assertEqual(self.c.get_Customeremail(), 'william.anderson2@seattle.colleges.edu' )


class EmployeeTest(unittest.TestCase):
    def setUp(self):
        self.c=Employee(1234, 'Mike', 'mike2@seattle.colleges.edu')

    def test_Id(self):
            self.assertEqual(self.c.get_Employeeid(), 1234)
    
    def test_name(self):
            self.assertEqual(self.c.get_Employeename(), 'Mike' )

    def test_email(self):
            self.assertEqual(self.c.get_Employeeemail(), 'mike2@seattle.colleges.edu' )




        
            

        


