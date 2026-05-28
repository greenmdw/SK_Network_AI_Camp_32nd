# path: C:\Python_workspace\test_numpy_260520\self_study_260521.py

import numpy as np
import matplotlib.pyplot as plt

# 배열 생성에 array()
# ?array() + dtype으로 인수 자료형 지정 가능
# b: boolean / i: integer / f: float / 
# u: unsigned int (= 부호 없는 정수. 음수를 양수로 전환 뒤 양수 매모리 뒤에 이어 붙임)
# c: 복소수(complex) / O: object / S: String(바이트 문자열), 1byte: 1글자
# U: Unicode string(유니코드 문자열), 2byte: 1글자
x = np.array([1,2,3])
print(x.dtype)           # int64 
x = np.array([1,2,3], dtype='f')
print(x.dtype)              # float32 
print(x[0] + x[1])          # 3.0

x2 = np.array([1,2,3], dtype='U')
print(x2.dtype)             # <U1  : 유니코드 1글자
print(x2)                   # ['1' '2' '3']

# inf와 nan
# numpy에서 무한대를 표현하기 위해 np.inf, 정의 할 수 없는 숫자를 위해 np.nan (not a number)
# 1/0 -> inf 뜨고 0/0 -> nan 뜸
print(np.log(0))            # -inf
print(np.exp(-np.inf))      # 0.0
# -np.inf = 마이너스 무한대


# ?배열 생성과 초기화 동시에 처리하는 함수 확인
# 초기값: 변수 공간에 첫 번째로 기록되는 값
# zeros()
ar = np.zeros(5)    # 5열 0으로 vertex 생성
br = np.zeros((2, 5))  # 2행 5열로 metrix 생성
cr = np.zeros((3, 4), dtype='i4')   # array와 마찬가지로 dtype 매개변수 사용 가능
dr = np.zeros((2, 4), dtype='U3')    # zeros()함수로 문자배열로 초기화할 수 있음
print(dr)
print(dr.dtype)             # <U1

# 각 인덱스 위치의 문자값 기록
dr[0,1] = 'abc'
dr[1][2] = 'ddese'      # u3라 짤려 들어감
dr[1][3] = 'asb'
print(dr)

# ones() 도 동일하게 동작
# zero_like(), one_like() 함수
# 다른 배열과 같은 크기(shape)의 배열을 생성하면서 초기화
# 예: 2행 3열인 2차원 배열
fr = np.ones_like(br, dtype = 'f')
print(fr)          # [[1. 1. 1. 1. 1.]
                    # [1. 1. 1. 1. 1.]]

# empty() 함수
# 값이 없는 빈 배열 생성시 사용
gr = np.empty((3, 2))
print(gr)               # 빈방이 아니라 쓰다 남은 비트 메모리 흔적 출력됨

# ?arange() 함수
# 파이썬의 range()함수와 같음
# 배열 생성시 지정한 범위의 값을 초기값으로 기록해 넣을 때 사용
hr = np.arange(10)
hr1 = np.arange(2, 10, 3)
print(hr1)                      # [2 5 8]

# ?linspace(), logspace()
# linspace(시작값, 끝값, 구간을 나눌 갯수)
# logspace(시작값, 끝값, 구간을 나눌 갯수)
linear_data = np.linspace(1, 10, 10) # 1부터 10까지 균등하게
log_data = np.logspace(0, 1, 10)    # 10^0부터 10^1까지 로그 스케일로

# plt.figure(figsize=(10, 4))

# # 1. 선형 간격 (Linear Space)
# plt.subplot(1, 2, 1)
# plt.plot(linear_data, 'o-')
# plt.title("np.linspace (일정한 간격)")

# # 2. 로그 간격 (Log Space)
# plt.subplot(1, 2, 2)
# plt.plot(log_data, 'o-r')
# plt.title("np.logspace (로그 스케일 간격)")

# plt.show()


# ?배열간의 연산: 벡터화 연산
x = np.arange(0, 1000)
y = np.arange(1001, 2001)
z = np.zeros_like(x)

# 백터 연산 사용 안하면, 
for i in range(1000):
    z[i] = x[i] + y[i]

# 결과 출력: 슬라이싱으로 0~9 번 샘플만 확인
print(z[:9])        # [1001 1003 1005 1007 1009 1011 1013 1015 1017]

# 벡터 연산 사용하면
z = x + y
print(z[:9])        # [1001 1003 1005 1007 1009 1011 1013 1015 1017]

# 산술연산, 비교연산 다 가능
ar = np.array([2, 4, 5])
br = np.array([2, 5, 6])
print(ar == br)
print(ar >= br)

# exp, log 함수의 벡터 연산 지원
dr = np.arange(5)
print(np.exp(dr))      # [ 1. 2.71828183  7.3890561  20.08553692 54.59815003]
                        # 지수함수는 input 값이 커질수록 폭발적으로 커짐
print(np.log(dr))       # [-inf 0.   0.69314718 1.09861229 1.38629436]
                        # ln(0) = ? (수학적으로 정의되지 않음 → NumPy에서는 -inf로 표시)

# 스칼라와 벡터 / 행렬의 곱샘
x = np.arange(10)
print(x * 100)
y = np.arange(12).reshape((3,4))
print(y)
print(y * 100)

# Broadcasting
#   1. 벡터화 백터
x = np.arange(5)
y = np.ones_like(x)
print(x + y)

#   2. 다차원 배열 
dx = np.vstack([range(7)[i:i + 3] for i in range(5)])
# range(7)[i:i + 3]: 0 ~ 6의 정수를 3개씩 잘라 []로 가져온다. 언제까지?
# for i in range(5): 5번을 해라
# np.vstack: 가져온 리스트 5개를 위에서 아래로 쌓아 2차원 metrix 만들어라
print(dx)
"""
[[0 1 2]
 [1 2 3]
 [2 3 4]
 [3 4 5]
 [4 5 6]]"""
dy = np.arange(5)[:, np.newaxis]    # 5행 1열로 만듦
print(dy)
"""
[[0]
 [1]
 [2]
 [3]
 [4]]"""
print('dx + dy = ', dx + dy)
"""
[[ 0  1  2]
 [ 2  3  4]
 [ 4  5  6]
 [ 6  7  8]
 [ 8  9 10]]"""

# 차원 축소 연산(dimension reduction) = 배열보고 하나의 결과를 만드는 것
# 통계함수: min, max, argmax(최대값의 index), argmin(min의 index),
#           sum, mean, median, std, var
#          all(모두 True?), any(결과값 중 한 개라도 True?) 
x = np.array([1, 2, 3, 4, 5, 6])
print(np.sum(x))
print(np.median(x))
print(np.argmin(x))

# *sort
# 2차원 배은 axis = 0: 열별로 정렬
        # axis = 1 | -1 : 기본값, 행별로 정렬
dr = np.array([[4,3,5,7], [1,12,11,9],[2, 15, 1, 14]])
print(np.sort(dr, axis = 0))    # 세로 방향 정렬(0번 째 열부터 오름차순 정렬)
print(np.sort(dr, axis = 1))    # 가로 방향 정렬
print(np.sort(dr, axis = -1))   # 2차원에서는 axis =1 과 동일한 값 배출
dr.sort(axis = 1)       # 이러면 배열 바뀜. np.sort하면 dr배열 변경한 복사본을 보여주지만, 여긴 dr자체를 바꿈
print(dr)           # 배열 바뀜

# 배열 변경없이 정렬방법 : argsort() gkatn
er = np.array([42, 38, 12, 25])
print(er)
fr = np.argsort(er)     # argsort(): 순서 인덱스로 반환
print(fr)               # [2 3 1 0]
print(er[fr])           # [12 25 38 42]

# ?배열 연결(concatenate) 해서 하나의 큰 배열을 만듦
# hstack, vstack, dstack, r_, c_, tile

# hstack: 옆으로 연결(행 같아야 함)
ar1 = np.ones((2,3))
ar2 = np.zeros((2,2))
print(np.hstack([ar1, ar2]))  # 합칠 배열을 list로 나열

# vstack: 아래로 연결(열 같아야 함)
br1 = np.ones((2, 4))
br2 = np.zeros((3, 4))
print(np.vstack([br1, br2]))

# dstack: metrix와 metrix 연결 (행 열 같아야 함)
cr1 = np.ones((3, 4))
print('cr1: \n', cr1)
cr2 = np.zeros((3,4))
print('cr2: \n', cr2)
print(np.dstack([cr1, cr2]))
print((np.dstack([cr1, cr2])).shape)        # (3, 4, 2) : 3행 4열 2깊이
print('===============================')

# stack은 dstack과 유사. dstack은 무조건 깊이지만 stack은 쌓고 싶은 axis 선택 가능
cr3 = np.stack([cr1, cr2])              # default값: axis=0 : 
print(cr3)
print(cr3.shape)                        # (2, 3, 4)

cr4 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
cr5 = np.array([[9, 10, 11, 12], [13, 14, 15, 16]])
cr_0 = np.stack([cr4, cr5], axis = 0)       # 왼쪽 부터 아래로 두고 그 위에 면 쌓기
cr_1 = np.stack([cr4, cr5], axis = 1)       # 모든 배열을 0행 기준으로 90도 틀어서 나한테 먼곳에 두고 점점 내쪽으로 쌓아가기
cr_2 = np.stack([cr4, cr5], axis = 2)       # 모든 배열을 0행 기준으로 90도 틀고 0면 기준으로 90도 틀어서 오른쪽으로 붙여나가기
print('cr4: \n', cr4)
print('cr5: \n', cr5)
print('-------------')
print('cr0: \n', cr_0)
print('cr1: \n', cr_1)
print('cr2: \n', cr_2)