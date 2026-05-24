# path C:\Python_workspace\test_pandas_260521.self_study_260524.py
# 20260524

# ?인터넷 상의 데이터베이스 자료 읽어오기.
# 추가 설치 필요: pandas-datareader
'''
참조 : https://pandas-datareader.readthedocs.io/en/latest/index.html
사이트 종류 확인 : https://pandas-datareader.readthedocs.io/en/latest/readers/index.html
사이트 종류 : FRED, Farma/French, World Bank, OECD, Eurostat, EDGAR index, TSP Fund Data,
                Oanda currency historical rate, Nasdaq Trader Symbol Definitions  등
'''

import pandas as pd
import numpy as np

# 데이터 검색을 위한 날짜 지정할 때 datatime 모듈 이용 가능
import datetime as dt

# datetime 써도 되고, 내부적으로 dateutil 패키지가 사용되고 있어 날짜가 됨
dt_start = dt.datetime(2023, 1, 1)
dt_end = dt.datetime(2024, 6, 30)

# date_source = '읽어올 웹사이트 url 지정
# pandas_datereader 패키지가 제공하는 기본 웹사이트 정보 읽어오기 함수 있음
# pdr.get_data_fred() 함수 사용하면 자동 data_source 가 FRED 로 설정됨

from pandas_datareader import data as pdr

gdp = pdr.DataReader('GDP', 'fred', dt_start, dt_end)
print(gdp)

# *데이터프레임 고급 인덱싱
# loc 인덱서 (인덱싱 속성) 라벨 기반의 2차원 인덱싱
df = pd.DataFrame(np.arange(10, 22).reshape(3,4), index = ['a', 'b', 'c'], columns=['A', 'B', 'C', 'D'])
print(df)
print(df.loc['a'])      # 한 행 인덱싱인데 세로로 출력
print(df.loc['b':'c'])      # 두 행 슬라이싱이고 그대로 가로로 출력
print(df['b':'c'])          # 실은 슬라이싱 때 loc 생략 가능

print(df.A > 15)            # A열 값중에 15보다 큰지 작은지 True/False
print(df.loc[df.A > 15])    # df.A > 15결과 값은 c행만 true 이기 때문에 C 행 값만 리턴
"""
    A   B   C   D
c  18  19  20  21
"""

# 인덱스 값을 반환하는 함수를 사용할 수도 있음. 위 사례와 비슷
def select_row(df):
    return df.A > 12
print(select_row(df))
# print(df.loc[select_row(df)])       # True가 리턴된 행의 값들이 출력됨

# 인덱싱에 행과 열 같이 작성
# print(df.loc['a', 'A'])
# print(df.loc['a', :])
# print(df.loc[['a', 'b'], ['B', 'C']])

# boolean 값으로 인덱실 할 수 있음
# print(df.loc[df.A > 15, ['C', 'D']])

# *iloc 인덱서
# 순서를 나타내는 정수 기반의 2차원 인덱싱에 사용
print('--------------')
print(df)
print(df.iloc[:2, 2])           # 0행부터 1열 중, 2열 값
print(df.iloc[0, 2:])           # 0행 중, 2열부터 끝까지
print(df.iloc[0, :-3])          # 0행 중, 우측에서 3열에 있는 값
print(df.iloc[2:3, 1:3])        # 2행 중, 1열 부터 2열까지

df.iloc[-1] = df.iloc[-1] * 2
print(df)

# ?시계열 데이터 다루기
# 시간과 날짜 데이터를 시계열 데이터
# pandas는 시계열 다루기 위해 인덱스 자료형을 DataTimeIndex로 지정해야 함
# DatetimeIndex : 타임스탬프 (timestapm) 형식의 특정 시간을 기록하는 시계열 데이터
# 생성함수: pd.to_datetime(), pd.date_range() 함수 사용

# pd.to_datetime()
date_str = ['2024. 1. 4', '2024. 1. 5', '2024. 1. 6']
idx = pd.to_datetime(date_str)
print(idx)      # DatetimeIndex(['2024-01-04', '2024-01-05', '2024-01-06'], dtype='datetime64[ns]', freq=None)

# pd.to_date_range()
# 날짜 시간을 일일이 입력하지 않고 범위를 주면 자동으로 범위 내의 시계열 인덱스 생성
print(pd.date_range('2026.05.01', '2026.05.30'))
print(pd.date_range('2024.12.01', periods=30))
print(pd.date_range('2019-4-1', '2019-4-30', freq='BMS'))
# freq 인수로 특정 날짜만 생성되도록 할 수도 있음
# s : 초, min : 분, H : 시간
# D : 일(day), B : 주말이 아닌 평일, W : 주(일요일), W-MON : 주(월요일)
# M : 각 달(month) 의 마지막 날, MS : 각 달의 첫날
# BM : 주말이 아닌 평일 중에서 각 달의 마지막 날
# BMS : 주말이 아닌 평일중에서 각 달의 첫날
# WOM-2THU : 각 달의 두번째 목요일
# Q-JAN : 각 분기의 첫달의 마지막 날
# Q-DEC : 각 분기의 마지막 달의 마지막 말

# *shift 연산자
# 시계열 데이터 인덱스는 날짜 이동에 대한 연산 가능
# shift 연산을 시용하면 인덱스는 그대로 두고, 데이터만 이동
np.random.seed(0)
ts = pd.Series(np.random.randn(4), index=pd.date_range('2023-1-1', periods=4, freq='M'))
# print(ts)
"""
2023-01-31    1.764052
2023-02-28    0.400157
2023-03-31    0.978738
2023-04-30    2.240893
Freq: M, dtype: float64
"""

# print(ts.shift(1))      # 인덱스는 그대로 두고 값들을 한 칸씩 아래로 내림
# print(ts.shift(-1))     # 인덱스는 그대로 두고 값들을 한 칸씩 위로
# print(ts.shift(1, freq='M'))        # 인덱스가 밀림

# *resample 연산
# 시간간격 재조정
# up-sampling: 시간 구간을 줄이면 데이터 양 증가
# down-sampling: 시간 구간을 늘리면 데이터 양 감소
ts = pd.Series(np.random.randn(100), index=pd.date_range('2023-1-1', periods=100, freq='D'))
# print(ts.tail(20))

# 다운샘플링의 경우, 원래 데이터가 그룹으로 묶이기 때문에 groupby와 같은 그룹연산을 해서 대표값을 구해야 함
# print(ts.resample('W').mean())
# print('-------------')
# print(ts.resample('MS').first())        
"""
2023-01-01    1.867558
2023-02-01    0.156349
2023-03-01   -1.726283
2023-04-01    0.356366
Freq: MS, dtype: float64"""

# 날짜가 아닌 시/분 단위로 간격을 지정시, 구간위 왼쪽 한계값(가장 빠른 시간)은 포함됨
# 오른쪽 한계값(가장 늦은 시간)은 포함 안됨
# 예: 10분 간격으로 구간을 만들면 10의 배수가 되는 시각은 다음 구간의 시작점이 됨
ts = pd.Series(np.random.randn(60), index = pd.date_range('2024-1-1', periods=60, freq='min'))
print(ts.tail(20))                  # 1분 간격 60개 데이터
print(ts.resample('10min').sum())   # 10분 간격 다운 샘플링, 10개 데이터의 합계로 표현

print(ts.resample('10min', closed='right').sum())       # 0분 ~ 10분 까지 합계

# *ohlc() 함수: 구간의 시고저종(open, high, low, close) 값을 구함
print(ts.resample('5min').ohlc())
"""
                     open      high       low     close
2024-01-01 00:00:00 -1.173123  1.943621 -1.173123  1.922942
2024-01-01 00:05:00  1.480515  1.910065 -0.861226  1.910065
2024-01-01 00:10:00 -0.268003  0.947252 -0.268003  0.614079
2024-01-01 00:15:00  0.922207  1.326386 -1.099401  1.326386
2024-01-01 00:20:00 -0.694568  1.849264 -0.694568  0.672295
"""
# 업샘플링의 경우에 존재하지 않는 데이터를 만들어야 함
# 앞 데이터를 뒤 데이터로 그대로 쓰는 forward filling 방식과
# 뒤 데이터를 미리 쓰는 backward filling 방식이 있음
# ffill(), bfill() 함수 사용
print(ts.resample('30s').ffill().head(10))
print(ts.resample('30s').bfill().head(10))

# df 접근자
# datetime 자료형 시리즈에 dt 접근자 제공됨, 속성과 메소드도 제공함
s = pd.Series(pd.date_range('2024-12-25', periods=100, freq='D'))
print(s.tail(10))

# year, month, day, weekday 속성을 이용하면 년, 월, 일 요일 저보 추출
print(s.dt.year.head(10))
print(s.dt.weekday.head(10))        # 요일: 7로 나눈 나머지로 표현 (0=일요일)

# strftime() 함수: 포맷을 이용해서 문자열로 벼환
print(s.dt.strftime('%Y년 $M월 %d일'))