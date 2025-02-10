# Scheduling? 특정 시간에 작업을 예약하고 실행하는 프로세스
import schedule
import time
import requests
from bs4 import BeautifulSoup  # 파싱

def perform_web_crawling():
    response = requests.get("http://www.naver.com")
    soup = ""
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
    print(soup)

def job():
    print("Scheduling 을 수행 합니다.")
    perform_web_crawling()
    
# 매일 정해진 시간에 동작하도록 구현
schedule.every().day.at("09:44").do(job)

while True:
    schedule.run_pending() # 대기 중인 작업을 수행하는 함수
    time.sleep(1)          # 1초마다 반복 수행