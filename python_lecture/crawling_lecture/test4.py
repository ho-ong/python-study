from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("chromedriver")

url = "https://www.google.com"
driver.get(url)

# 키보드 입력
elem = driver.find_element(By.CSS_SELECTOR, '#APjFqb')
elem.send_keys("코로나") # 엔터키 입력
elem.send_keys(Keys.RETURN) # 검색키 입력
time.sleep(200)
