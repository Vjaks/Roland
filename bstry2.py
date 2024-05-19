from bs4 import BeautifulSoup
import requests

URl ="https://www.w3schools.com/python/default.asp"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0'}
r =requests.get(url=URl,headers=headers)

soup = BeautifulSoup(r.content,'html.parser')

parent = soup.find("div",id="leftmenuinner")
a =parent.find_all("a")
for i in a:
   print(i.text.strip())
  
