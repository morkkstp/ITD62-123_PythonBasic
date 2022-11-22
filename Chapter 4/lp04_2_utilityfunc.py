# function ตรวจสอบเลขบัตรประจำตัวประชาชน
def validate_person_id(id): # สร้าง function โดยมี paramater
    n = 13 # กำหนด n เท่ากับ 13
    sum = 0 # ผลรวมของ sum
    for i in id: # for loop สำหรับคำนวณค่าเลขบัตรประชาชน
        if n == 1: # ถ้า n เท่ากับ 1
            break # ให้หยุดการทำงาน
        sum += int(i) * n # คำนวณผลรวม
        n -= 1 # n - 1
    digit = sum % 11 # ผลรวมจาก sum มา mod 11
    # abs() หรือ absolute คือ แปลงค่าจากลบเป็นบวก
    # นำ digit มาลบ 11 แล้วแปลงด้วย abs() จากนั้น mod 10
    checkdigit = abs(digit - 11) % 10
    if int(id[12]) == checkdigit: # ตรวจสอบ Check digit
        # ถ้าจริงก็ return ค่า True และรูปแบบข้อความ
        return "{} | This ID card number is {}".format(id, True)
    else:
        # ถ้าเท็จก็ return ค่า False และรูปแบบข้อความ
        return "{} | This ID card number is {}".format(id, False)

# function ตรวจสอบ email
def get_email(): # สร้าง function
    email = input("Enter Your Email: ") # รับค่า email เป็น string
    atCheck = 0 # กำหนด atCheck เป็น 0 (atCheck คือ มี @ กี่ตัว)
    dotCheck = False # กำหนด dotCheck เป็น False
    if email[0] == "@": # ตรวจสอบ @ อยู่ตัวแรก
        return get_email() # ถ้า @ อยู่ตัวแรกก็ return function
    for e in email: # for loop
        if e == "@": # ถ้า e(email) มี @
            atCheck += 1 # เพิ่มค่า atCheck เพิ่มไปอีก 1
        if atCheck > 1: # ถ้า atCheck > 1
            return get_email() # return function
        if atCheck == 1 and e == ".": # ถ้า atCheck เท่ากับ 1 และมี . อยู่หลัง @
            dotCheck = True # เปลี่ยน Boolean จาก False เป็น True
    if dotCheck: # ตรวจสอบ dotCheck ว่าเป็นจริงหรือไม่
        # ถ้าเป็นจริงให้ return email และรูปแบบข้อความ
        return "{} | This email is correct".format(email)
    else: # ถ้าเป็นเท็จ
        return get_email() # return function