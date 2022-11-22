# LP03-1.1
# โปรแกรมเก็บข้อมูลหมายเลขสายการบิน
from datetime import datetime # daretime object containing current date and time
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S") # dd/mm/YY H:M:S
print("Exrcuted time: ", dt_string)
name = "Setthapong Kiankhao"
std_id = "64114069"
lab = "LP03-1"
print(lab +" Name: "+name+" Student ID:"+ std_id)
print("-"*52)
# 1
flight_landing_list = ["SL789","FD3187"] # สร้าง list 
print(flight_landing_list) # แสดงข้อมูลใน list

# 2
flight_landing_list.append(input("Enter flight no: ")) # รับค่าเพื่อเพิ่มใน list
print(flight_landing_list) # แสดงข้อมูลใน list

# 3
flight_landing_list.pop(0) # ลบ index 0
print(flight_landing_list) # แสดงข้อมูลใน list

# 4
print(flight_landing_list[1]) # แสดงข้อมูลใน list index 1

# 5
print(flight_landing_list[0]) # แสดงข้อมูลใน list index 0

# 6
flight_landing_list[0] = "FD3188" # แทนที่ FD3188 ใน list index 0
print(flight_landing_list) # แสดงข้อมูลใน list

# 7
flight_landing_list.append(input("Enter flight no: ")) # รับค่าเพื่อเพิ่มใน list
flight_landing_list.append(input("Enter flight no: ")) # รับค่าเพื่อเพิ่มใน list
print(flight_landing_list) # แสดงข้อมูลใน list

# 8
flight_landing_list.remove(input("Enter flight No. to remove: ")) # รับค่าเพื่อลบใน list
print(flight_landing_list) # แสดงข้อมูลใน list

# 9
flight_landing_list.clear() # การลบข้อมูลใน list ทั้งหมด
print(flight_landing_list) # แสดงข้อมูลใน list
print("-"*52)