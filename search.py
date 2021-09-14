from bs4 import BeautifulSoup
from selenium import webdriver
import time
import sys
import os
import pandas as pd

# 엑셀 파일명은 상품.xlsx, 맛집.xlsx, 명소.xlsx

driver = webdriver.Chrome()

stg_dev = input('운영이면 0, stg면 1을, dev면 2를 눌러주세요')
if stg_dev == '0':
    url = 'https://tripcody.com/search/182592'
elif stg_dev == '1':
    url = 'https://stg.tripcody.com/search/182592'
elif stg_dev == '2':
    url = 'https://dev.tripcody.com/search/182592'

driver.get(url)
time.sleep(3)


# input으로 받은 값을 검색해주는 함수
def search(query_text):
    driver.find_element_by_xpath('//*[@id="__layout"]/div/div[3]/div[1]/header/div/input').clear()  # 기존에 있는 검색키워드를 지워줌
    driver.find_element_by_xpath('//*[@id="__layout"]/div/div[3]/div[1]/header/div/input').send_keys(
        query_text)  # input으로 값을 검색어 input box에 넣는다
    driver.find_element_by_xpath('//*[@id="__layout"]/div/div[3]/div[1]/header/div/input').send_keys('\n')  # 엔터를 누르는 효과


# 검색 결과에 있는지 확인해서 있으면 True, 없으면 False를 반환하는 함수
def get_result(label, name):
    search(name)
    time.sleep(2)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    results = soup.find_all(class_='result-category-section')
    if label == '상품':
        result = results[0].text
        return (name in result)

    elif label == '맛집' or label == '음식':
        result = results[1].text
        return (name in result)

    elif label == '명소':
        result = results[2].text
        return (name in result)


files = []
# 현재 .py 파일이 있는 폴더에서 .xlsx확장자를 가진 파일들을 찾는다.
# 모든 파일에 대해 수행한다(원하는 파일만 수행할 수 없으므로, 검색을 원하지 않는 파일은 미리 다른 폴더에 옮겨야 한다)
for i in os.listdir(os.getcwd()):
    if i.endswith('.xlsx'):
        files.append(i)
print('다음 파일들을 찾았습니다:', files)

# .xlsx로 끝나는 파일들을 찾아서 이름을 읽어와 이전에 정의한 함수들을 수행한다.
#
for f in files:
    print(f, '파일 수행 중')
    label = f[:2]
    names = pd.read_excel(f, header=None)[0]
    print('names: ', names)
    result_pass = []
    result_fail = []

    # 엑셀에 있는 모든 이름에 대해 수행하여 결과를 저장한다.
    for name in names:
        if '(' in name:
            name = name.split('(')[0]
        print(name)
        if get_result(label, name):
            result_pass.append(name)
        else:
            result_fail.append(name)

    # 수행 결과에 대한 판단을 한다.
    if len(result_fail) == 0:  # 실패 항목이 없는 경우
        print('%s에서 실패 항목 없음' % label)

    else:  # 실패한 항목이 있는 경우, 개수와 그 이름을 터미널에 출력해준다.
        print('%s의 실패 항목 개수: %d' % (label, len(result_fail)))
        print('%s의 실패 항목: ' % label)
        for i in result_fail:
            print(i, end=',')

        txt = open(label + '.txt', 'a', encoding='utf8')  # 사용자가 확인하기 편하도록 .txt로도 저장해준다.
        for i in result_fail:
            txt.write(i)
            txt.write('\n')
        txt.close()




