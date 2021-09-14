from selenium import webdriver
import time
import sys
import os


naver_email = input('네이버 이메일: ')
naver_pwd = input('네이버 비밀번호: ')

n = int(input('몇개나 만들까요?: '))

driver = webdriver.Chrome()

stg_dev = input('운영이면 0, stg면 1을, dev면 2를 눌러주세요')
if stg_dev == '0':
    url = 'https://www.tripcody.com/itinerary/182592'
elif stg_dev =='1':
    url = 'https://stg.tripcody.com/itinerary/182592'
elif stg_dev =='2':
    url = 'https://dev.tripcody.com/itinerary/182592'



driver.get('https://www.tripcody.com/itinerary/182592')
time.sleep(3)

# 새 일정을 만들어주는 함수, input으로 일정의 이름을 받는다.
def new_schedule(schedule_name):
    # 새 일정 만들기
    driver.find_element_by_xpath('//*[@id="__layout"]/div/div[3]/div[1]/button/div').click()
    time.sleep(1)
    # 일정 제목
    driver.find_element_by_xpath('//*[@id="__layout"]/div/div[3]/div/div[1]/input').send_keys(schedule_name)
    # 일정 시작과 끝 선택
    driver.find_element_by_xpath('//*[@id="__layout"]/div/div[3]/div/div[1]/section/div[2]/div[30]/div/div[3]').click()
    driver.find_element_by_xpath('//*[@id="__layout"]/div/div[3]/div/div[1]/section/div[2]/div[33]/div/div[3]').click()
    # 새 일정 생성하기
    driver.find_element_by_xpath('//*[@id="bottom-button"]/button').click()
    time.sleep(1)
    # 일정 목록으로 가기
    driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div/header/div/button[1]').click()
    time.sleep(1)

# 네이버 로그인 클릭
driver.find_element_by_xpath('//*[@id="__layout"]/div/div[3]/div/div[4]/div[1]/div').click()
time.sleep(2)

# 이메일과 패스워드 입력
driver.find_element_by_id('id').send_keys(naver_email)
driver.find_element_by_id('pw').send_keys(naver_pwd)
time.sleep(2)
# 로그인 클릭
driver.find_element_by_xpath('//*[@id="log.login"]').click()
time.sleep(5)


for i in range(n):
    new_schedule(str(i+1))