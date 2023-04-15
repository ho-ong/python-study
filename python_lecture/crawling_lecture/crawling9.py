from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from openpyxl import Workbook
import pandas as pd
import time
import warnings

warnings.filterwarnings('ignore')
wb = Workbook(write_only=True)
ws = wb.create_sheet()

driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://www.youtube.com/watch?v=8pSC6QgxFzI&t=593s")
driver.implicitly_wait(3)
time.sleep(1.5)

driver.execute_script("window.scrollTo(0, 800)")
time.sleep(3)

last_height = driver.execute_script("return document.documentElement.scrollHeight")

# while True : # 끝까지 내릴 때
# 스크롤을 2번 내리는 구문
for i in range(0, 2): # 2번만 내린다.
  driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
  # 댓글이 다 돌 때까지 기다리기 위해 1.5초 기다린다.
  time.sleep(1.5)
  # 내린 상태의 높이를 반환
  new_height = driver.execute_script("return document.documentElement.scrollHeight")

  # 다 내렸을 때 더 스크롤이 내려가지 않으므로 before과 높이가 같으니까
  # 즉 스크롤을 다 내렸다고 판단할 수 있다.
  # 그때 break문으로 더 loop를 돌지 않는다.
  if new_height == last_height:
    break
  last_height = new_height

time.sleep(10)

# ==================================================================== 여기까지 댓글이 다 렌더링할 때까지 기다려야 한다.

# 유튜브 프리미엄 팝업이 뜨는 것을 닫아주는 역할
# try:
#   driver.find_element(By.CSS_SELECTOR,"#dismiss-button > a").click()
# except:
#   pass

html_source = driver.page_source
soup = BeautifulSoup(html_source, 'html.parser')

# div중에 id가 header-author인 것을 찾고, id가 autor-text인 것을 찾고, span 부분
id_list = soup.select("div#header-author > h3 > #author-text > span")
# yt-formatted-string 요소 중에 id가 content-text인 것들 찾기
# comment_list = soup.select("yt-formatted-string#content-text")
comment_list = soup.select("yt-formatted-string#content-text")

# print(comment_list)

id_final = []
comment_final = []

for i in range(len(comment_list)):
  temp_id = id_list[i].text

  print("작성자 :", str(id_list[i].text).strip(), "댓글 :", comment_list[i].text)
  print("===================================================================")
  
  # 데이터 확인
  # print(id_list[i])
  # print(id_list[i].text)
  
  temp_id = temp_id.replace('\n', '')
  temp_id = temp_id.replace('\t', '')
  temp_id = temp_id.replace('    ', '')
  id_final.append(temp_id) # 댓글 작성자

  temp_comment = comment_list[i].text
  temp_comment = temp_comment.replace('\n', '')
  temp_comment = temp_comment.replace('\t', '')
  temp_comment = temp_comment.replace('    ', '')
  comment_final.append(temp_comment) # 댓글 내용

pd_data = {"아이디": id_final , "댓글 내용": comment_final}
youtube_pd = pd.DataFrame(pd_data)
youtube_pd.to_excel('Youtube_result.xlsx')

id_list_zip = []
conmment_list_zip = []

for i in range(0, len(id_list)):
  id_list_zip.append(str(id_list[i].text).strip())
  conmment_list_zip.append(comment_list[i].text)

sdict = {
  "작성자": id_list_zip,
  "댓글": conmment_list_zip
}

you_tube = pd.DataFrame(sdict)
you_tube.to_csv("youtube_result.csv")
