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

url = "https://www.dinamalar.com/"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0'}
page = requests.get(url=url)

soup =BeautifulSoup(page.content,"html5lib")
main = soup.find("div", class_ = "MuiGrid-root MuiGrid-item MuiGrid-grid-xs-12 MuiGrid-grid-sm-12 MuiGrid-grid-md-8.5 css-1fq84pi")
firstcontent = main.find("div", class_ = "MuiGrid-root MuiGrid-item MuiGrid-grid-xs-12 MuiGrid-grid-md-12 css-1c993yn")
secondcontent = main.find_all("div", class_ = "MuiGrid-root MuiGrid-item MuiGrid-grid-xs-12 MuiGrid-grid-md-12 css-jgmj13")
thirdcontent = main.find_all("div", class_ = "MuiGrid-root MuiGrid-item MuiGrid-grid-xs-12 MuiGrid-grid-md-3 css-hewddt")


def Extracter(whichcontent):
        content = whichcontent.find("p",class_ = "MuiTypography-root MuiTypography-body1 css-1thrkza")
        loc = whichcontent.find("p",class_ = "MuiTypography-root MuiTypography-body2 css-rnvbsw")
        a = content.text
        b = loc.text

        sql = "INSERT INTO news (than,loc) values(%s,%s)"
        
        mycursor.execute(sql,(a,b))

        mydb.commit()
        print(mycursor.rowcount,"Rows Updateded")


        for i in secondcontent:
            content = i.find("p",class_ = "MuiTypography-root MuiTypography-body1 css-1thrkza")
            a=content.text
            b = loc.text
            
            sql = "INSERT INTO news (than,loc) values(%s,%s)"
            mycursor.execute(sql,(a,b))
                    
            mydb.commit()
            print(mycursor.rowcount,"Rows Updateded")
        for i in thirdcontent:
    
            content = i.find("p",class_ = "MuiTypography-root MuiTypography-body1 css-1icbtnf")
            a=content.text
            b = loc.text
            
            sql = "INSERT INTO news (than,loc) values(%s,%s)"
            mycursor.execute(sql,(a,b))
                    
            mydb.commit()
            print(mycursor.rowcount,"Rows Updateded")
        sql = "INSERT INTO news (than) values('Once Updated')"

        mycursor.execute(sql)
        
        mydb.commit()
        print(mycursor.rowcount,"Rows Updateded")     








