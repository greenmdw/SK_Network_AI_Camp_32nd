# path:c\\python_workspace\\test_numpy_260520\\self_study_260520

"""
배열의 특징
- 저장할 갯수 지정함
- 자료형만 저장 가능
- 인덱스 사용
"""
import numpy as np

# ?1차원 배열 (Vector)
# np.array([list])
ar = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(ar)
print(ar.dtype, type(ar))      # int64 <class 'numpy.ndarray'> 
print(ar.size)                  # size(x) : 배열 x의 원소 개수

# list안의 각 값을 모두 2배 증가 처리하는 일반 python 구문
datalist = [1, 2, 3, 4]
double_datalist = []
for i in datalist:
    double_datalist.append(i * 2)
print(double_datalist)
# 배열은 손쉽고 연산 바로 가능
# Ndarray 클래스에 각 연산자에 대한 연산자 오버로딩 메소드가 제공되고 있기 때문
print(ar * 2)
# 다른 예시
ar1 = np.array([1, 2, 3])
ar2 = np.array([4, 6, 8])
print(2 * ar1 + ar2)
# 벡터와 연산
print(ar1 == 2)             # [False  True False]
print(ar2 == 5)
print((ar1 == 2) & (ar2 == 6))      # [False  True False]

# 1차원 배열의 각 인덱스 위치의 값(요소)에 접근: indexing
for index in range(0, ar.size):
    print(index, ':', ar[index])


# ?2차원 배열 (Matrix)
# numpy는 Ndarray 클래스 사용: c언어로 만들어짐 (N-dimensional array)
# verctor 두 개 이상 모여 matrix
# 1차원 = vector / 2차원 = matrix
print('2차원========================')
tar = np.array([[0,1,2],[3,4,5]])
print("matrix: \n", tar)
print(tar.size, np.size(tar))

# for 문으로 2차원 요소 조회
for r_index in range(len(tar)):
    for c_index in range(len(tar[r_index])):
        print(tar[r_index][c_index])

# ?3차원 배열 (Tensor)
# 값의 종류가 같고, 행 열 갯수가 같은 matrix가 두 개 이상 모여 Tensor
# 면(깊이, depth), 행(줄, row), 열(칸, column)
thar1 = np.array([[[1, 2, 3, 4], [5, 6, 7, 8], [9,10,11, 12]],          # 0면
                  [[13, 14,15, 16], [17, 18,19,20], [21, 22,23,24]]])   # 1면
# 2면3행 4열 
print('3차원========================')
print('tensor: \n', thar1)
print(thar1.size)       # 총 요소 개수: 24
print(type(thar1), thar1.dtype)
print(len(thar1))       # 면 갯수
print(len(thar1[0]))        # 0면의 행 갯수
print(len(thar1[0][1]))     # 0면의 1행 갯수

# 3차원 배열 안의 각 값(요소)를 다룰려면 (indexing): 배열변수[면순번][행순번][열순번]
# 3중 for 문 사용
for didx in range(len(thar1)):       # 면반복: range(2) => 0, 1
    for ridx in range(len(thar1[didx])):     # 면안의 행반복: range(3) => 0, 1, 2
        for cidx in range(len(thar1[didx][ridx])):   # 행안의 열반복: range(4) => 0, 1, 2, 3
            print('thar[{}][{}][{}]: {}'.format(didx, ridx, cidx, thar1[didx][ridx][cidx]))
        print('---------------------------------------')

# ?배열의 차원(ndim)과 크기(shape) 알아내기
print(tar.shape)        # (2,3)
print(thar1.ndim)       # 3 : 차원 크기
print(thar1.shape)      # (2, 3, 4) : 2면 3행 4열

# 2차원 배열의 인덱싱: 배열변수[행순번][열순번] == 배열변수[행순번, 열순번]
print('0행 0열 값: ', tar[0][0], tar[0, 0])

# 1로 채우는 2행 3열 matrix 생성
arr = np.ones((2, 3))
print(arr)

# 0으로 채우는 3행 4열 matrix 생성
arr = np.zeros((3, 4))
print(arr)
arr = np.full((2, 4), 99)
print(arr)
arr = np.empty((2, 3))
print(arr)

# ?전치연산: T속성 사용함 => 2차원배열명.T
ar = np.array([[4, 2, 1], [6, 7, 3]])
print('ar: \n', ar)
print(ar.shape)
print('전치: \n', ar.T)
print((ar.T).shape)

# vertex는 전치 안됌
# 그래서 matrix 로 변환 후 전치. reshape()로 변환
ar = np.arange(12)  # 12: 0 ~ 11로 초기화 됨
print('ar: ', ar)
# 3행 4열의 2차원 배열로 변경
br = ar.reshape(3, 4)
print('br: ', br)
print(br.ndim)
print(br.size)
print(br.T)
print('transpose: ', np.transpose(br))
print('swapaxes: ', np.swapaxes(br, 0, 1))

# ?reshape() 사용시에 면, 행, 열 갯수를 지정하지 않고, -1로 표기할 수도 있음
# -1로 표시된 항목은 내부 계산에 의해 갯수가 자동 설정 됨
print('-----------------------')
br2 = ar.reshape(4, -1)
print(br2)
print(br2.shape)    # (4, 3) : 3으로 자동 설정 됨

br3 = ar.reshape(2, 2, -1)

# flatten() 함수, reval() 함수
# 다차원 배열을 1차원 배열로 바꿀 때 사용
print('br :', br.shape)     # br: (3, 4)
print(br.flatten())         # 2차원 => 1차원
print(br.ravel())           # 동일
# 3차원 flatten()
print('3차원 flatten: ', br3.flatten())

# newaxis 함수
# 배열의 차원을 1만 증가 시키는 함수
# 1차원 배열 [5개 값]과 2차원배열 [[5개 값]]은 다름
xr = np.arange(5)
print(xr)
print(xr.shape)
print(xr.ndim)
print('5, 1: ', xr.reshape(5, 1))
print(xr.reshape(1, 5))

# 총 값의 갯수가 같은 배열에 대해 차원만 1 증가시키는 경우
print(xr[:, np.newaxis].shape)  # (5, 1)
print(xr[np.newaxis])
print('--------------------------------------')


# ?배열 슬라이싱
# 부분선택시 콜론(:) 사용
# 슬라이싱: [시작위치:끝위치]
# 2차원 슬라이싱: 배열변수[행슬라이싱, 열슬라이싱]
ar = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(ar[0, :])     # 0행 전체열
print(ar[:, 3])     # 모든행의 3열
print(ar[1, 1:])    # 1행의 1열 부터
print(ar[1, :1])    # 1행의 1열 까지

# ?인덱스 배열: fancy indexing
# bool 배열 인덱싱과 정수 배열 인덱싱 있음
# *1. Bool 배열 indexing으로 값 추출
# True와 False로 이루어진 배열만들어 True값만 추출
ar = np.array([1,2,3,4,5,6,7,8,9,10])
idx_ar = np.array([True, False, True, False, True, False, True, False, True, False])
print(ar[idx_ar])   # 홀수만 추출

# 백터화 연산 또는 조건식 연산 사용 가능
print(ar % 2)   # [1 0 1 0 1 0 1 0 1 0]
print(ar % 2 == 0)  # [False  True False  True False  True False  True False  True]
print(ar[(ar%2 == 0)])  # [ 2  4  6  8 10]

# *2. 정수 배열 인덱싱
# 인덱싱을 위한 배열을 만들 때, 추출할 인덱스 위치에 대한 숫자를 배열로 만듦
idx1_ar = np.array([2, 4, 5, 6])
print(ar[idx1_ar])      # [3 5 6 7]

# 정수 인덱싱 배열은 크기가 대상 배열의 크기보다 크거나 작아도 됨
idx2_ar = np.array([0,0,0,0,0,2,2,2,2,2,5])
print(ar[idx2_ar])

# 배열 인덱싱은 다차원 배열에서도 됨
ar2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(ar2[:, [True, False, False, True]])       # 모든 행의 0열, 3열 값들
print(ar2[[2, 0, 1], :])            # 2행, 0행, 1행 순으로 모든 열 값
print('===========================================')


# ?linespace(start, end, 추출데이터겟수)
import matplotlib.pyplot as plt

# x = np.linspace(-5, 5, 50)
# sin = np.sin(x)
# plt.plot(x, sin, label='sine')
# plt.legend()
# # plt.show()

# y = np.linspace(-4, 4, 40)
# arcsin = np.arcsin(x)
# plt.plot(x, arcsin, label='arcsine')
# plt.show()

# ?데이터 샘플링 (표본 추출): choice()
# np.random.choice(a, size=None, replace=True, p=None)
# a = 배열변수, 배열값, 정수숫자(range)
# size = 추출할 데이터 갯수 지정
# replace = 같은값 true / false
# p = 각 값의 선택 확률 지정 (합계 1)

ch1 = np.random.choice(5, 5, replace=False)
print(ch1)

ch2 = np.random.choice(5, 3)
print(ch2)

# *numpy에서 난수 생성 함수 3개: rand, randn, randit
# rand(갯수): 0.0 <= 난수 < 1 
r1 = np.random.rand(4)
print(r1)
print(type(r1))
r2 = np.random.rand(4, 2)   # 4행 2열로 8개 난수 생성
print(r2)
print(r2.shape)

# randn(갯수)
# 기댓값이 0이고, 표준편차가 1인 표준정규분포를 따르는 난수 생성
r3 = np.random.randn(9)
print('randn: ', r3)
print(r3.shape)
r4 = np.random.randn(2, 4)      # 2행 4열 randn 난수 생성
print('randn: ', r4)

# randint(low, high=None, size=None)
# low <= 난수 < high 사이의 정수를 size 갯수만큼 발생시키면서 배열 생성
# high 생략되면 0 ~ low 까지 범위에서 값 발생함
r5 = np.random.randint (10, size=10)
print(r5)
r6 = np.random.randint (10, 20, size=10)
print(r6)
r7 = np.random.randint(10, 20, size=(3, 5))
print(r7)
print('----------------------------------------')


# ?기술통계
x = np.random.randint(-10, 50, size=30)
print('len: ', len(x))
print('mean: ', np.mean(x))
print('var: ', np.var(x))                   
print('var ddof=1: ', np.var(x, ddof=1))    # ddof 비편향분산
print('std: ', np.std(x))                   # 표준편차: 분산의 제곱근
print('min: ', np.min(x))
print('max: ', np.max(x))
print('median: ', np.median(x))
print('0/4: ', np.percentile(x, 0))
print('1/4: ', np.percentile(x, 25))

# 난수 발생과 난수발생 고정시키는 인수
# np.random.seed(인수)
print(np.random.rand(5))
# 1차: [0.34129583 0.08964255 0.27536619 0.35405685 0.91617423]
# 2차: [0.32276911 0.93648797 0.44431848 0.85162587 0.73679777]
np.random.seed(0)
print(np.random.rand(5))
# 1차: [0.5488135  0.71518937 0.60276338 0.54488318 0.4236548 ]
# 2차: [0.5488135  0.71518937 0.60276338 0.54488318 0.4236548 ]

# shuffle
y = np.arange(10)
print('arrange: ', y)
np.random.shuffle(y)
print('shuffle: ', y)