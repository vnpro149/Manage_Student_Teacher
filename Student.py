from Member import Member

class Student(Member):
    def __init__(self, fname, lname, contact,classname):
        super().__init__(fname, lname, contact)
        self.classname=classname
        self.email="{}{}.st.vnpro.org".format(self.fname,self.lname)
    
    def student_data(self):
        student={}
        student['fname']=self.fname
        student['lname']=self.lname
        student['contact']=self.contact
        student['classname']=self.classname
        student['admission_date']=self.addmission_date
        student['email']=self.email
        return student



#JSON: {key:value}

#Dictionary: {key:value}

