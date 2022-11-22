from datetime import datetime # daretime object containing current date and time
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S") # dd/mm/YY H:M:S
print("Exrcuted time: ", dt_string)
name = "Setthapong Kiankhao"
std_id = "64114069"
quiz = "Quiz-1"
print(quiz +" Name: "+name+" Student ID:"+ std_id)
print("-"*52)
print("Water billing program...")
print("-"*52)
waterUnit = int(input("Enter water unit(s): ")) # รับค่าหน่วยน้ำประปา
service_charge = 30 # ค่าบริการรายเดือน
if waterUnit <= 15: # ถ้าค่าหน่วยน้ำประปาไม่เกิน 15 หน่วย
    cost = waterUnit * 10 # ค่าหน่วยน้ำประปาคูณกับ 10
elif waterUnit <= 30: # ถ้าค่าหน่วยน้ำประปาไม่เกิน 30 หน่วย
    cost = waterUnit * 15 # ค่าหน่วยน้ำประปาคูณกับ 15
else: # ถ้าค่าหน่วยน้ำประปามากกว่า 30 หน่วย
    cost = waterUnit * 20 # ค่าหน่วยน้ำประปาคูณกับ 20
totalcost = cost + service_charge # ค่าใช้จ่ายบวกกับค่าบริการรายเดือน
print("Total cost = {}".format(totalcost)) # แสดงผลลัพธ์โดยใช้ .format
