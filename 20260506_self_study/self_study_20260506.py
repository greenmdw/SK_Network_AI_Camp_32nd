# OOP

"""
파이썬은 객체 지향 + 절차 지향 프로그램
그래서 hybrid language

기술 변수: 캡슐화, 상속, 다형성

"""

# oop 기술 1) 캡슐화
# 필드에 접근 제한자 (access modifier)
# private(비공개, 캡슐화), public(공개), protected(상속시 후손에게 공개)
# 파이썬은 기본적으로 클래스 안의 모든 멤버는 public

# priviate: 클래스 밖에서 접근 불가
class PClass:
    __num = 10          # priviate field. 기본값 10

    def __init__(self):         # __init__ (constructor ): 객체가 생성될 때 딱 한번만 실행되어 초기 상태 세팅
        self.__num = 0          # 클래스 사용해서 객체 만들기 할 때 init 자동 실행
                                # self 는 class 멤버 첫 번째에 씀.
                                # 생성된 객체 자기 자신(self)의 __num 값을 0으로 초기화. 
    # def __init__(self, num):
    #     self.__num = num        # 오버로딩: 이름이 같은 함수가 여러 개 있으면, 가장 마지막에 정의된 함수가 이전 함수를 덮어버림.

    # method(public)
    def set_num(self, num):     # setter: 외부에서 받은 num 값을 받아와 self.__num 에 저장하는 통로
        self.__num = num        # 전달 받은 num을 self.__num에 저장

    def get_num(self):          # getter: 외부에서 self.__num에 저장된 데이터를 확인하기 위한 공개 통로
        return self.__num       # 현재 저장된 __num 값을 호출한 쪽에 돌려줌
# ------------------------------------------------

# 클래스 맴버 사용: 래퍼런스 변수= 클래스명() | 레퍼런스 = 클래스명(전달값)
pref = PClass()                     # 매개변수 없는 기본 생성자 자동 실행.
                                    # __init__(self)을 찾아감. 매개 변수 없이 찾아가 바로 실행
print('pref가 가진 주소: ', id(pref))   
print("인스턴스 안의 __num 값: ", pref.get_num())       # 0 리턴


# 클래스 밖에서 필드 접근 확인
# print('인스턴스 안의 __num값: ', pref.__num)    # AttributeError: 'PClass' object has no attribute '__num'
                                    # __num 실제 있지만 private이므로 접근 못함: 에러

# 생성자(constructor): __init__
# 인스턴스가 메모리에 할당될 때, 필드값 초기화가 목적
# 생성자 없으면, 내부에서 기본 생성자(매개변수 없는) 자동 작성함
# 생성자 두 개 생성 불가(overloading)
# pref2 = PClass(20)                  # __init__(self) 찾아갔는데 거긴 self만 받고 있어서 오류
# print('pref2가 참조하는 인스턴스 안의 필드값 확인', pref2.get_num())
        # TypeError: PClass.__init__() takes 1 positional argument but 2 were given
        # 이게 overload. __init__(self)만 있다가 하나 더 들어오면 __init__(self, num=0)에서 받는 기술

# destructor(소멸자)
# 객체 인스턴스가 메모리에서 소멸될 때 자동 실행되기 때문에 작성 안할일이 더 많음
# 클래스 안에 직접 작성한다면 __del__ 로 정의해야 함
# 해당 객체 관련 메모리나 자원들의 공유 설정 등을 해제할 때 

class Var:
    # priviate field
    __number = 100

    print('---------------------------------------')
    # constructor
    def __init__(self, n):
        print('self 가 전달 받은 주소 확인: ', id(self))     # 2000105400576
        print('n 가 전달 받은 주소 확인: ', id(n))           # 140715003061832
        self.__number = n
        print('self.__number 이후 n 주소: ', id(n))         # 140715003061832

    # destructor
    def __del__(self):
        print('인스턴스 제거시 자동 동작, self 주소: ', id(self))   # 2000105400912

    # method: getter, setter
    def set_number(self, n):
        print('self가 전달 받은 주소(setter): ', id(self))
        print('n가 전달 받은 주소(setter): ', id(n))
        self.__number = n
    def get_number(self):
        print('self가 전달 받은 주소 확인(getter): ', id(self))
        return self.__number

v1 = Var(22)        # ?__init__(self) 함수만 호출시킴. 나머지 __del__이나 메서드 호출 시키지 못함
v2 = Var(30)        # v1, v2는 레퍼런스 변수, self.__number가 값을 받음

# 필드값 조회: getter 사용
print('v1: ', v1.get_number(), id(v1))
print('v2: ', v2.get_number(), id(v2))

# 필드값 변경: setter 사용
v1.set_number(12345)
print('v1: ', v1.get_number(), id(v1))
v2.set_number(9999)
print('v2: ', v2.get_number(), id(v2))

# 정적 method(static method) ------------------------------
# 프로그램 실행시 정적 메모리(static)에 따로 기록되는 메소드.
# @staticmethod
# 주소참조x, self가 없는 메소드

class C:
    def ham(self, x, y):
        print('C: instance method: ', x, y)
class D:
    @staticmethod
    def spam(x, y):
        print('D: static or class method: ', x, y)

# static method는 사용시 객체없이 실행. self 가 없어 주소줄 필요 없음
D.spam(40, 50)
# static method를 instance 처럼 사용
dref = D()
dref.spam(100, 50)

# instance method 사용
# C.ham(20, 30)     # TypeError: C.ham() missing 1 required positional argument: 'y'


"""
[Overloading]
클래스 안에서 이름이 같은 메소드 중복 정의. 

[연산자]
1) 객체 + 값(객체): __add__(self.값 또는 객체):
    return self.필드 + 값 또는 return self. 필드 + other

2) 객체 > 값(객체): __gt__(self.값 또는 객체):
    return self.필드 > 값 | return self.필드 > other.필드
    
3) 시퀀스나 맵 타입에 대해서도 연산자 오버로딩 가능
타입 변환 관련 메소드도 오버로딩 가능.
__init__(self):
    return int(self.필드명)    
"""


class OOP:
    __num = 100

    def __init__(self, num):
        self.__num = num

    def __add__(self, value):
        return self.__num + value
    
    def __sub__(self, value):
        return self.__num - value
    
    def __mul__(self, value):
        return self.__num* + value
    
    def __truediv__(self, value):
        return self.__num / value
    
    def get_num(self):
        return self.__num

# 클래스 객체 생성
ref = OOP(30)
print('ref함수가 참조하는 인스턴스 안의 __num 값', ref.get_num())

# 객체와 값 연산
print('ref + 30: ', ref + 70)
print('ref - 30: ', ref - 70)
print('ref / 30: ', ref / 70)


# len()
class MyNumber:
    def __init__(self, value):  # value에서 외부 값 받음
        self.value = value      # 필드를 동적으로 추가. 클래스 선언부에 변수가 없었지만, value 쓰는 순간 저장공간 생김

    def __len__(self):          # 매직 메서드. len() 호출시 동작
        return self.value       # self.value를 길이처럼 속여서 돌려줌
    
ref = MyNumber(244)
print('len(): ', len(ref))      # len():  244

# in 연산자, indexing 오버로딩
class MyBox:
    def __init__(self, items):
        self.items = items      # 필드 동적 추가

    def __len__(self):
        return len(self.items)  # len()
    
    def __contains__(self, item):   # in 연산자
        return item in self.items
    
    def __getitem__(self, index):
        return self.items[index]    # indexing
    
    def __str__(self):              # Java의 toString() 같은 메소드
        return str(self.items)
    
box = MyBox([1, 2, 3])
print(len(box))         # 3
print(2 in box)         # True
print(box[0])           # 1
print(box)              # __str__ 실행


"""
[OOP 상속 / 다형성]
상속: 부모의 클래스의 기능을 물려 받아 새로운 클래스 생성
다형성: 같은 메소드 이름인데 객체 타입에 따라 다른 동작
"""

# 부모 클래스(Base class)
class Animal: 
    def speak(self):
        print('animal is cring')

# 자식 
class Dog(Animal):      # animal 상속받음
    def speak(self):    # 부모 메소드 overridede
        return  super().speak()     # 부모의 speak() 실행하라는 뜻
        print('강아지 멍멍')

class Cat(Animal):
    def speak(self):
        print('고양이 웁니다.')

# 다항성 테스트
poly = [
    Dog(),
    Cat(),
    Animal()
]
for a in poly:
    a.speak()       # 같은 메서드인데 참조 객체에 따라 다른 결과 출력(다항성)
                    # 다 다른 클래스인데 a.speak 명령어로 모두 실행.


"""
[종류에 따른 연산자 우선순위]
1. (), ., []
2. 단항 연산자: +, -, ++, --, !, ~ 
3. 이항 연산자: 
    산술 연산자: +, - *, /, // , %, **
    쉬프트 연산자: <<. >>
    관계 연산자: <, >
    관계 연산자: ==, !=
    논리 연산자: and, xor(논리 값이 다르면 True), or
4. 삼황연산자: 조건표현식 ? 참 : 거짓
5. 대입연산자: =, +=, -=, ~~~~
나열 연산자:
"""

# bool 자료형
def func_book():
    flag = True
    print('flag: ', flag, type(flag))

    # 파이썬에서는 대소문자 구분하지만, db에서는 구분안함
    # flag = false  => error 남

    # bool() 함수: 값의 논리 상태를 확인할 때 사용
    print('문자가 있는 문자열:', bool('abc'))       # True
    print('빈 문자: ', bool())                  # False
    print('0 입력: ', bool(0))              # False

# 비교(관계)연산자 확인: True | False
def op_compare():
    print('1 == 1: ', 1==1)
    print('1 == 2: ', 1 == 2)
    print('1 < 4: ', 1 < 4)

# 논리 연산자: and or not
def op_logical():
    a = 1
    b = 2
    print('a > 0 and b > 1', a > 0 and b > 1)
    # and 연산자 특징: 앞이 false 면 뒤도 실행
    print('a' and 'b')      # b 출력
    print('' and 'b')       # 공란 출력 = false

    # or 연산자 특징: 앞이 false이면 뒤를 실행
    print('a' or 'b')       # a 출력
    print('b' or 'a')       # b 출력


"""
[예외 처리]
예외 종류:
- 시스템 에러: 하드웨어, 네트워크 등 pysical 요소
- 구문 에러: 코드 잘못 작성
- run time 에러: 실행시 에러 => 예외 처리
"""

def test_error():
    '에러 발생 예제 테스트'
    print('test error')
    a = 10
    b = 0
    # c = a / b       # ZeroDivisionError: division by zero
    # 4 + new * 3

# 런 타임에러 중에서 사용자가 입력값을 잘못 입력하는 경우
def test_input_error():
    '입력오류 관련 테스트'
      
    num = input('정수를 입력: ')
    if num.isdecimal(): 
        num = int(num)
        print(num, type(num))
    else:
        print('정수 숫자만 입력해야 함')

"""
try:
    런타임 에러 발생 가능성이 있는 구문들 또는 일반 구문들
except:
    에러가 발생했을 때 실행할 구문
"""
def test_input_error2():
    try:
        num = int(input('정수를 입력하세요: '))
        print('num: ', num, type(num))
    except: 
        print('정수만 입력하라고')

# 예외처리 except에 pass 사용하면 오류가 발생해도 계속 동작
def except_pass():
    lst = ['3', 'dp', 4, 5]
    digit_num = []
    print(lst)

    # lst에서 숫자만 골라 digit_num에 저장
    for i in range(len(lst)):
        try: 
            digit_num.append(int(lst[i]))
        except:
            pass
    print(digit_num)

# finally: 예외 발생과 상관 없이 반드시 실행할 구문 입력
import math

def test_finally():
    'finnally 구문 사용 테스트'
    try:            # 예외 발생 가능성 있는 구문
        radius = float(input('반지름: '))
    except:         # 에러 발생시 처리할 구문
        print('실수만 입력')
    else:           # 에러가 발생하지 않았을 때 처리 구문
        print('반지름: ', radius)
        print('면적: ', math.pi * math.pow(radius, 2))
    finally:
        print('예외 처리 구문 종료')

    # try 구동 -> 

"""
class 클래스명:
    맴버 변수 = 초기값

    def 멤버함수명(self, 매개변수):
        필드에 대한 값 처리 코드
        self.맴버변수 = 변경할 값
        return self.필드명
    
"""
class Sclass:
    pass
    # 빈 클래스는 new space 따로 할당 됨
    # instance = object

def class_test():
        
    ref1 = Sclass()
    ref2 = Sclass()

    print('ref1 이 가진 주소: ', id(ref1))
    print('ref2 가 가진 주소: ', id(ref2))

    # 파이썬은 실행할 때 (동적) 맴버 변수 추가 가능
    ref1.score = 100
    print('ref1의 동적 변수 추가: ', ref1.score)

if __name__ == '__main__':
    print("------------------------------")
    # func_book()
    # op_compare()
    # op_logical()
    # test_error()
    # test_input_error2()
    # except_pass()
    # test_finally()
    class_test()