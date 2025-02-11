# 데이터전처리 : 주어진 데이터를 분석에 적합하도록 가공하는 작업
import pandas as pd
exam = pd.read_csv('exam.csv')

# query()를 사용해서 행 제한
print(exam.query('nclass == 1'))

print(exam.query('math > 50')) # 조건문 사용

# 1반 이면서 수학 점수가 50점 이상인 경우 출력
print(exam.query('nclass == 1 & math >= 50'))

# 수학 점수 90점 이상 or 영어 점수 90점 이상 
print(exam.query('math >= 90 | english >= 90'))

# 필요한 변수만 추출
print(exam['math'])

# 여러 열 제한 출력
print(exam[['nclass', 'math', 'english']])

# 열 제거
print(exam.drop(columns='math'))

# 행 제한(query())과 열 제한([]) 조합
print(exam.query('nclass ==2')[['english', 'math']])

# 일부만 출력 : 수학 점수가 50점 이상인 행만 추출한 다음, ID, math 앞부분 5행까지 추출
print(exam.query('math >= 50')[['id', 'math']].head(8))

# 연습 문제 1 : 11개의 컬럼중에 category(자동차 종류), cty(도시 연비) 추출해서 새로운 데이터 생성
mpg = pd.read_csv('mpg.csv')
new_mpg = mpg[['category', 'cty']]
print(new_mpg)

# 연습 문제 2 : category(자동차 종류)가 'suv'인 자동차와 'compact'인 자동차 중
# 어떤 자동차의 cty(도시 연비) 평균이 더 높은 것을 출력
suv_mean = mpg.query('category == "suv"')['cty'].mean()
compact_mean = mpg.query('category == "compact"')['cty'].mean()
if suv_mean > compact_mean:
    print(f"SUV : {suv_mean}")
else:
    print(f"COMPACT : {compact_mean}")

# 정렬하기
print(exam.sort_values('math', ascending=False)) # 수학 성적 기준 오름 차순 정렬

# 여러 정렬 기준 적용하기
print(exam.sort_values(['nclass', 'math'], ascending=[True, False]))