import re
import requests
from bs4 import BeautifulSoup # pip install beautifulsoup4

url = "https://prod.danawa.com/list/?cate=112757"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}
res=requests.get(url, headers = headers)
res.raise_for_status()
print(res)

soup = BeautifulSoup(res.text, "lxml") # pip install lxml
tv = soup.find_all("li", attrs={ "class" : "prod_item prod_layer width_change" })



with open("danawa_monitor.txt", "w", encoding="utf-8", newline="") as lap:
   for target in tv:
      tvn = target.find("a", attrs={"name": "productName"})
      print(tvn.get_text().strip())
      lap.write(tvn.get_text().strip() + " ")
      tvp = target.find("p", attrs={"class":"price_sect"}).find("strong")
      print(tvp.get_text())
      lap.write(tvp.get_text() + '\n')