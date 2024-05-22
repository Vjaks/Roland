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
Main = soup.find("div", class_ = "MuiGrid-root MuiGrid-item MuiGrid-grid-xs-12 MuiGrid-grid-sm-12 MuiGrid-grid-md-8.5 css-1fq84pi")
FirstContent = Main.find("div", class_ = "MuiGrid-root MuiGrid-item MuiGrid-grid-xs-12 MuiGrid-grid-md-12 css-1c993yn")
SecondContent = Main.find_all("div", class_ = "MuiGrid-root MuiGrid-item MuiGrid-grid-xs-12 MuiGrid-grid-md-12 css-jgmj13")
ThirdContent = Main.find_all("div", class_ = "MuiGrid-root MuiGrid-item MuiGrid-grid-xs-12 MuiGrid-grid-md-3 css-hewddt")


Content = FirstContent.find("p",class_ = "MuiTypography-root MuiTypography-body1 css-1jdrf15")
Loc = FirstContent.find("p",class_ = "MuiTypography-root MuiTypography-body2 css-1l5uvfz")


FinalOutput = []

FirstOutput = Content.text
SecondOutput = Loc.text



FinalOutput.insert(0,FirstOutput)
FinalOutput.insert(1,SecondOutput)

DinaLoopList1 = """"""

for i in SecondContent :
    
    Content = i.find("p",class_ = "MuiTypography-root MuiTypography-body1 css-1jdrf15")
   
    FirstOutput = Content.text
    SecondOutput = Loc.text
    
    DinaLoopList1 += FirstOutput+"\n"
    DinaLoopList1 += SecondOutput+"\n"

DinaLoopList1 = DinaLoopList1.split("\n")
FinalOutput.insert(5,DinaLoopList1)
FinalOutput.insert(6,DinaLoopList1)

DinaLoopList2 = """"""

for i in ThirdContent :
    
    Content = i.find("p",class_ = "MuiTypography-root MuiTypography-body1 css-101ltf4")

    FirstOutput = Content.text
    SecondOutput = Loc.text

    DinaLoopList2 += FirstOutput+"\n"
    DinaLoopList2 += SecondOutput+"\n"

DinaLoopList2 = DinaLoopList2.split("\n")


# ------------  After Lines All Use Of Scrape thanthi Website  ------------

url = "https://www.dailythanthi.com/"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0'}
page = requests.get(url)

soup =BeautifulSoup(page.content,'html5lib')

main1 =soup.find("div",class_ ="col-md-8")

first = main1.find("div", class_="col-md-5 col-sm-6 b-r p-t-15 h-order-11")
first1 =first.find("div", class_ ="NewsWithLargeHeadline main_heading big-heading")
first2 =first.find_all("div", class_ ="NewsWithLargeHeadline main_heading")


second = main1.find("div", class_="col-md-7 col-sm-6 p-t-15 h-order-21")
second1 =second.find("div", class_ ="non-mob-item")
second2 =second.find_all("div", class_ ="NewsWithNormalHeadline")


heading = second1.h4.text.strip()
time = second1.span.text.strip("GMT")
timestr =str(time)
timestrip =timestr.strip()
Abstract = second1.div.text.strip()

FinalOutput.insert(2,heading)
FinalOutput.insert(3,timestrip)
FinalOutput.insert(4,Abstract)

heading = first1.h4.text.strip()
time = first1.span.text.strip("GMT")
timestr =str(time)
timestrip =timestr.strip()
Abstract = first1.div.text.strip()


ThanLoopOutput1 = """"""

for i in first2 :
    heading = i.h4.text.strip()
    time = i.span.text.strip("GMT")
    timestr =str(time)
    timestrip =timestr.strip()
    Abstract = i.div.text.strip()


    ThanLoopOutput1 += heading+"\n"
    ThanLoopOutput1 += timestrip+"\n"
    ThanLoopOutput1 += Abstract+"\n"

ThanLoopOutput1 = ThanLoopOutput1.split("\n")


ThanLoopOutput2 = """"""

for i in second2 :
   
    heading = i.h4.text.strip()
    time = i.span.text.strip("GMT")
    timestr =str(time)
    timestrip =timestr.strip()
    Abstract = i.div.text.strip()

    ThanLoopOutput2 += heading+"\n"
    ThanLoopOutput2 += timestrip+"\n"
    ThanLoopOutput2 += Abstract+"\n"

ThanLoopOutput2 = ThanLoopOutput2.split("\n")

print(FinalOutput[2])

li = FinalOutput
for i in li :
    for i1 in i:

     index1 = 0
     index2 = 1
     index3 = 2
     index4 = 3
     index5 = 4

count = 0
for i in li :
    count += 1
while index5 < count :
      ind1 = li[index1]
      ind2 = li[index2]
      ind3 = li[index3]
      ind4 = li[index4] 
      ind5 = li[index5]

     #  sql = "insert into news (than,loc) value(%s,%s)"
     # mycursor.execute(sql,(ind1,ind2))
     # mydb.commit()

      index1 += 5
      index2 += 5
      index3 += 5
      index4 += 5
      index5 += 5
