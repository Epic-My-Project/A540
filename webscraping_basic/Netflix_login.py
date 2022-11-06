from selenium import webdriver
from selenium.webdriver.common.by import By
import time


browser = webdriver.Chrome()
browser.get("https://www.netflix.com/kr/login")

browser.find_element(By.ID,"id_userLoginId").send_keys("minjeehye@naver.com")
browser.find_element(By.ID,"id_password").send_keys("jeehyewisdom121314")

browser.find_element(By.CLASS_NAME,"btn.login-button.btn-submit.btn-small").click()

time.sleep(2)

profile = browser.find_elements(By.CLASS_NAME,"profile-link")
profile[3].click()


while(True):
    pass
