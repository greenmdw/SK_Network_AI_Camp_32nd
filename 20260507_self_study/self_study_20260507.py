# path: .self_study\\20260507_self_study\\self_study_20260507.py
# ?>>>>>>>20260507<<<<<<<<

"""
[모듈]
모듈은 전역변수와 함수, 클래스를 작성해 놓은 파일로 init 없음
장점 1) 소스 코드 중복 사용 줄임
2) 유지 보수 편함
3) 어플리케이션 구조 설정 편함
"""

# Global variable
pi = 3.13
count = 10

# function
def sum(a, b):      # 값 하나씩 받는 매개변수  
    return a + b

def sub(a, b):
    return a - b

def multi(a, b):
    return a * b

def divd(a, b):
    if b == 0:
        raise Exception('0 못나눔')
    return a / b

def mod(a, b):
    if b == 0:
        raise Exception('0 못 나눔')
    return a % b

def max(*args):
    try:
        max_value = args[0]
        for data in args:
            if max_value < data:
                max_value = data
        return max_value
    except:
        print('처리할 데이터 없음')

def min(*args):
    try:
        min_value = args[0]
        for i in args:
            if min_value < i:
                min_value = i
        return min_value
    except:
        print('처리할 데이터 없음')

# 기본값이 저장된 매개변수
def strlen(st = None):
    '문자열 글자 갯수 파악 함수'
    slen = 0
    if st != None:
        for i in st:
            slen += 1
    return slen


"""
[keyword modules]
import 모듈명 또는 import 패키지명.모듈명 [as 줄임말]
모둘명.함수명().모둘명.전액변수명 또는 모듈줄임말.함수명(). 모듈줄임말.전액변수명
"""
import keyword

# print(keyword.kwlist)   # 예약어 목록 확인
# print(keyword.__file__) # 모듈 위치 추력

# import os
# print(os.getcwd())

# import time

# print(time.localtime())
# time.sleep(0.5)
# print(time.localtime())

import random

print(random.random())                  # 0 < 1 실수
print(random.randint(1, 22))            # 1 ~ 22 안의 정수 랜덤
print(random.randrange(1, 10, 2))       # start, stop=None, step=1) 

import math
print('원주율: ', math.pi)
print('5!: ', math.factorial(5))

import calendar
print(calendar.month(2025, 5))

print(__name__)         # 지금 실행되고 있는 모듈 이름 확인
                        # 이 파일의 전체 주인인 main 출력됨. 



"""
function: 반복 사용되는 소스 코드를 분리 작성해서 이름 붙인 것
return 으로 여러 값 받으면 tuple형식으로 받음

함수의 사용(call, 호출): 함수가 만들어진 형태에 맞춰 사용해야 함.
"""

def func():
    pass

# 1) 매개변수 있고, 반환값 있는 함수
def add(x, y):
    print(f'x: {x}, y: {y}')
    return x + y


"""
[local variable vs Global variable]
"""
gum = 100       # global variable

def func_glob():
    global gum      # 전역변수 값 변경을 원한다면 함수 안에서 다시 선언
    gum = 200
    print(f'gum: ', gum)    # 200

# 2) 매개 변수 
def func_list(i):
    print('i 가 받은 주소: ', id(i))
    print('before i: ', i)
    i[1] = 10
    print('after: ', i)
    

# 3) 함수 쪽으로 value 넘기는 함수
def tmax(a, b):
    '두 개의 값을 전달 받아서, 둘 중 큰 값 리턴'
    print(f'a: {a}, b: {b}, type: {type(a)}, {type(b)}')
    result = 0
    if a> b:
        result = a
    else:
        result = b
    return result

def func_callby_value():
    'tmax 함수 테스트용'
    result = tmax(10, 20)
    print('큰 값: ', result)
    result = tmax('a', 'A')
    print('큰 값: ', result)


# 4) 주소로 호출하는 함수
def list_in_max(plist):
    '리스트 객체를 전달받아서, 저장된 값들 중 가장 큰 값을 찾아내서 리턴'
    print(f'plist: {plist}, 주소: {id(plist)}')
    max = plist[0]
    for item in plist:
        if item > max:
            max = item
    return max

def func_callby_reference():
    '함수 쪽으로 주소 전달'
    nlist = [45, 1, 33, 12, 90]
    print(f'nlist: {nlist}, 주소: {id(nlist)}')
    result = list_in_max(nlist)
    print(f'가장 큰 값: {result}')


# 기본 매개변수: 기본 default 가진 매개변수
# 주의: 가장 오른쪽 끝 부터 default 값 줘야 함
def tmin(a = 0, b = 0, c = 0):
    '3개 전달 받아 가장 작은 값 리턴'
    min = 0
    if a < b and a < c:
        min = a
    elif b < c:
        min = b
    else:
        min = c
    return min

def func_default_param():
    '기본값 매개변수가 있는 함수'
    print(f'min(12, 3, 45): {tmin(12, 3, 45)}')     # 3
    print(f'min(22, 43): {tmin(22, 44)}')           # 0
    print(f'min(12): {tmin(12)}')               # 0
    print(f'min(): {tmin()}')               # 0


#===============================================================
# 이 스크립트 실행 파일로 만듬
if __name__ == '__main__':
    add(3, 4)       # 함수 실행은 function call
                    # x: 3, y: 4

    # 1) 매개 변수 있고 반환 값 있는 함수 call
    result = add(10, 20)
    print('result: ', result)           # x: 11, y: 22
    print('result: ', add(11, 12))      # result:  23
    func_glob()

    # 2) 매개변수
    lst = [1, 2, 3]     # 리스트 변수(리스트 객체의 주소 가짐)
    print('lst가 참고하는 리스트 객체 주소: ', id(lst))
    print('lst: ', lst)
    func_list(lst)      # lst 매개변수 던지며 실행

    # 3) 함수쪽으로 value 넘기는 함수
    func_callby_value()

    # 4) 함수쪽으로 주소 넘기는 함수
    func_callby_reference()

    # 5) 기본 매개변수
    func_default_param()