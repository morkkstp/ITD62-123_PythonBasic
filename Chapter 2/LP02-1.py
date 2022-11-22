# โปรแกรมตรวจสอบน้ำตาลในเลือด
from datetime import datetime # daretime object containing current date and time

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S") # dd/mm/YY H:M:S
print("Exrcuted time: ", dt_string)
name = 'Setthapong Kiankhao'
std_id = '64114069'
lab = 'LP02-1'
print(lab +' Name: '+name+' Student ID:'+ std_id)
print('----------------------------------------------------')

# command script
print("Diabetes measurement program")
blood_sugar = int(input("Enter blood sugar: ")) # รับค่าน้ำตาลในเลือด
print('----------------------------------------------------')
if blood_sugar > 126: # ตรวจสอบเงื่อนไขค่าน้ำตาลในเลือด
    # แสดงข้อความ ถ้าค่าน้ำตาลในเลือดมากกว่า 126
    print("Blood sugar = {} mg/DL. You are risk.".format(blood_sugar))
else:
    # แสดงข้อความ ถ้าค่าน้ำตาลในเลือดน้อยกว่า 126
    print("Blood sugar = {} mg/DL. You are normal.".format(blood_sugar))
print('----------------------------------------------------')
