# path:  C:\Python_workspace\test_pandas_260521\self_study_260523
# 260523


import numpy as np
import pandas as pd

# ?test5 다중 인덱스
# 행이나 열에 여러 계층의 인덱스 라벨이 지정된 것
# 데이터 프레임 생성할 때, column 인수에[[], []] 리스트의 리스트로 (행렬) 설정하면 됨
np.random.seed(1)
df3 = pd.DataFrame(np.round(np.random.randn(5, 4), 2), columns=[['A', 'A', 'B', 'B'], ['C1', 'C2', 'C3', 'C4']])
# print(df3)
"""
      A           B      
     C1    C2    C3    C4
0  1.62 -0.61 -0.53 -1.07
1  0.87 -2.30  1.74 -0.76
2  0.32 -0.25  1.46 -2.06
3 -0.32 -0.38  1.13 -1.10
4 -0.17 -0.88  0.04  0.58
"""

# columns.name 속성
# 다중 인덱스라벨에 이름 지정시 사용함. 이름들은 리스트로 지정
df3.columns.names = ['Cidx1', 'Cidx2']
# print(df3)

# 행라벨도 다중인덱스 적용할 수 있음. 이름도 지정 가능
df4 = pd.DataFrame(np.round(np.random.randn(6, 4), 2), columns=[['A', 'A', 'B', 'B'], ['C1', 'C2', 'C3', 'C4']],
                   index=[['M', 'M', 'M', 'F', 'F', 'F'], ['id_' + str(i + 1) for i in range(3)] * 2])
df4.columns.names = ['Cidx1', 'Cidx2']
df4.index.names = ['Ridx1', 'Ridx2']
# print(df4)
"""
Cidx1           A           B      
Cidx2          C1    C2    C3    C4
Ridx1 Ridx2                        
M     id_1  -1.10  1.14  0.90  0.50
      id_2   0.90 -0.68 -0.12 -0.94
      id_3  -0.27  0.53 -0.69 -0.40
F     id_1  -0.69 -0.85 -0.67 -0.01
      id_2  -1.12  0.23  1.66  0.74
      id_3  -0.19 -0.89 -0.75  1.69
"""

# 행 라벨과 열라벨 교환
# stack(): 열인덱스라벨 = 행인덱스 라벨
# print(df4.stack('Cidx1'))   # 열 라벨이던 Cidx1을 행라벨로 가져옴
"""
Cidx2                C1    C2    C3    C4
Ridx1 Ridx2 Cidx1                        
M     id_1  A     -1.10  1.14   NaN   NaN
            B       NaN   NaN  0.90  0.50
      id_2  A      0.90 -0.68   NaN   NaN
            B       NaN   NaN -0.12 -0.94
      id_3  A     -0.27  0.53   NaN   NaN
            B       NaN   NaN -0.69 -0.40
F     id_1  A     -0.69 -0.85   NaN   NaN
            B       NaN   NaN -0.67 -0.01
      id_2  A     -1.12  0.23   NaN   NaN
            B       NaN   NaN  1.66  0.74
      id_3  A     -0.19 -0.89   NaN   NaN
            B       NaN   NaN -0.75  1.69
"""
# unstack(): 행인덱스라벨 => 열라벨로 교환
# print(df4.unstack('Ridx2'))     
"""
Cidx1     A                                   B                              
Cidx2    C1                C2                C3                C4            
Ridx2  id_1  id_2  id_3  id_1  id_2  id_3  id_1  id_2  id_3  id_1  id_2  id_3
Ridx1                                                                        
F     -0.69 -1.12 -0.19 -0.85  0.23 -0.89 -0.67  1.66 -0.75 -0.01  0.74  1.69
M     -1.10  0.90 -0.27  1.14 -0.68  0.53  0.90 -0.12 -0.69  0.50 -0.94 -0.40
"""

# ?데이터 갯수 세기 (seaborn)
import seaborn as sns

# 데이터 갯수 세기, NaN은 제외
s = pd.Series(range(10))
# print(s)
s[3] = np.nan   # 3번째 인덱스에 NaN 기록
# print(s)

# df의 count는 열별 데이터 갯수. 값이 누락된 부분 찾을 때 용이
np.random.seed(0)
df = pd.DataFrame(np.random.randint(5, size=(4,4)), dtype=float)
# print(df)
df.iloc[2, 3] = np.nan
# print(df)
# print(df.count())       # 열별로 갯수 셈
"""
0    4
1    4
2    4
3    3
"""

# 타이타닉 호 승객 데이터를 df로 만듦
titanic = sns.load_dataset('titanic')
# print(titanic.head())       # head(): 최고 5ro rmfovmaks qhduwna. 
# print(titanic.value_counts())

# 카테고리 갯수 세기: value_counts()
# 시리즈의 값이 정수 | 문자열로 된 카테고리 갯수를 리턴
# 카테고리: 기록된 값을 종류별로 구분
np.random.seed(2)
s2 = pd.Series(np.random.randint(6, size=100))
# print(s2.tail())
# print(s2.value_counts())
""" 각 value별 몇 개의 값이 나왔는지 수치 나옴
2    22
0    18
3    16
5    15
4    15
1    14
dtype: int64
"""
# 정렬: sort_index(), sort_values()
# sort_index(): 값을 정렬하고 나서 index 배치를 리턴
# sort_values(): 정렬하고 value에 따른 리턴
# print(s2.value_counts().sort_index())
# print(s2.value_counts().sort_values(ascending=False))

# dataframe처럼 여러 컬럼을 가진경우 sort_values()로 정렬시 by 사용해 기준 설정
# print(df)
# print(df.sort_values(by=2))

# *행열 합계: sum()
# 행과 열 합계를 구할 때 sum(axis=1 | 0)
# 0 = 열, 1 = 행
np.random.seed(3)
df2 = pd.DataFrame(np.random.randint(10, size=(4, 8)))
# print(df2)
# print('sum axis=0: ', df2.sum(axis=0))  # axis=0 => 열별 합계 나열

# 컬럼 하나 추가해서 합계 기록
df2.loc['colTotal', :] = df2.sum()
# print(df2)

df2.loc[:, 'indexTotal'] = df2.sum(axis=1)
# print(df2)

# *apply(lambda ~)
# 행이나 열 단위로 좀 더 복잡한 계산을 적용해야 할 때 사용하는 함수
# 복잡한 계산식은 사용자정의함수로 작성하거나, 람다함수를 사용
df3 = pd.DataFrame({
    'A': [1,3,1,3,4],
    'B': [2,3,1,2,3],
    'C': [1,3,2,4,4]
})
# print(df3)

# 예: 각 열의 최대값과 최소값의 차이를 구한다면
# print(df3.apply(lambda x: x.max() - x.min()))

# 예: 각 행의 최대값과 최소값의 차이를 구하라
# print(df3.apply(lambda x: x.max() - x.min(), axis=1))

# 예: 각 열에 대해 어떤 값이 얼마나 사용되는지를 확인한다면
# print(df3.apply(lambda x: x.value_counts(), axis=0))

# 타이타닉호의 승객 중 20살을 기준으로
# 20살 이상이면 성인(adult), 20살 미만이면 미성년자(child)로 구별
# 라벨링된 컬럼을 추가해서 표시되게 한다면
titanic['성인구분'] = titanic.apply(lambda r: 'adult' if r.age >=20 else 'child', axis=1)


# *fillna() 함수
# NaN을 원하는 값으로 바꿀 때 사용
# print('df: \n', df)
# print(df.fillna(100).astype(int))       # astype(자료형) : 전체 데이터의 자료형을 바꿈

# cut(): 실수값을 경계선으로 지정하는 경우에 사용(분류)
# qcut(): 갯수가 똑같은 구간으로 분류할 때 사용
# 예: 나이 데이터를 가진 리스트의 경우
ages = [0, 2, 10, 21, 23, 37, 31, 61, 20, 41, 32, 101]
# cut()을 사용해서 카테고리(열) 값으로 변경
# bins 인수로 분류하는 기준값을 지정함. 기준 벗어나면 NaN
bins = [1, 20, 30, 50, 70, 100]     # 1~20 / 20~30 / 30~50 / 50~70 / 70~100의 구간을 만듦
labels = ['미성년자', '청년', '중년', '장년', '노년']       # 각 구간별 명칭
result = pd.cut(ages, bins=bins, labels = labels)
# print(result)
"""
[NaN, '미성년자', '미성년자', '청년', '청년', ..., '장년', '미성년자', '중년', '중년', NaN]
Length: 12
Categories (5, object): ['미성년자' < '청년' < '중년' < '장년' < '노년']
"""
# print(type(result))

# cut()의 반환 자료형이 Categorical 클래스 객체
# 이 객체는 라벨 문자열을, codes 속성으로 정수로 인코딩된 값을 확인 가능
# print(result.categories)        # Index(['미성년자', '청년', '중년', '장년', '노년'], dtype='object')
# print(result.codes)         # [-1  0  0  1  1  2  2  3  0  2  2 -1] -1은 NaN값

# 위 결과를 데이터프레임에 적용한다면
df4 = pd.DataFrame(ages, columns=['age'])
# print(df4)
df4['age_category'] = pd.cut(ages, bins=bins, labels=labels)
# print(df4)

# ?데이터 입출력
# ,로 데이터 구분한 csv가 기본으로 다루어짐

data = {
    'c1' : [1, 2, 3],
    'c2' : [1.11, 2.22, 3.33],
    'c3' : ['one', 'two', 'three']
}


df = pd.DataFrame(data)
# print(df)
# df를 csv파일로 저장 처리. 한번 실행 후 주석 처리 필요
# df.to_csv('sample1.csv', mode='w')

# pd.read_csv(): csv 파일 읽어서, df 만들기 
df2 = pd.read_csv('sample1.csv')
print('csv read===========')
# print(df2)
# print(type(df2))        # <class 'pandas.core.frame.DataFrame'>

# 파일에 기록 저장시 컬럼 라벨과 행인덱스 라벨 제외할 수 있음
# df.to_csv('sample2.csv', mode='w', header=False, index=False)
# 데이터 파일을 읽어 들일 때, 컬럼라벨을 추가할 수 있음
df3 = pd.read_csv('sample2.csv', names=['아', '야', '어'])
# print(df3)

# 파일 읽어 들일 때, 특정 컬럼값을 인덱스 행으로 지정할 수 있음
df4 = pd.read_csv('sample1.csv', index_col='c1')
# print(df4)

# 파일 기록시 , 대신에 원하는 seperator를 지정할 수 있음
df4.to_csv('sample3.csv', mode='w', sep='\t')          # 데이터를 공백으로 구분
# 공백으로 구분된 (regular expression) 문자열을 이용해서 구분자를 지정
# 공백에 대한 정규표현식 문자열은 '\s+' 이다
df5 = pd.read_csv('sample3.csv', sep='\s+') 
# print(df5)

# skiprows: 파일안에 건너뛰어야 되는 행이 있다면 
df6 = pd.read_csv('sample3.csv', skiprows=[0, 1])
# print(df6)

# *파일의 특정값 NaN처리
data2 = {
    'c1': [1, 2, 3],
    'c2': [ 1.11, 2.22, 3.33],
    'c3': ['누락', 'two', 'three']
}
df7 = pd.DataFrame(data2)

# df7.to_csv('sample5.csv', mode='w')
df8 = pd.read_csv('sample5.csv', na_values=['누락'])
print(df8)

# 반대로 파일에 기록할 때 NaN 표시값을 다른 값으로 바꿀 수 있음
# df8.to_csv(('sample6.csv', na_rep='값없음'))

# 데이터 프레임에 인덱스 라벨 지정
print(df)
df.index = ['a', 'b', 'c']
print(df)

# 인터넷상에 있는 파일 읽을 수 있음. 
df9 = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
