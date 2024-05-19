import requests
from bs4 import BeautifulSoup
import mysql.connector
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="",
  database="newsdb"
)
mycursor = mydb.cursor()
URL ="https://www.dailythanthi.com/"

req = requests.get(url=URL)

soup = BeautifulSoup(req.content,"html.parser")

first = soup.find('div',class_ = "col-md-5 col-sm-6 b-r p-t-15 h-order-11")
first1 = first.find_all('h4')
for i in first1 :
    sql = "INSERT INTO heading (heading) values(%s)"
    values=(i)
    mycursor.execute(sql,values)
    
    mydb.commit()
    print(mycursor.rowcount,"Rows Updateded")




