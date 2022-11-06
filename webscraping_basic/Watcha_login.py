from selenium import webdriver
from selenium.webdriver.common.by import By
import time


browser = webdriver.Chrome()
browser.get("https://watcha.com/")

elem = browser.find_element(By.XPATH,"//*[@id='root']/div[1]/nav/ul[2]/li/a")
elem.click()

browser.find_element(By.XPATH,"//*[@id='root']/div[1]/main/div/main/div/form/div[1]/input").send_keys("개인id")
browser.find_element(By.XPATH,"//*[@id='root']/div[1]/main/div/main/div/form/div[2]/input").send_keys("개인pw")

browser.find_element(By.XPATH,"//*[@id='root']/div[1]/main/div/main/div/form/div[3]/button").click()

time.sleep(2)

browser.find_element(By.CLASS_NAME,"css-1blyq76").click()

while(True):
    pass
