import re
import requests
from bs4 import BeautifulSoup

url = "https://prod.danawa.com/list/?cate=1022811&15main_10_02"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}
res=requests.get(url, headers = headers)

res = requests.get(url)
res.raise_for_status()
# soup = BeautifulSoup(res.text, "lxml")
print("응답코드 : ", res.status_code)
# items = soup.find_all("li", attrs={"class":re.compile("^search-product")})