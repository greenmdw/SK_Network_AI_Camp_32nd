# path : C:\Python_workspace\test_pandas_260521\self_study_260522.py

import numpy as np
import pandas as pd

# ?Series() : numpy의 vector, list에 index 라벨을 추가 지정하는 것을 말함
# 1. Series 객체 생성
# Series는 1차원 배열 형태의 자료 구조. 파이썬의 list랑 비슷해 보이지만 각 요소별 index를 지정할 수 있음
# 예) 각 도시에 2025 년도 인구 데이터를 시리즈로 만든다면?
s = pd.Series([19284910, 5000000, 2919999, 2800000], index=['서울', '부산', '인천', '대구'])
# print(s)
"""
서울    19284910
부산     5000000
인천     2919999
대구     2800000
dtype: int64
"""

# 객체 생성시 인덱스 라벨 생략 가능
# print(pd.Series(range(10)))

# 2. DataFrame: 2차원 표만들기
# Series는 1차원이였다면 DataFrame은 2차원 데이터 구조. 
# df의 구성 요소는 Series들의 집합 + 인덱스 + 컬럼명
# 변수 = pd.DataFrame(행렬|변수|사전자료형변수, index=행인덱스라벨, columns=열인덱스라벨)
data = {
    '2022': [11284910, 4100000, 2129999, 2150000],
    '2023': [12284910, 4200000, 2249999, 2220000],
    '2024': [13284910, 4300000, 2489999, 2450000],
    '2025': [14284910, 4400000, 2839999, 2730000],
    '지역': ['수도권', '경상권', '수도권', '경상권'], 
    '2015~2019 증가율': [0.0256, 0.0163, 0.982, 0.015]
    }   # dict 사전자료형 변수 준비

index_lbl = ['서울', '부산', '인천', '대구']
columns_lbl = ['지역', '2022', '2023', '2024', '2025', '2015~2019 증가율']
df = pd.DataFrame(data, index=index_lbl, columns=columns_lbl)
# print(df)
"""
     지역      2022      2023      2024      2025  2015~2019 증가율
서울  수도권  11284910  12284910  13284910  14284910         0.0256
부산  경상권   4100000   4200000   4300000   4400000         0.0163
인천  수도권   2129999   2249999   2489999   2839999         0.9820
대구  경상권   2150000   2220000   2450000   2730000         0.0150
"""

# 3. 데이터 파일 입출력 기능 제공
# 파일에 저장(출력): 데이터프레임.to_파일종류('파일명.확장자', 속성='값',....)
#   df.to_csv('test_csv', mode='w', sep='.')
# 파일 읽어와서 DataFrame에 저장
# df4 = pd.read_csv('sample.csv')

# ?Series.()
# # Series.index / values, 변수명.name  
# print(s.index)      # Index(['서울', '부산', '인천', '대구'], dtype='object')
# print(s.values)     # 맨 위 지정한 값 표출
# s.name = '인구'         # 시리즈의 이름
# s.index.name = '도시'   # 
# print(s)

# ?Series의 연산, indexing, slicing
# print(s / 1000)

# # 시리즈변수.iloc['라벨'] : 시리즈의 인덱싱. 해당 인덱스 행값 불러옴
# print('인덱싱: ', s.iloc[1])    # 5000000
# # 4가지 방법 있음
# print('인덱싱 4가지 방법: ', s.iloc[1], s.loc['부산'], s['부산'], s.부산)

# # 인덱서(배열 인덱싱)를 사용하면 배열 순서 바꾸거나 특정 데이터 선택 가능
# print(s.iloc[[3, 2, 0]])
# print(s.loc[['대구', '부산', '서울']])

# # 조건부 인덱싱도 가능
# print(s[(300e4 < s) & (s <= 500e4)])

# # 슬라이싱
# print(s[1:3])
# print(s['부산':'대구'])

# 시리즈와 딕셔너리 자료형
# 시리즈의 인덱스 라벨이 딕셔너리의 key
# 딕셔너리의 in과 items를 series에도 적용 가능
# print('서울' in s)      # True
# print('팝콘' in s)

# print(s.items())        # <zip object at 0x0000026E60AA38C0>
# for k, v in s.items():
#     print('%s = %d' % (k, v))

# 딕셔너리 객체를 시리즈로 변환 
dict = {'서울': 17284910, '부산': 5000000, '인천': 1819999, '대구': 3500000} 
s2 = pd.Series(dict)
# print(s2)
# + 라벨 붙이기
s2.name = '2025년 인구'
s2.index.name = '도시'
# print(s2)
"""
도시
서울    17284910
부산     5000000
인천     1819999
대구     3500000
Name: 2025년 인구, dtype: int64
"""

# 시리즈 연산
s = pd.Series([19284910, 5000000, 2919999, 2800000], index=['서울', '부산', '인천', '광주']) 
s3 = s - s2         
# print(s3)           # 라벨이 같지 않은 인덱스는 NaN처리됨
"""
광주          NaN
대구          NaN
부산          0.0
서울    2000000.0
인천    1100000.0
dtype: float64
"""
# print(s.values - s2.values)     # [2000000       0 1100000 -700000] 벨류 끼리는 그냥 빼기 됨

# Series.notnull()
# NaN은 float 자료형에서만 표현됨
# 계산 결과에서 NaN이 아닌 값들만 구현하려면 notnul() 메소드 사용
# print(s3.notnull()) 
"""
광주    False
대구    False
부산     True
서울     True
인천     True
dtype: bool
"""
# print(s3[s3.notnull()])
"""
부산          0.0
서울    2000000.0
인천    1100000.0
dtype: float64
"""

# ?DataFrame 클래스
"""
DF란? : 데이터를 2차원으로 만드는 클래스

생성 방법
1. dictionary 만듦. key 값이 column 라벨됨 (기본 문자열)
2. DataFrame 생성자로 딕셔너리를 초기값으로 객체 생성
"""

# dict 사전자료형 준비 (열 라벨 = key값)
data = {
 "2019": [9904312, 3448737, 2890451, 2466052],
 "2020": [9631482, 3393191, 2632035, 2431774],
 "2021": [9762546, 3512547, 2517680, 2456016],
 "2022": [9853972, 3655437, 2466338, 2473990],
 "지역": ["수도권", "경상권", "수도권", "경상권"],
 "2010-2015 증가율": [0.0283, 0.0163, 0.0982, 0.0141]
} 

# 인덱스 라벨 준비 (행 라벨)
index_label = ['서울', '부산', '인천', '대구']
df = pd.DataFrame(data, index = index_label)
# df 출력
# print(df)
"""
       2019     2020     2021     2022   지역  2010-2015 증가율
서울  9904312  9631482  9762546  9853972  수도권         0.0283
부산  3448737  3393191  3512547  3655437  경상권         0.0163
인천  2890451  2632035  2517680  2466338  수도권         0.0982
대구  2466052  2431774  2456016  2473990  경상권         0.0141
"""
# df 속성
# print(df.values)
# print(df.columns)
# print(df.index)
# print(type(df.index))   # <class 'pandas.core.indexes.base.Index'>

# *색인 객체는 pandas.Index 클래스로 별도 생성
# 생성된 색인 객체를 시리즈나 데이터 프레임에 따로 지정 가능
stu_index = pd.Index(['학생이름', '국어점수', '영어점수'])
# print(stu_index)
stu_data = pd.Series([['홍길', '김유신', '황지니'], [50, 75, 95], [80, 90, 100]], index = stu_index)
# print(stu_data)
# stu_data.index = stu_index  => 로도 index 설정 가능

# name 속성 이용
df.index.name = '도시'
df.columns.name = '특성'
df.Name = '년도별 인구데이터'


# ?DF의 컬럼 데이터 갱신, 추가, 삭제
# DF 연산
df['2010-2015 증가율'] = df['2010-2015 증가율'] * 100
# 없는 열라벨 적으면 추가됨
df['2016-2020 증가율'] = ((df['2022'] - df['2019']) / df['2019'] * 100).round(2)
# print(df)

# DF 열 삭제
del df['2016-2020 증가율']
# print(df)

# *열 인덱싱 가능
# 컬럼 라벨(key)을 이용
# print(df['2019'])
# print(df[['2019', '2020']])
# print(type(df['2019']))              # <class 'pandas.core.series.Series'>
# print(type(df[['2019', '2020']]))       # <class 'pandas.core.frame.DataFrame'>

# *행 인덱싱: 행을 슬라이싱
# print(df[:1])       # 0행만 추출
# print(df[1:3])
# print(df["서울": '인천'])

# *값 하나만 인덱싱
# print(df['2019']['인천'])

# ? test4 DataFrame 인덱스 조작
# 인덱스 라벨이 없는 데이터프레임에 행라벨 지정하거나 제거하는 것
# set_index(): 기존 행라벨 제거하고 데이터 열중 하나를 행 라벨로
# reset_index(): 추가한 행라벨 제거하고 인덱스를 열 값들로 추가

np.random.seed(0)
df1 = pd.DataFrame(
    np.vstack([list('ABCDE'), np.round(np.random.rand(3, 5), 2)]).T,
    columns=['C1', 'C2', 'C3', 'C4']
)
# print(df1)

# set_index()
df2 = df1.set_index('C1')
# print(df2)
# print(df2.set_index('C2'))  # 지정한 컬럼을 행 인덱스로 삼음

# reset_index()
# print(df2.reset_index())        # 원래대로 인덱스 돌림

