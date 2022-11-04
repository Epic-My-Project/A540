import requests
from bs4 import BeautifulSoup # pip install beautifulsoup4

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml") # pip install lxml

# 이렇게 하는건 페이지의 정보를 잘 알고있을 때
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a)                 # soup 객체에서 처음 발견하는 a element를 출력
# print(soup.a.attrs)           # a element의 속성 정보를 출력
# print(soup.a["href"])           # a element의 href 속성 '값' 정보를 출력

# 일반적으로 페이지의 정보를 잘 모를 때
# print(soup.find("a", attrs={"class" : "Nbtn_upload"})) # class = "Nbtn_upload" 인 a element를 찾아줘
# print(soup.find(attrs={"class" : "Nbtn_upload"})) # class="Nbtn_upload" 인 어떤 element를 찾아줘

#
# print(soup.find("li", attrs={"class" : "rank01"}))
rank01 = soup.find("li", attrs={"class" : "rank01"})
print(rank01)
# print(rank01.next_sibling) # 빈줄이 있을 수 도 있음 그럴땐 next.sibling을 한번더 쓸것
# rank02 = rank01.next_sibling.next_sibling
# rank03 = rank02.next_sibling.next_sibling
# print(rank03.a.get_text())
# rank02 = rank03.previous_sibling.previous_sibling
# print(rank02.a.get_text())
# print(rank01.parent)

# rank02 = rank01.find_next_sibling("li")
# print(rank02.a.get_text())
# rank01 = rank02.find_previous_sibling("li")
# print(rank01.a.get_text())

# rankall = rank01.find_next_siblings("li")
# print(rankall)

# webtoon = soup.find("a", text="참교육-101화")
# print(webtoon.get_text())
