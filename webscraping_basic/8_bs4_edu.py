import requests
from bs4 import BeautifulSoup # pip install beautifulsoup4

url = "https://comic.naver.com/webtoon/list?titleId=758037&weekday=mon"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml") # pip install lxml


# 링크 정보 다 가져오기 + 회차 이름
# cartoons = soup.find_all("td", attrs={"class":"title"})
# title = cartoons[1].a.get_text()
# link = cartoons[0].a["href"]
# print(title)
# print("https://comic.naver.com" + link)   # 링크 정보 가져오기
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "https://comic.naver.com" + cartoon.a["href"]    
#     print(title, link)

# 평점 구하기
total_rates = 0
cartoons = soup.find_all("div", attrs={"class" : "rating_type"})
for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()
    print(rate)
    total_rates += float(rate)
print("전체점수 : ", total_rates)
print("평균점수 : ", total_rates/len(cartoons))