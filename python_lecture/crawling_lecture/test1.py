from selenium import webdriver
import time

driver = webdriver.Chrome("chromedriver")
driver.get("https://www.naver.com")

# 200초 동안 멈추기
time.sleep(200)
