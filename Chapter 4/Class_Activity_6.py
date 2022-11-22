# 64114069 เศรษฐพงษ์ เคียนเขา
# ข้อที่ 1
def average(num_list): # สร้าง function หาค่าเฉลี่ย
    sum = 0 # กำหนด sum = 0
    for n in num_list: # for loop list
        sum += n # บวกเพิ่มไปใน sum
    avg = float(sum / len(num_list)) # คืนค่าโดย sum/len(num_list)
    return avg # คืนค่า avg
numberint = [57, 34, 102, 46, 54, 22, 61] # list(numberint)
print(average(numberint)) # เรียกใช้ function หาค่าเฉลี่ย
print("-"*52)

# ข้อที่ 2
def body_temp(): # สร้าง function ตรวจสอบอุณหภูมิในร่างกาย
    # รับค่าอุณหภูมิเป็นตัวเลขแบบ float เก็บไว้ในตัวแปร tem(temperature)
    tem = float(input("Temperature Input: ")) 
    if tem >= 37.5: # ถ้า tem มากกว่า 37.5
        result = True # เก็บค่า True ใน result
    else: # ถ้านอกเหนือจากนั้น
        result = False # เก็บค่า False ใน result
    return result # คืนค่า result
print(body_temp()) # เรียกใช้ function ตรวจสอบอุณหภูมิในร่างกาย
print("-"*52)

# ข้อที่ 3
def patient(name, age, symptoms): # สร้าง function เก็บข้อมูลผู้ป่วย
    # แสดงข้อมูลโดยใช้รูปแบบ format
    print("Name: {}\nAge: {}\nSymptons: {}".format(name, age, symptoms))
# เรียกใช้ function โดยกำหนดและใส่ค่าใน Argument 3 ตัว 
patient(name="Setthapong Kiankhao" ,age="19", symptoms="flu")
print("-"*52)