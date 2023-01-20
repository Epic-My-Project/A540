from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from bs4 import BeautifulSoup
import time

# pandas dataframe으로 저장
def processing_chart_list(chart_list):
    df = pd.DataFrame(chart_list, columns=['title', 'imgsrc', 'history'])
    # DataFrame에 잘라놓은 리스트들을 담아준다. columns는 반드시 갯수에 맞게 만들어준다.
    # df.index = df.index + 1
    # index 시작을 1부터 한다
    df.to_csv(f'Netflix_title.csv', mode='w', encoding='utf-8-sig', header=True, index=False)
    # csv로 저장해준다
    print(df)

browser = webdriver.Chrome()
browser.get("https://www.netflix.com/kr/login")

browser.find_element(By.ID,"id_userLoginId").send_keys("minjeehye@naver.com")
browser.find_element(By.ID,"id_password").send_keys("jeehyewisdom121314")

browser.find_element(By.CLASS_NAME,"btn.login-button.btn-submit.btn-small").click()

time.sleep(3)

profile = browser.find_elements(By.CLASS_NAME,"profile-link")
profile[2].click()      # 다수의 프로필 중 선택

time.sleep(3)

navigation_tab = browser.find_elements(By.CLASS_NAME,"navigation-tab")
navigation_tab[2].click()   
browser.find_element(By.CLASS_NAME,"aro-grid-toggle").click()

# 스크롤 끝까지 밀기
prev_height = browser.execute_script("return document.body.scrollHeight")
scroll = 0
while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(1.5)
    curr_height = browser.execute_script("return document.body.scrollHeight")
    # if curr_height == prev_height:
    #     break
    # prev_height = curr_height

    if scroll == 6:
        break
    scroll += 1

soup = BeautifulSoup(browser.page_source, 'lxml')
movies = soup.find_all("div", attrs={"class":"boxart-size-16x9 boxart-container boxart-rounded"})

# 받아온 타이틀 이미지링크를 저장
data=[]
for movie in movies:
    title = movie.find("p", attrs={"class":"fallback-text"}).get_text()
    img = movie.find("img", attrs={"class":"boxart-image boxart-image-in-padded-container"}).get('src')
    # print(title)
    temp = [title, img, 0]
    data.append(temp)
print(data)
processing_chart_list(data)
# while(True):
#     pass
