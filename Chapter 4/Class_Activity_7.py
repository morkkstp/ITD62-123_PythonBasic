# Class Activity 7_64114069 Setthapong Kiankhao
def inputnumber(): # สร้าง function ชื่อ inputnumber
    print("Input Number")
    n1 = int(input("Enter Number 1: ")) # รับค่าตัวเลข
    n2 = int(input("Enter Number 2: ")) # รับค่าตัวเลข
    n3 = int(input("Enter Number 3: ")) # รับค่าตัวเลข
    print("-"*55)
    avg = (n1 + n2 + n3) / 3 # คำนวณค่าเฉลี่ย
    if avg > (n1 + n2): # if ถ้าค่าเฉลี่ยมากกว่าผลรวมของ n1 และ n2
        print("The End") # แสดงข้อความคำว่า "The End"
    else: # else
        inputnumber() # เรียกใช้ function แบบ recursion
    return # return ค่ากลับไป
inputnumber() # เรียนใช้ function