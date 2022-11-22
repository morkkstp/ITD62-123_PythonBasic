# import ไฟล์จากโฟลเดอร์ WU_Python ในไดร์ฟ D
import sys
sys.path.append("D:\WU_Python") # ในวงเล็บขึ้นอยู่กับที่อยู่ไฟล์
import heading as hd # import ไฟล์ชื่อ heading.py(เป็นไฟล์เก็บหัวเรื่อง)
# ส่ง Argument "LP04-2" ไปที่ function headinglab จากไฟล์ heading.py
hd.headinglab("LP04-2")
print("-"*52)

# import function จากไฟล์ lp04_2_utilityfunc
import lp04_2_utilityfunc as lp04func
# เรียกใช้ function validate_person_id โดยใส่ argument
print(lp04func.validate_person_id("1234567890121"))
print("-"*52)
# เรียกใช้ function get_email
print(lp04func.get_email())
print("-"*52)