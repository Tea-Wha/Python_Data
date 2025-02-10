# 판다스 : 테이블 형태의 데이터를 쉽게 다룰 수 있도록 설계된 파이썬 데이터 분석 라이브러리
# 데이터의 전처리, 탐색, 변환 및 시각화 등에 사용
# Series - 1차원 데이터 구조, 리스트와 유사하지만 인덱스(라벨)가 붙어 있음
import pandas as pd
import numpy as np

s1 = pd.Series([10, 20, 30, 40, 50])
print(s1)
print(s1.index)
print(s1.values)

# pandas는 데이터 타입이 달라도 사용 가능
s2 = pd.Series(["a", "b", "c", 3.14, True, 1000, 2000, "seoul"])
print(s2)

# 결측치 임의로 생성
s3 = pd.Series([1,2,3,4,np.nan,5,6,7,np.nan,9,10])
print(s3)

# 임의의 인덱스 생성
index_date = ['2024-02-01', '2024-02-02', '2024-02-03', '2024-02-04']
s4 = pd.Series([200, 220, np.nan, 300], index=index_date)
print(s4)

# 2차원 데이터 구조 : DataFrame, 2차원 표 형태의 데이터 구조
data = {
    '이름': ['민지', '하니', '해린', '혜인', '다니엘'],
    '수학': [90, 80, 70, 60, 80],
    '영어': [98, 100, 60, 89, 99],
    '반': ['A', 'B', 'A', 'B', 'C']
}
df = pd.DataFrame(data)
print(df)
print(df.info())      # 데이터 타입 및 결측치 정보
print(df.describe())  # 수치형 데이터 요약 및 통계 제공

print(df['수학']) # 특정 열 추출
print(df.loc[0]) # 특정 행 추출
print(df.loc[1, '영어'])

# 새로운 열 및 행 추가
df['국어'] = [100, 98, 98, 70, 45] # 새로운 열 추가
print(df)
df.loc[5] = ['박지숙', 67, 45, 'C', 45]
print(df)

# 기본 연산
print(df[['수학', '영어']].sum())
print(df['수학'].mean())
print(df['수학'].max())
print(df['수학'].min())

# 그룹화 및 집계
# 반별 수학, 과학, 영어 평균 점수 구하기
class_avg = df.groupby('반')[['수학', '영어', '국어']].mean()
print(f"반별 평균 : {class_avg} ")

# 1. 각 반별 수학과 영어 평균을 동시에 출력하기
class_avg2 = df.groupby('반')[['수학', '영어']].mean()
print(f"반별 평균 : {class_avg2}")

# 2. 각 반별 수학 점수의 최대값과 최소값 구하기
class_max = df.groupby('반')[['수학', '영어']].max()
class_min = df.groupby('반')[['수학', '영어']].min()
print(f"반별 최대값 및 최소값 정리 : {class_max} {class_min} ")

# 3. 과일의 가격 평균과 판매량 평균을 구해 보세요.
data1 ={
    '제품' : ['사과', '딸기', '수박'],
    '가격' : [1800, 1500, 3000],
    '판매량' : [24, 38, 13]
}
df = pd.DataFrame(data1)
price_avg = df['가격'].mean()
print(price_avg)
sell_avg = df['판매량'].mean()
print(sell_avg)