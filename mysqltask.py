import mysql.connector 

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="",
  database="studdetails"
)


class StudDetails :
        
       
      mycursor = mydb.cursor()
      def Biodata(self,name,age,dob,dept,year) :
        self.x = (name,age,dob,dept,year)
        sql ="insert into biodata (name,age,dob,dept,year) values(%s,%s,%s,%s,%s)"
        values=(self.x)
        self.mycursor.execute(sql,values)
        mydb.commit()



obj = StudDetails()
i=0
while i<2:
    obj.Biodata(
    name=input("Enter Your Name : "),
    age=input("Enter Your Age : "),
    dob=input("Enter Your Date Of Birth : "),
    dept=input("Enter Your Departmant : "),
    year=input("Enter Your Year : ")
    )
    i=i+1 