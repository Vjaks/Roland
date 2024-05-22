import requests
from bs4 import BeautifulSoup
import mysql.connector

# ------------  After Lines All Use Scrape Dinamalar Website  ------------


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


content = firstcontent.find("p",class_ = "MuiTypography-root MuiTypography-body1 css-1jdrf15")
loc = firstcontent.find("p",class_ = "MuiTypography-root MuiTypography-body2 css-1l5uvfz")

a = content.text
b = loc.text

count = 1

sql ="insert into news (than,loc) value(%s,%s)"
mycursor.execute(sql,(a,b))
mydb.commit()


for i in secondcontent :
    
    content = i.find("p",class_ = "MuiTypography-root MuiTypography-body1 css-1jdrf15")
    a=content.text
    b = loc.text

    count += 1

    sql ="insert into news (than,loc) value(%s,%s)"
    mycursor.execute(sql,(a,b))
    mydb.commit()
    
for i in thirdcontent :
    
    content = i.find("p",class_ = "MuiTypography-root MuiTypography-body1 css-101ltf4")
    a=content.text
    b = loc.text
    sql ="insert into news (than,loc) value(%s,%s)"
    mycursor.execute(sql,(a,b))
    mydb.commit()
    count +=1



# ------------  After Lines All Use Scrape thanthi Website  ------------

url = "https://www.dailythanthi.com/"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0'}
page = requests.get(url)

soup =BeautifulSoup(page.content,'html5lib')

main1 =soup.find("div",class_ ="col-md-8")

first = main1.find("div", class_="col-md-5 col-sm-6 b-r p-t-15 h-order-11")
first1 =first.find("div", class_ ="NewsWithLargeHeadline main_heading big-heading")
first2 =first.find_all("div", class_ ="NewsWithLargeHeadline main_heading")


second = main1.find("div", class_="col-md-7 col-sm-6 p-t-15 h-order-21")
second1 =second.find("div", class_ ="NewsWithTopImage")
second2 =second.find_all("div", class_ ="NewsWithNormalHeadline")

main2 = soup.find("div", class_ ="row row-bottom-border")
rowdiv = main2.find("div", class_ ="row")
rowloop = rowdiv.find_all("div", class_ ="col-md-3 col-sm-6 col-xs-12")


    

FinalOutput = """"""

heading = second1.h4.text.strip()
time = second1.span.text.strip("GMT")
timestr =str(time)
timestrip =timestr.strip()
Abstract = second1.div.text.strip()

FinalOutput += heading+"\n"
FinalOutput += timestrip+"\n"
FinalOutput += Abstract+"\n"


heading1 = first1.h4.text.strip()
time1 = first1.span.text.strip("GMT")
timestr1 =str(time)
timestrip1 =timestr1.strip()
Abstract1 = first1.find("div", class_ = "abstract").text.strip()

FinalOutput += heading1+"\n"
FinalOutput += timestrip1+"\n"
FinalOutput += Abstract1+"\n"

for i in first2 :
    heading = i.h4.text.strip()
    time = i.span.text.strip("GMT")
    timestr =str(time)
    timestrip =timestr.strip()
    Abstract = i.find("div", class_ = "abstract").text.strip()

    FinalOutput += heading+"\n"
    FinalOutput += timestrip+"\n"
    FinalOutput += Abstract+"\n"


for i in second2 :
     heading = i.h4.text.strip()
     time = i.span.text.strip("GMT")
     timestr =str(time)
     timestrip =timestr.strip()
     Abstract = i.find("div", class_ = "abstract").text.strip()
     
     FinalOutput += heading+"\n"
     FinalOutput += timestrip+"\n"
     FinalOutput += Abstract+"\n"

for i in rowloop :
    heading = i.h4.text.strip()
    time = i.span.text.strip("GMT")
    timestr =str(time)
    timestrip =timestr.strip()
    Abstract = i.find("div", class_ = "abstract").text.strip()

    FinalOutput += heading+"\n"
    FinalOutput += timestrip+"\n"
    FinalOutput += Abstract+"\n"

FinalOutput = FinalOutput.split("\n")


li = FinalOutput

for i in li :
    for i1 in i:

     index1 = 0
     index2 = 1
     index3 = 2

mycursor.execute('SELECT COUNT(*) FROM news')

rowcount = mycursor.fetchone()[0]

OutputCount = 0

for i in li :
    OutputCount += 1
rowcount -= 15
while index3 < OutputCount :
      ind1 = li[index1]
      ind2 = li[index2]
      ind3 = li[index3]
      sql = "update news set dina = %s,time = %s,abstract = %s where  newsid =%s"
      mycursor.execute(sql,(ind1,ind2,ind3,rowcount))
      mydb.commit()


      index1 += 3
      index2 += 3
      index3 += 3
      rowcount += 1