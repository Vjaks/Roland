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

Source_URL = "https://www.quora.com/Can-we-store-images-in-SQL-database"
page = requests.get(Source_URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find("div", class_="q-text")
news_elements = results.find_all("span", class_="q-box qu-userSelect--text")
for news_raw in news_elements:
    tit = news_raw.find("p", class_="q-text qu-display--block qu-wordBreak--break-word qu-textAlign--start").text.strip()
    

    print(tit)
   
 
    print('\n'*2)

    sql = "INSERT INTO news (news, source, news_url) VALUES (%s, %s, %s)"
    data = (tit)
    try:
        mycursor.execute(sql, data)
        mydb.commit()
    except:
        mydb.rollback()

mydb.close()

