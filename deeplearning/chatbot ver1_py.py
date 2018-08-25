from pymongo import MongoClient
from datetime import datetime

import threading

conn = MongoClient('127.0.0.1')
db = conn.test1
collec = db.collect

def chatbot():
    sidoName=['서울', '부산', '대구', '인천', '광주', '대전', '울산', '경기', '강원', '충북', '충남', '전북', '전남', '경북', '경남', '제주', '세종']
    while True:
        print("어느 지역의 미세먼지가 알고 싶으세요? 종료 exit")        
        answer=input("")
        now = datetime.now()
        nowDate = now.strftime('%Y-%m-%d %H')
        nowDate= nowDate+":00"
        if(answer.find("exit") != -1):
            break
        for sidolist in sidoName:
            if answer.find(sidolist) != -1:
                data=list(collec.find({"datatime":nowDate,"sidoname":sidolist},{"_id":False,"sidoname":False,"datatime":False,"pm25vale":False}))
                #print(data)
                for city in data:
                    if answer.find(city['cityname']) != -1:
                        #print(city['cityname'])
                        pm25list=list(collec.find({"datatime":nowDate,"sidoname":sidolist,"cityname":city['cityname']},{"_id":False,"sidoname":False,"datatime":False}))
                        pm25dict=dict(pm25list[0])
                        print(city['cityname']+'의 현재 미세먼지는 '+pm25dict['pm25vale']+'입니다.\n\n\n')
                        break
                break