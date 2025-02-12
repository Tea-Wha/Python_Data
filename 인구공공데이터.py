import csv
import matplotlib.pyplot as plt
with open('gender.csv', encoding='cp949') as file:
    data = csv.reader(file)
    m = [] # 남성 데이터 저장
    f = [] # 여성 데이터 저장
    for row in data:
        if '신도림' in row[0]:
            for i in row[3:104]:
                m.append(-int(i)) # 남성 데이터를 m 리스트에 저장
            for i in row[106:]:
                f.append(int(i)) # 여성 데이터를 f 리스트에 저장

plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False
plt.title('신도림 지역의 남녀 성별 인구 분포')
plt.barh(range(101), m, label='남성')
plt.barh(range(101), f, label='여성')
plt.legend()
plt.show()