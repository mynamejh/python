import csv
f = open('../Seoul.csv')
data = csv.reader(f)
header = next(data)
for row in data :
    # row[-1] 은 리스트 마지막 요소를 선택하는 indexing 방법
    # row[-1] : 각 행의 마지막 열 의미
    # 이때, csv 파일에서 읽어온 값들은 문자열 형태로 저장되기 때문에 형 변환 = float() 필요
    row[-1] = float(row[-1])
    print(row)
f.close()