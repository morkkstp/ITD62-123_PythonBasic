from datetime import datetime # daretime object containing current date and time
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S") # dd/mm/YY H:M:S
print("Exrcuted time: ", dt_string)
name = "Setthapong Kiankhao"
std_id = "64114069"
quiz = "Quiz-2"
print(quiz +" Name: "+name+" Student ID:"+ std_id)
print("-"*52)
print("Elevator controller program...")
print("-"*52)
human = 0 # เก็บจำนวนคน
weighthuman = [] # เก็บค่าน้ำหนักคน
weightresult = [0] # เก็บน้ำหนักล่าสุด
while human < 15: # ถ้า จำนวนคนน้อยกว่า 15
    # รับค่าน้ำหนัก
    amounthuman = int(input("Enter person {} weight: ".format(human+1)))
    # เพิ่มน้ำหนักไปใน list(weighthuman)
    weighthuman.append(amounthuman)
    human += 1 # บวกจำนวนคน
    if amounthuman == 0: # ถ้าน้ำหนักเท่ากับ 0 
        human -= 1 # ลบจำนวนคน
        break # หยุด
    total = 0 # ผลรวมของน้ำหนัก
    for wh in weighthuman: # for loop
        total += wh # บวกน้ำหนักไปที่ total 
        weightresult[0] = wh # เพิ่มน้ำหนักไปที่ list(weightresult)
    if total >= 1200: # ถ้า total มากกว่า 1200
        print("-"*52)
        # แสดงผลว่าคนเกิน
        print("Warning:\nPerson {} is Over weight, Please leave...".format(human))
        human -= 1 # ลบจำนวนคน
        # แสดงผลลัพธ์ โดยที่แสดงจำนวนคนและค่าน้ำหนักที่คำนวณล่าสุดโดยที่เอาผลรวมของน้ำหนักมาลบกับlistที่เก็บน้ำหนักล่าสุด
        print("Door closed, {} person(s), Total weight {} KG.".format(human, total - weightresult[0]))
        break # หยุด

if total < 1200: # ถ้า total น้อยกว่า 1200
    print("-"*52)
    # แสดงผลลัพธ์ 
    print("Door closed, {} person(s), Total weight {} KG.".format(human, total))
