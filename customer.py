class Customer():
    def __init__(self, customerid, customername,customeremail):
        self.customerid=customerid
        self.customername=customername
        self.customeremail=customeremail

    
    def get_Customerid(self):
        return self.customerid

    def get_Customername(self):
        return self.customername

    def get_Customeremail(self):
        return self.customeremail

    def __str__(self):
        return self.customername 
