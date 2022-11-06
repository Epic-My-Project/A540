from selenium import webdriver
from selenium.webdriver.common.by import By
import time


browser = webdriver.Chrome()
browser.get("https://watcha.com/")

elem = browser.find_element(By.CLASS_NAME,"css-qxkazn")
elem.click()

browser.find_element(By.CLASS_NAME,"css-2sw17l").send_keys("wlsdud2528@gmail.com")
browser.find_element(By.CLASS_NAME,"css-s8pas4").send_keys("ehxhfl1720!")

browser.find_element(By.CLASS_NAME,"css-11a3zmg").click()

time.sleep(2)

browser.find_element(By.CLASS_NAME,"css-1blyq76").click()

while(True):
    pass
