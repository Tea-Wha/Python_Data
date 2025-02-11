import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

mpg = pd.read_csv('./mpg.csv')
# print(mpg.head())  # 기본적으로 앞부분 5행 출력
# print(mpg.tail(3)) # 데이터의 마지막 3행 출력
# print(mpg.shape)   # 데이터프레임의 크기를 보여줌
# print(mpg.info())  # 변수들의 속성을 보여줌, 결측치도 확인 가능
# print(mpg.describe()) # 요약 통계정보 출력

print(mpg)

# 변수 이름 변경
mgr_new = mpg.copy()
mgr_new = mgr_new.rename(columns={'cty' : 'city'})
mgr_new = mgr_new.rename(columns={'hwy' : 'highway'})
print(mgr_new.head())

# 파생 변수 만들기
mpg['total'] = (mpg['cty'] + mpg['hwy']) / 2
print(mpg.head())

# 조건문을 활용한 파생변수 생성
# mpg['test'] = np.where(mpg['total'] >= 20, 'pass', 'fail')
# count_test = mpg['test'].value_counts()
# count_test.plot.bar()
# plt.show()

# 중첩 조건문을 활용한 연비 등급 부여
# mpg['grade'] = np.where(mpg['total'] >= 30, 'A', np.where(mpg['total'] >= 20, 'B', 'C'))
# count_grade = mpg['grade'].value_counts().sort_index()
# count_grade.plot.bar(rot=0)
# plt.show()

# 연습문제
mw = pd.read_csv('./midwest.csv')
print(mw.info())
mw_new = mw.copy()
mw_new = mw_new.rename(columns={'poptotal' : 'total'})
mw_new = mw_new.rename(columns={'popasian' : 'asian'})
mw_new['percentage'] = (mw_new['asian'] / mw_new['total']) * 100
mw_new['percentage'].plot.hist()
print(mw_new.info())
asian_mean = mw_new['percasian'].mean()
mw_new['mean_test'] = np.where(mw_new['percasian'] >= asian_mean, 'large', 'small')
count_mean = mw_new['mean_test'].value_counts().sort_index()
count_mean.plot.bar(rot=0)
plt.show()