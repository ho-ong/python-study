from selenium import webdriver
import time

driver = webdriver.Chrome("chromedriver")

# 네이버로 이동하기
url = "https://www.naver.com"
driver.get(url)

time.sleep(3)

# 다음으로 이동하기
url = "https://www.daum.net"
driver.get(url)

# 종료
driver.quit()
