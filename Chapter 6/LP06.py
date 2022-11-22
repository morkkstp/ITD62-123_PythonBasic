import sys # import ไฟล์จากโฟลเดอร์ WU_Python ในไดร์ฟ D
sys.path.append("D:\WU_Python")
import heading as hd # import ไฟล์ชื่อ heading.py(เป็นไฟล์เก็บหัวเรื่อง)
dt = hd.headinglab("LP06") # function จะ return วันและเวลา
print("-"*55)

import json

persondict = {}

def getinfo(info):
    info.update({"datetime":dt})
    info.update({"fname":input("Enter first name: ")})
    info.update({"lname":input("Enter last name: ")})
    info.update({"age":input("Enter age name: ")})
    info.update({"body_temp":float(input("Enter body temperature: "))})
    # แสดงรายชื่อจังหวัดโดยการอ่านไฟล์ province.txt
    print(open("D:\WU_Python\Week12\province.txt").read())
    info.update({"location":int(input("Enter location number: "))})

def checkrisk(check):
    if check.get("location") != 0:# ตรวจสอบว่าอยู่ในจังหวัดที่มีความเสี่ยงหรือไม่
        check.update({"risk":True})
        if check.get("body_temp") > 37.5: # ตรวจสอบว่าอุณหภูมิมากกว่า 37.5 หรือไม่
            check.update({"covid":True})
        else:
            check.update({"covid":False})
    else:
        check.update({"risk":False})
        check.update({"covid":False})
    
getinfo(persondict)
checkrisk(persondict)
print(persondict)
json_string = json.dumps(persondict) # แปลงข้อมูลจาก python เป็น json
print("JSON = "+json_string) # แสดงข้อมูล json