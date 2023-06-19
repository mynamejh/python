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