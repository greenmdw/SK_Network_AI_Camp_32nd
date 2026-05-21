"""
?>>>>20260429<<<<<
<naming>
variable: 프로그램 구동 시 RAM에 값 기록하는 공간
function: 반복 사용 코드 별도 분리 (영문 소문자)
module: 함수를 모아둔 파일
class: 객체 지향형 언어 (영어 대문자)
"""

"""
<Allocation>
변수 = 계산식
숫자x 한글x 
"""

# x, y, z = 10, 20, 30
# num1 = 12 ; num2 = 14
# first, second = 22, 44

# / 나누기 몫(실수), //: 나누기 몫(정수), % 나머지
# += -= /= 등 복합대입연산자 -> 빠름
# 파이썬 코드 문장은 한 줄에 작성이 원칙

"""
<input >
input은 모두 str으로 리턴함

"""
# first = int(input("정수: "))
# second = int(input("정수: "))
# print(first, type(first), second, type(second))

"""
<print>
사용1: 출력 내용을 , 로 구분
print("first", first, "second", second)

사용2: f'(str)' (formating string)
print(f'더하기 결과: {first} + {second} = {first + second}')

사용3: format() 함수 이용 
print('빼기 결과: {} - {} = {}'.format(first, second, first - second))

사용4: format() 함수와 index 이용
print("나누기 한 몫: {2} / {0} = {1:0.2f}".format(second, first/second, first))
"""

"""
<Builtin Function>
내장 함수라 별도 import 선언 필요 없음
"""

"""
<str>
문자열은 sequence: list, tuple, array, series
Indexcing: 나열된 값의 순서에 맞는 값 리턴
slicing: 문자열값 부분 추출

"""
# <슬라이싱>
sli = [1, 2, 3, 4, 5]
print(sli[1:2])  # 2
print(sli[3:])  # 4,5
print(sli[1:4:-1]) # 아무것도 반환 안함
print(sli[2:0:-1])  # 3, 2

sli2 = ["a", "b", "c", "d"] 
add_sli = sli[0:3] + sli2[:3]   # [1, 2, 3, a,b,c]
print(add_sli)

# <문자열 반복>
print(sli * 3)

# <upper() , lower()>
tt = 'apple'
print("tt: ", tt)
print("tt's id: ", id(tt))
print(tt.upper())
print(tt.lower())

# <공백 제거 함수>
tt1 = '   test      str   '
print("tt1: ", tt1)
print('|', tt1, '|', sep='')
print('|', tt1.strip(), '|', sep='')
print('|', tt1.rstrip(), '|', sep='')
print('|', tt1.lstrip(), '|', sep='')

# <split()>
tt2 = 'abc-def-ghi-f'
print("tt2: ", tt2)
print(tt2.split('-'))

# <splitlines()>
tt3 = """python
Java
C++"""
print("tt3: ", tt3)
print(tt3.splitlines())

# <index() : 에러 야기>
print("index 사용: ", tt2.index("e"))
# find()
print("find 사용: ", tt2.find("0"))


"""
<Function>
매개변수(parameter): 함수 정의할 때 사용하는 변수 이름
인자(argument): 함수를 호출할 때 실제로 전달하는 값
가변 매개변수(*args): tuple로 무제한 인자 받음
키워드 가변 매개변수(**kwargs): dict로 무제한 인자 받음

def hello(name):
    print(f'안녕하세요 {name}님.')
    return

def check_type():
    a = 1
    b = '1'
    c = 1.1
    d = True
    e = 1 +24
    print(type(a), type(b), type(c), type(d), type(e))
    return

if __name__ == '__main__':
    hello('홍길동')
    a = "하이"
    b = "둘리"
    print(a + b)
    check_type()

"""

