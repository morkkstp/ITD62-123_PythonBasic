import sys # import ไฟล์จากโฟลเดอร์ WU_Python ในไดร์ฟ D
sys.path.append("D:\WU_Python")
import heading as hd # import ไฟล์ชื่อ heading.py(เป็นไฟล์เก็บหัวเรื่อง)
# ส่ง Argument "LP05-1" ไปที่ function headinglab จากไฟล์ heading.py
hd.headinglab("LP05-1")
print("-"*55)

import lp05_function as lp05func
print("MRT blue line ticket machine")
print("Press 1 for Adult ticket")
print("Press 2 for Elder/Child ticket")
print("Press 3 for Student ticket")
ticket = lp05func.pickticket() # เรียกใช้ function จาก lp05_function.py
lp05func.calticket(ticket) # เรียกใช้ function มี argument เป็น ticket
print("-"*55)