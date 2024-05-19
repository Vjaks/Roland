from scipy import stats
import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  database="number"
)

mycursor = mydb.cursor()
sql ="SELECT * From list"
mycursor.execute(sql)
for i in mycursor.fetchall():
    a =list(i)
    b=stats.mode(a)
    print(b)
    
   
mydb.commit() 
mydb.close()
print(mycursor.rowcount,"Rows Updateded")