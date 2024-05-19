import requests
from bs4 import BeautifulSoup

URL = "https://tamil.news18.com/technology/"

req = requests.get(url=URL)

soup = BeautifulSoup(req.content, "html.parser")

par = soup.find("h1", class_="jsx-a21ba16ef998c3ee newglblctgrhd")
a = par.text

mainn = soup.find_all("div", class_="jsx-7fb8351356a551b4 hd")

for item in mainn:
    mainn1 = item.find_next("a", class_="jsx-7fb8351356a551b4")
    if mainn1:
        print(mainn1.text)
