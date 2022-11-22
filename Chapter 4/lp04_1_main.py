# import ไฟล์จากโฟลเดอร์ WU_Python ในไดร์ฟ D
import sys
sys.path.append("D:\WU_Python") # ในวงเล็บขึ้นอยู่กับที่อยู่ไฟล์
# import ไฟล์ชื่อ heading.py(เป็นไฟล์เก็บหัวเรื่อง)
import heading as hd
# ส่ง Argument "LP04-1" ไปที่ function headinglab จากไฟล์ heading.py
hd.headinglab("LP04-1")
print("-"*52)

#import function definition
import function_def as fn

fn.calculate_circle_area(5)
fn.calculate_circle_area(8)

fn.calculate_circle_circumference(9)
fn.calculate_circle_circumference(4)

fn.calculate_rectangle_area(3, 5)
fn.calculate_rectangle_area(3, 9)

fn.calculate_triangle_area(2, 5)
fn.calculate_triangle_area(5, 9)
print("-"*52)