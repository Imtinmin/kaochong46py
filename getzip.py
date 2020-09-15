import requests
import json
import os

url = "https://teaching.kaochong.com/teaching-extension/app/mycourse/offline/live/list?apiVer=2&appId=2001&ca=%E4%B8%AD%E5%9B%BD%E8%81%94%E9%80%9A&cl=appstore&courseId=15529&duid=18FD89FF0547F8D42790BD16B070BB7AE7337749D17FDEE18559803B6F1EE307256DFE8FDEC58316BFAFF740F00DEF27&dv=iPhone%206s%20Plus&idfa=55F1A10C-9141-4A0D-8050-EDF6B4B835FB&idfv=2AB597BB-0E9E-4434-A056-23FA80EB0609&nt=wifi&ov=13.1.3&rosType=ios&sh=2208&sortType=1&sw=1242&token=C769278ADC390D0F4888D2EC029C7A11685ED7245C2B0BA2DF6EC16FA696C4FE&ver=3.17.0"
#课程json数据

r = requests.get(url)
data = json.loads(r.text)
current_path = os.getcwd()
for i in data["results"]:
    os.chdir(current_path) #创建文件夹分类存放
    os.mkdir(i["name"])
    os.chdir(i["name"])
    for j in i["lessons"]:
        lessonUrl = j["lessonUrl"]
        r = requests.get(lessonUrl)
        with open(j["title"]+".zip", "wb") as zip:
            zip.write(r.content)
