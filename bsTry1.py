from bs4 import BeautifulSoup
import requests

URl ="https://webscraper.io/test-sites"
# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0'}
r =requests.get(url=URl)
soup = BeautifulSoup(r.content,'html.parser')

parent = soup.find("div",class_="container test-sites")
h2 = parent.find_all("a")
p = parent.find_all("p")
for a in h2 :
     print(a.text.strip())
     print()
for b in p :

    print(b.text.strip())