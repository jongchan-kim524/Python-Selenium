from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
stg_dev = input('운영이면 0, stg면 1을, dev면 2를 눌러주세요')

if stg_dev == '0':
    url = 'https://www.tripcody.com/notice'
elif stg_dev =='1':
    url = 'https://stg.tripcody.com/notice/182592'
elif stg_dev =='2':
    url = 'https://dev.tripcody.com/notice/182592'


driver.get(url)
time.sleep(3)

# 컨텐츠 카드들 찾기
cards = driver.find_elements(By.CLASS_NAME, 'content-card-wrapper')
titles = []

# 카드들에서 타이틀 추출하기
for card in cards:
    contents = card.find_element(By.CLASS_NAME, 'card-contents')
    title = card.find_element(By.CLASS_NAME,'main-title').text
    titles.append(title)
if len(titles)==0:
    print('공지사항이 없습니다.')

else:
    print('총 %d개의 공지사항을 찾았습니다!'%len(titles))

    # 어떤 타이틀의 공지사항 조회수를 올릴지 index를 input으로 받음
    for i, title in enumerate(titles):
        print(i, ":",title)
    idx = int(input('조회수를 올릴 contents의 index를 입력해주세요 '))

    # index를 input으로 받아서 해당 index카드의 제목을 클릭해줌
    def click_idx(idx):
        cards =  driver.find_elements(By.CLASS_NAME, 'content-card-wrapper')
        card = cards[idx]
        contents = card.find_element(By.CLASS_NAME, 'card-contents')
        title = contents.find_element(By.CLASS_NAME,'main-title')
        title.click()

    # card 내에서 뒤로가기 버튼을 눌러줌
    def go_back():
        back_btn = driver.find_element(By.CLASS_NAME, 'v-btn__content')
        back_btn.click()

    # 얼마나 조회수를 올릴지 입력받아서 그만큼 반복수행
    n = int(input('얼마나 올릴까요?: '))
    for i in range(n):
        # 클릭
        click_idx(idx)
        time.sleep(1)
        # 뒤로가기
        go_back()
        time.sleep(1)

    # 수행완료되면 끝 출력해서 알려줌
    print('끝')