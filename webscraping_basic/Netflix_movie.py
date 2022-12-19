from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
from bs4 import BeautifulSoup
import time

# 넷플 영화 csv 파일 만들기
filename = "Netflix_title.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)
column = "title  imgsrc  history  genre".split("  ")
writer.writerow(column)

browser = webdriver.Chrome()
browser.get("https://www.netflix.com/kr/login")

browser.find_element(By.ID,"id_userLoginId").send_keys("minjeehye@naver.com")
browser.find_element(By.ID,"id_password").send_keys("jeehyewisdom121314")

browser.find_element(By.CLASS_NAME,"btn.login-button.btn-submit.btn-small").click()

time.sleep(3)

profile = browser.find_elements(By.CLASS_NAME,"profile-link")
profile[3].click()      # 다수의 프로필 중 선택

time.sleep(3)

navigation_tab = browser.find_elements(By.CLASS_NAME,"navigation-tab")
navigation_tab[2].click()   
browser.find_element(By.CLASS_NAME,"aro-grid-toggle").click()

# 스크롤 끝까지 밀기
prev_height = browser.execute_script("return document.body.scrollHeight")
# scroll = 0
while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(1.5)
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break
    prev_height = curr_height

    # if scroll == 6:
    #     break
    # scroll += 1

soup = BeautifulSoup(browser.page_source, 'lxml')
movies = soup.find_all("div", attrs={"class":"boxart-size-16x9 boxart-container boxart-rounded"})
# with open("movie.html", "w", encoding="utf8") as f:
#     f.write(soup.prettify())

# 받아온 타이틀 이미지링크를 저장
for movie in movies:
    title = movie.find("p", attrs={"class":"fallback-text"}).get_text()
    img = movie.find("img", attrs={"class":"boxart-image boxart-image-in-padded-container"}).get('src')
    # print(title)
    data=[title,img,0]
    print(data)
    print(img)
    writer.writerow(data)

# while(True):
#     pass
