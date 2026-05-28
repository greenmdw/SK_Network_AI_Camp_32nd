import seaborn as sns

titanic = sns.load_dataset('titanic')

print(titanic.info())
# 결측치 확인
titanic.isnull().sum()

# 1. 결측치가 있는 행(row) 삭제
titanic_dropped = titanic.dropna()
# 2. 평균 값으로 결측치 대체(age 열에 대해)
age_mean = titanic['age'].mean()
titanic['age_mean_filled'] = titanic['age'].fillna(titanic['age'].mean())
# -> result
titanic['age_mean_filled'].isnull().sum()

# 3. 중앙값으로 결측치 대체 (fare열에 대해)
titanic['fare_median_filled'] = titanic['fare'].fillna(titanic['fare'].median())
# -> result
titanic['fare_median_filled'].isnull().sum()

# 4. 최빈값으로 결측치 대체 (embarked 열에 대해)
titanic['embarked_mode_filled'] = titanic['embarked'].fillna(titanic['embarked'].mode()[0])
# -> result
titanic['embarked_mode_filled'].isnull().sum()

# 5. 전진 채우기 (forward fill)
titanic['age_ffill'] = titanic['age'].ffill()

# 6. 후진 채우기 (Backword fill) (age열에 대해)
titanic['age_bfill'] = titanic['age'].bfill()

# outlier_iqr
import numpy as np
tips = sns.load_dataset('tips')
def calculate_iqr(data):
    Q1 = np.percentile(data, 25)
    Q3 = np.percentile(data, 75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return lower_bound, upper_bound

# total_bill 열에 대해 IQR 계산
lower_bound, upper_bound = calculate_iqr(tips['total_bill'])

# 이상치 탐지(IQR 기준을 벗어나는 값들)
outliers = tips[(tips['total_bill'] < lower_bound) | (tips['total_Bill'] > upper_bound)]

# 이상치 처리 (이상치를 중앙값으로 대체)
median_total_bill = tips['total_bill'].median()
tips.loc[(tips['total_bill'] < lower_bound) | (tips['total_bill'] > upper_bound), 'total_bill'] = median_total_bill


# 03_outlier_zscore.py
# z-스코어 계산 함수
def calculate_z_scores(data):
    return (data - np.mean(data)) / np.std(data)

# total_bill 열에 대해 z-score 계산
tips['total_bill_zscore'] = calculate_z_scores(tips['total_bill'])

# 이상치 탐지(z-score가 3 이상이거나 -3 이하인 경우
outliers = tips[np.abs(tips['total_bill_zscore']) > 3]
