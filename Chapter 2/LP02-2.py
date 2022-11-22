# โปรแกรมหาค่าดัชนีมวลกาย
from datetime import datetime # daretime object containing current date and time

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S") # dd/mm/YY H:M:S
print("Exrcuted time: ", dt_string)
name = 'Setthapong Kiankhao'
std_id = '64114069'
lab = 'LP02-2'
print(lab +' Name: '+name+' Student ID:'+ std_id)
print('----------------------------------------------------')

#command script
print("Body Mass Index (BMI) Calculator")
kg = float(input("Enter your weight(kg): ")) # รับค่าน้ำหนัก(kg)
m = float(input("Enter your height(m): ")) # รับค่าส่วนสูง(m)
print('----------------------------------------------------')
bmi = kg / (m ** 2) # คำนวณค่าดัชนีมวลกาย
if bmi < 18.5:# ตรวจสอบเงื่อนไขค่าดัชนีมวลกาย
    # ถ้าน้อยกว่า 18.5 เก็บค่า "You are Underweight." ใน result
    result = "You are Underweight."
elif bmi <= 24.9:
    # ถ้าน้อยกว่าหรือเท่ากับ 24.9 เก็บค่า "You are Healthy." ใน result
    result = "You are Healthy."
elif bmi <= 29.9:
    # ถ้าน้อยกว่าหรือเท่ากับ 29.9 เก็บค่า "You are Overweight." ใน result
    result = "You are Overweight."
else:
    # ถ้านอกเหนือจากนั้น(มากกว่า 30.0) เก็บค่า "You are Obese." ใน result
    result = "You are Obese."

textform = "BMI = {:.2f}. {}" # รูปแบบ form
print(textform.format(bmi, result)) # แสดงข้อความโดยใช้ฟังก์ชั่น format
print('----------------------------------------------------')
