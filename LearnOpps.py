from datetime import datetime
class employee:
    employees = 0 
    salary = 10000
    def __init__(self,name,phno,mailid,dob):
        self.name = name
        self.phno = phno
        self.mailid = mailid
        self.dob = dob
        employee.employees +=1
        print(f"His Salary is : {self.salary}\n")


    def bio(self):
        print(f"\nName : {self.name}\nMobile Number : {self.phno}\nMail ID : {self.mailid}\nAge : {self.age}")
        print(f"His Salary is : {self.salary}")
    def vayasu(self):
        Current_yr = datetime.now().year
        self.age = Current_yr-self.dob
        print(f"His Salary is : {self.salary}")                                                                                                                                                                                                              
    
   
    def test(self,b):
        employee.salary += b
        

per1 = employee("ganesh",9360206902,"ganesh@mail.com",2005)
per2 = employee("suresh",9360206901,"suresh@mail.com",2004)
per3 = employee("ramesh",9360206912,"ramesh@mail.com",1999)
per4 = employee("raja",9360206921,"raja@mail.com",2000)

employee.test(1,10)

per1.vayasu()
per2.vayasu()
per3.vayasu()
per4.vayasu()
employee.test(1,10)
per1.bio()
per2.bio()
per3.bio()
per4.bio()

print(f"\nTotal Employee's : {employee.employees}")

