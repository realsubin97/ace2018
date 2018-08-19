
# coding: utf-8

# In[5]:


import threading

import pandas as pd
from bs4 import BeautifulSoup
import requests

import pymongo
from pymongo import MongoClient #from이 있을경우 import뒤에있는건 함수 인데 db연동 모듈 추가역할을 합니다

# db 연동
conn = MongoClient('127.0.0.1')
# print(conn) # MongoClient(host=['127.0.0.1:27017'], document_class=dict, tz_aware=False, connect=True)

#db.collection.함수()

# db 생성
db = conn.test1
# collection 생성
collect = db.collect # collect = conn.test_db.collect 쉽게말하면 이 db와 이 collect를 가지고있는거죠


# In[6]:


serviceKey='F%2FxP1NfaTBhw0giVbsH7HTUMMnbJF6p9LhD9p8mJ4HpucMsVcxUzoTw4RxZDFdnRP3NgWj0IwJke%2FOzfe5VxhA%3D%3D'
numOfRows=[25, 22, 15, 23, 9, 10, 17, 86, 14, 16, 30, 23, 24, 20, 25, 5, 4]
sidoName=['서울', '부산', '대구', '인천', '광주', '대전', '울산', '경기', '강원', '충북', '충남', '전북', '전남', '경북', '경남', '제주', '세종']


# In[9]:



def func():
    timer=threading.Timer(3600,func)
    
    for number in range(0,17):
        url='http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnMesureSidoLIst?serviceKey='+str(serviceKey)+'&numOfRows='+str(numOfRows[number])+'&pageSize=10&pageNo=1&startPage=1&sidoName='+str(sidoName[number])+'&searchCondition=DAILY'
        html=requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')
    
        citylist=[]
        pm25list=[]
        timelist=[]

        datatime=soup.find_all('datatime')
        cityname=soup.find_all('cityname')
        pm25vale=soup.find_all('pm25value')

        for code in datatime:
            timelist.append(code.text)
        for code in cityname:
            citylist.append(code.text)
        for code in pm25vale:
            pm25list.append(code.text)
    
        numb=numOfRows[number]
    
        for num in range(0,numb):
            test={'sidoname':sidoName[number],'cityname':citylist[int(num)], 'pm25vale':pm25list[int(num)],'datatime':timelist[int(num)]}
            collect.insert(test)
    
    timer.start()

func()


# In[38]:





# In[ ]:



    

