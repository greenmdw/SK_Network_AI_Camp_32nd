# path: .\\static_crawling_project\\crawling\\self_Study_260514.py

# 모듈 설치: beautifulsoul4, requsets
import urllib.request, bs4

# *1. url로 웹 페이지 접속
web_page1 = urllib.request.urlopen('http://www.naver.com')
print(web_page1)     # <http.client.HTTPResponse object at 0x0000024013FB5300>

# *2. 접속한 페이지 소스 읽기
html_code = web_page1.read()
# print(html_code)    # 페이지 소스 출력됨. 한글은 인코딩되어 안읽힘

# *3. 읽어온 소스 html 태그 구문으로 바꿈 
decoding_code = bs4.BeautifulSoup(html_code, 'html.parser')
# print(decoding_code)    # 디코딩 됨

# *4. url을 키보드로 입력받아서 (복사>붙여넣기) 크롤링
# url_input = input('접속할 url: ')
# url: 웹 상에서 자원까지의 경로
# 표현: 프로토콜://도메인명/폴더명/파일명?이름=값&이름=값#표식이름
# 도메인명: 웹 서버에 ip 주소: 포트번호를 매핑한 이름
# 쿼리스트링: 서버측의 연결 대상에게 전달되는 값들을 표현
# 쿼리스트링은 pathvariable로 대체될 수 있음. 
# pathvariable은 경로변수로 웹 서버에 요청보낼 때, url 경로 자체에 데이터를 포함시켜 전달하는 방식

# web_page0 = urllib.request.urlopen(url_input)
# result_code0 = bs4.BeautifulSoup(web_page0, 'html.parser')
# print(result_code0)      

# *5. 네이버 개봉 영화 검색 결과 페이지에서 크롤링해서 분석 스크립트
web_page = urllib.request.urlopen('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EA%B0%9C%EB%B4%89%EC%98%81%ED%99%94&ackey=5777hk7c')
result_code = bs4.BeautifulSoup(web_page, 'html.parser')
# print(result_code)
"""
개봉 영화 정보가 기록된 태그 엘리먼트 찾는 법:
브라우저 개발 도구 (F12)
태그안의 값을 추출: find() 함수 => 찾은 엘리먼트 첫 번째 것 하나만 리턴
    find(태그명, 태그속성_='속성값')
    find(태그속성_='속성값')
    find(태그명)
"""
data_box = result_code.find('div', {'class': 'data_box'})
# print(data_box.prettify())    첫 번째 data_box인 마이클 잭슨 항목의 소스코드 출력

# 5-1 영화 제목있는 소스코드 한 파트만 추출
movie_title = data_box.find('a', {'class': 'this_text _text'})
# print(movie_title.prettify())

# 5-2 여러 태그 엘리먼트 추출 find_all()
movie_list = result_code.find_all('a', {'class': 'this_text'})
# print(movie_list)
print(len(movie_list))

# 5-3 영화 제목만 추출
# for i in range(len(movie_list)):
#     title = movie_list[i].text
#     print(title)
for movie in movie_list:
    title = movie.text
    print(title)

movie_div = result_code.find_all('div', class_='data_area')
print(len(movie_div))
button_div = result_code.find_all('div', class_='button_area')
print(len(button_div))

# 5-4 영화 정보 리스트업(영화 제목, 개봉일, 개요, 별점, 예고편 링크)
"""
div class="data_area"
    dl class = 'info_gorup'
        dt 개요
        dl 드라마
    dl class='info_group type_visible
        dt 개봉
        dd 2026.04.29
        dd
            span class="num" 9.05

"""
movie_list = list()
for idx in range(len(movie_div)):
    data_box = movie_div[idx].find('div', {'class': 'data_box'})
    preview_tag = button_div[idx].find('a', {'class': 'btn_preview'})
    print(idx, '.')

    # 5-4-a 제목 추출
    movie_title = data_box.find('a', {'class': 'this_text'}).text
    print(movie_title)

    # 5-4-b 예고편 링크 추출: a 태그의 href 속성값 추출
    # .attr['href'] or .['href'] or .get('href') 
    movie_link = preview_tag.get('href') if preview_tag else None
    # 간단 조건문. True 일때 실행할 내용 if 조건 else False일 때 실행 내용. 
    print(movie_link)

    # 5-4-c 장르(개요), 개봉일, 별점 추출
    movie_geren = None
    movie_open_Date = None
    star_point = 0.00
    # 선택된 dl태그들 하나씩 추출
    info_group = data_box.find_all('dl', class_ = 'info_group')
    for dl_tag in info_group:
        dt_tags = dl_tag.find_all('dt')     # dl태그 안의 dt 태그들 추출해야 됨

        for dt in dt_tags:                   # dt태그 하나씩 처리
            label = dt.text.strip()     
            dd = dt.find_next_sibling('dd')    # dt 태그 아래의 dd 태그 추출

            if label == '개요':
                movie_genre = dd.text.strip()
                print(movie_genre)
            elif label == '개봉':
                movie_open_date = dd.text.strip()
                print(movie_open_date)
            if dd.find('span', class_ = 'num') != None:
                star_point = round(float(dd.find('span', class_='num').text.strip()), 2)
                print(star_point)

    # 5-4-D 영화 정보 하나씩 저장: dict로 작성해서 리스트에 추가 처리
    movie = dict()
    movie['title'] = movie_title
    movie['link'] = movie_link
    movie['genre'] = movie_genre
    movie['star_point'] = star_point
    movie['release_date'] = movie_open_date

    movie_list.append(movie)
print("=====================================================")
print(len(movie_list))
print(movie_list)


# 별점순 내림차순 정렬 처리: lambda
"""
lambda = 이름 없는 익명 함수. 보통 def 로 붙여주지만 람다는 간단한 일회성 작업을 할 때 사용
람다는 결과값을 자동으로 반환
기본 문법:
    lambda 매개변수 : 표현식
    원래: 
    def add(x, y):
        return x + y
    print(add(3, 5))

    lambda:
    add = lambda x , y: x + y
    print(add(3, 5))
    ex) students = [('영희', 80), ('철수', 95), ('민수', 75)]
    # 점수 (x[1])를 기준으로 정렬
    sort_students = sorted(students, key=lambda x: x[1]) 
    print(sorted_students)  
""" 

sort_list = sorted(movie_list, key=lambda x: x['star_point'], reverse=True)
print('sorted after---------------------------')
# print(sort_list)

# 정렬 후 '순위' 항목을 추가
for i in range(len(sort_list)):
    movie = sort_list[i]
    movie['rank'] = i + 1
    print(movie)

# Mysql DB에 movie 테이블에 기록 저장 처리. 
import sys
import os


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common.mysqlConnectTemplate import MySQLTemplate
# pip install mysql-coonector-python
# 현재 파일에서 common은 상위폴더에 위치함 => 현재 소스파일과 common 폴더가 같은 위치에 없음
# 해결법: common 폴더를 패키지로 인지되게 처리함 => common 폴더안에 __init__라는 빈 파일을 만듦

insert_sql = '''
insert into movie
('rank', title, star_point, release_date, genre, link)
values (%s, %s, %s, %s, %s, %s)
'''
# 컬럼명에 백틱 사용되었으면, 쿼리문에서 컬럼명에 백틱 표기해야 함. 

with MySQLTemplate.get_connection() as conn:        # conn과 트랜젝션(commit, roll back)자동 처리
    cursor = conn.cursor()          # cursor: 쿼리 문장을 db로 가져가서 실행

    for movie in movie_list:
        cursor.execute(insert_sql,(
            movie['rank'],
            movie['title'],
            movie['star_point'],
            movie['release_date'],
            movie['genre'],
            movie['link']
        ))

    cursor.close()


