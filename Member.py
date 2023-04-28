import datetime

class Member:
    def __init__(self,fname, lname,contact):
        self.fname=fname
        self.lname=lname
        self.contact=contact
        self.addmission_date=datetime.date.today()
    def get_fullname(self):
        return self.fname+" "+self.lname
    
    def get_contact(self):
        return self.contact
        