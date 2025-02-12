import csv
from flask import jsonify


def gender_data(region):
    # CSV 파일 읽기
    with open('gender.csv', encoding='cp949') as f:
        reader = csv.reader(f)
        m = []
        f = []
        for row in reader:
            if region in row[0]:
                m = [-int(i) for i in row[3:104]]
                f = [int(i) for i in row[106:]]

    data = {'male' : m, 'female' : f}
    return jsonify(data)