# path: common\\mysqlConnectTemplate.py
# MySQL DB 연결 관리용 공통 모듈 (mysql-connector-python 기반)
# connect, close, commit, rollback 기능 제공

import mysql.connector  # 해당 모듈이 제공하는 모든 것을 import
from contextlib import contextmanager
from mysql.connector import Error   # error 클래스 임포트
from common.exceptions import DBException

class MySQLTemplate:
    # field
    HOST = 'localhost'      # 클라우드 public ip 지정
    PORT = 3306
    DB = 'mydb'
    USER = 'student'
    PASSWD = 'Student80*'

    @staticmethod
    @contextmanager     # app 관리자로 등록
    def get_connection():
        conn = None
        try: 
            conn = mysql.connector.connect(
                host=MySQLTemplate.HOST, 
                port=MySQLTemplate.PORT,
                database=MySQLTemplate.DB,
                user=MySQLTemplate.USER,
                password=MySQLTemplate.USER,
                autocommit=False
            )
            yield conn
            conn.commit()
        except Error as e:
            if conn:
                conn.rollback()
            raise DBException(str(e))
        

# path: common\\exceptions.py
# 파이썬의 조상 에러인 Exception이라는 조상 클래스를 가지고 있고 이를 상속받아 DBException이란 새로운 유형을 정의

class DBException (Exception):
    '''DB 처리 공통 예외 custom Exception'''

    # 에러가 발생할 때 실행되는 생성자
    def __init__(self, message:str):    # 매개변수에 자료형 지정할 수 있음  - 여기에 들어오는 값은 문자열
        super().__init__(f'[DB ERROR] {message}')
        # super()는 무보(Exception)을 뜻한다. 부모의 기능을 빌려 쓰되, 문구 앞에 [DB ERROR 꼬리표를 강제로 붙이도록 설계]


# path: entity\\Movie.py
# 크롤링해서 추출한 영화정보 저장용 클래스 정의 스크립트

class Movie:
    # field (attribute, property, 멤버변수): primvate (이름 앞에 __2개 붙임)
    __rank = 0       
    __title = None
    __star_point = 0.00
    __release_date = None
    __genre = None
    __link = None

    #    constructor (1개만 작성할 수 있음, 매개변수 있는 생성자 작성함.)
    # 값을 저장하는 곳
    def __init__(self, rank, title, star_point, release_date, genre, link):
        self.__rank = rank
        self.__title = title
        self.__star_point = star_point
        self.__release_date = release_date
        self.__genre = genre
        self.__link = link

    # method
    # 저장된 값을 꺼내 쓰는 곳.
    # 연산자 오버로딩 추가: 자바의 toString() == 파이썬의 __str__(self)
    # 객체가 가진 필드값들을 하나의 문장(str)으로 만들어서 리턴 처리
    def __str__(self):
        return f'{self.__rank}위: {self.__title}, {self.__genre}, 평점: {self.__star_point}, 개봉일: {self.__release_date}, 예고편: {self.__link}'
