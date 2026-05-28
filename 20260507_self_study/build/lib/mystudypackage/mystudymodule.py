
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
