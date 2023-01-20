from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
from bs4 import BeautifulSoup
import time

f_name = ['Netflix_genre_kr.csv','Netflix_genre_usa.csv','Netflix_genre_os.csv','Netflix_genre_awd.csv',
'Netflix_genre_inde.csv','Netflix_genre_chil.csv','Netflix_genre_ani.csv','Netflix_genre_act.csv',
'Netflix_genre_cmd.csv','Netflix_genre_rmc.csv','Netflix_genre_thril.csv','Netflix_genre_horr.csv',
'Netflix_genre_sf.csv','Netflix_genre_fant.csv','Netflix_genre_dram.csv','Netflix_genre_crim.csv',
'Netflix_genre_docu.csv','Netflix_genre_music.csv','Netflix_genre_clasc.csv','Netflix_genre_shorts.csv']

# 장르 선택 2 ~ 21
menu_num = 21
menu_max = 21

# 크롬으로 넷플릭스 접속 후 로그인
browser = webdriver.Chrome()
browser.get("https://www.netflix.com/kr/login")

browser.find_element(By.ID,"id_userLoginId").send_keys("minjeehye@naver.com")
browser.find_element(By.ID,"id_password").send_keys("jeehyewisdom121314")
browser.find_element(By.CLASS_NAME,"btn.login-button.btn-submit.btn-small").click()
time.sleep(3)

# 다수의 프로필 중 선택
profile = browser.find_elements(By.CLASS_NAME,"profile-link")
profile[2].click()      
time.sleep(3)

# 영화 탭 클릭
navigation_tab = browser.find_elements(By.CLASS_NAME,"navigation-tab")      
navigation_tab[2].click()   
time.sleep(3)

# 넷플 영화 csv 파일 만들기
filename = f_name[menu_num-2]       # 저장할 csv파일 이름 지정
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)
# 장르 버튼 클릭 
browser.find_element(By.CLASS_NAME,"ptrack-container").click()

# 첫줄에 칼럼 이름 추가 
soup = BeautifulSoup(browser.page_source, 'lxml')
genre = soup.find_all("a", attrs={"class":"sub-menu-link"})
column = genre[menu_num]
writer.writerow(column)

# 후 장르 선택 2 ~ 21
sub_menu = browser.find_elements(By.CLASS_NAME,"sub-menu-item")
sub_menu[menu_num].click()
time.sleep(2)
# 보기목록 변환
browser.find_element(By.CLASS_NAME,"aro-grid-toggle").click()     

# 스크롤 끝까지 밀기
prev_height = browser.execute_script("return document.body.scrollHeight")
# scroll = 0
while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(2)
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break
    prev_height = curr_height

    # if scroll == 6:
    #     break
    # scroll += 1

soup = BeautifulSoup(browser.page_source, 'lxml')
movies = soup.find_all("div", attrs={"class":"boxart-size-16x9 boxart-container boxart-rounded"})

# 영화 타이틀 저장
for movie in movies:
    title = movie.find("p", attrs={"class":"fallback-text"}).get_text()
    # print(title)
    data=[title]
    print(data)
    writer.writerow(data)
f.close()
