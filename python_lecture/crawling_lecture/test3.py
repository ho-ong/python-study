from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("chromedriver")

url = "https://www.naver.com"
driver.get(url)

# 마우스 입력
driver.find_element(By.CSS_SELECTOR, '#NM_FAVORITE > div.group_nav > ul.list_nav.NM_FAVORITE_LIST > li:nth-child(8) > a').click()
time.sleep(5)

# 마우스 입력
driver.find_element(By.CSS_SELECTOR, '#menu > li:nth-child(3) > a').click()
time.sleep(200)
