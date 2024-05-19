import requests
from bs4 import BeautifulSoup

url = "https://www.dailythanthi.com/"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0'}
page = requests.get(url)

soup =BeautifulSoup(page.content,'html5lib')

main =soup.find("div",class_ ="col-md-8")

first = main.find("div", class_="col-md-5 col-sm-6 b-r p-t-15 h-order-11")
first1 =first.find("div", class_ ="NewsWithLargeHeadline main_heading big-heading")
first2 =first.find_all("div", class_ ="NewsWithLargeHeadline main_heading")


second = main.find("div", class_="col-md-7 col-sm-6 p-t-15 h-order-21")
second1 =second.find("div", class_ ="non-mob-item")
second2 =second.find_all("div", class_ ="NewsWithNormalHeadline")


def Extractor(name):
     f =open("news.txt","a", encoding='utf-8')
     heading = name.h4.text.strip()

     time = name.span.text.strip("GMT")
     timestr =str(time)
     timestrip =timestr.strip()
     Abstract = name.div.text.strip()
    
     
