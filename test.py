import csv
import openpyxl #엑셀 파일 저장
import pathlib
import pandas as pd
import json # json 파일 파싱





# 파일 열기
f = open('../Seoul.csv')
# 파일 읽기
data = csv.reader(f) 
header = next(data)
for row in data :
    # row[-1] 은 리스트 마지막 요소를 선택하는 indexing 방법
    # row[-1] : 각 행의 마지막 열 의미
    # 이때, csv 파일에서 읽어온 값들은 문자열 형태로 저장되기 때문에 형 변환 = float() 필요
    row[-1] = float(row[-1])
    print(row)
f.close()


# 텍스트 파일을 '개인정보.xlsx' 파일로 복사(생성)
# to_excel() 함수를 사용하여 데이터프레임을 엑셀 파일로 변환하고, '개인정보.xlsx'라는 파일명으로 저장합니다. 
# index=False는 인덱스를 엑셀 파일에 저장하지 않도록 지정하는 옵션

df = pd.DataFrame(pd.read_csv('hey.txt',sep=','))
print(df)
df.to_excel('개인정보.xlsx',index=False)

#json 파일 열고 file로 저장
with open('./jsonTest.json','r',encoding='utf-8')as file:
    data = json.load(file) # json.load() 함수에서 data 읽기
    
