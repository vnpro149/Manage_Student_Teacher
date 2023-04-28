from Member import Member
from Student import Student
import json

# a=Student("Tran","Chien",123456789,"Tong hop")
# data=a.student_data()
# print("Type Data:")
# print(type(data))
# print("Data:")
# print(json.dumps(data,indent=4,default=str))
Students=[]

def InputStudent():
    fname=input("Nhap Fname:")
    lname=input("Nhap Lname:")
    contact=input("Nhap Contact:")
    classname=input("Nhap Classname:")
    a=Student(fname,lname,contact,classname)
    Students.append(a)

def update_data():
    index=0
    for st in Students:
        print("{}.{}".format(index,st.student_data()))
        index+=1
    index=int(input("Nhap index hoc vien can thay doi:"))
    fname=input("Nhap Fname:")
    lname=input("Nhap Lname:")
    contact=input("Nhap Contact:")
    classname=input("Nhap Classname:")
    a=Student(fname,lname,contact,classname)
    Students[index]=a
def DelStudent():
    index=0
    for st in Students:
        print("{}.{}".format(index,st.student_data()))
        index+=1
    index=int(input("Nhap index hoc vien can xoa:"))
    Students.pop(index)

if __name__=="__main__":
    InputStudent()
    update_data()
    #DelStudent()
    print(Students[0].student_data())