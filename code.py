#웹크롤링
import requests
import json
import os

#C:\Users\USER\Desktop\gwanak data
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

print('스크래핑 시작')
url1='https://www.gwanak.go.kr/site/gwanak/WaitCallNo1.do'
data1=requests.get(url1).text
url2='https://www.gwanak.go.kr/site/gwanak/WaitCallNo2.do'
data2=requests.get(url2).text
url3='https://www.gwanak.go.kr/site/gwanak/WaitCallNo3.do'
data3=requests.get(url3).text

#캐스팅
cast1=data1.split('"')
info1=[cast1[3],cast1[7],cast1[11]]
cast2=data2.split('"')
info2=[cast2[3],cast2[7],cast2[11]]
cast3=data3.split('"')
info3=[cast3[3],cast3[7],cast3[11]]
"""
print(info1)
print(info2)
print(info3)
"""

#합치기
data={}
data['관악구 보건소']=info1
data['신림체육센터']=info2
data['낙성대공원']=info3


#save
with open(os.path.join(BASE_DIR, 'news.json'), 'w+',encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii = False, indent='\t')

print('스크래핑 끝')

