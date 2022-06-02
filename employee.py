class Employee():
    def __init__(self,employeeid,employeename,employeeemail):
        self.employeeid=employeeid
        self.employeename=employeename
        self.employeeemail=employeeemail

    
    def get_Employeeid(self):
        return self.employeeid

    def get_Employeename(self):
        return self.employeename

    def get_Employeeemail(self):
        return self.employeeemail

    def __str__(self):
        return self.employeename
        
