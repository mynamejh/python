import csv
f = open('../Seoul.csv','r',encoding='cp949')
data = csv.reader(f,delimiter=',')
header = next(data)

max_temp=-999
max_date= ''
for row in data:
    if row[-1]=='':
        row[-1]==-999
        row[-1]=float(row[-1])

        if max_temp<row[-1]:
            max_date = row[0]
            max_temp = row[-1]
f.close()
print('기상관측 아래 서울의 최고 기온이 가장 높았던 날은 ', max_date,'으로, \n')
print(max_temp,'였습니다.')