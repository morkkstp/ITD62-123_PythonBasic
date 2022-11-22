# LP03-2
# โปรแกรมเก็บข้อมูลส่วนสูงและน้ำหนักของเด็กเล็ก
from datetime import datetime # daretime object containing current date and time
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S") # dd/mm/YY H:M:S
print("Exrcuted time: ", dt_string)
name = "Setthapong Kiankhao"
std_id = "64114069"
lab = "LP03-2"
print(lab +" Name: "+name+" Student ID:"+ std_id)
print("-"*52)
# รับค่าจำนวนเด็กเล็ก
children_amount = int(input("Children record list... \nHow many children(s): "))
print("-"*52)
weight_children = [] # list เก็บค่าน้ำหนัก
height_children = [] # list เก็บค่าส่วนสูง
amountchild = 0 # จำนวนเด็กเล็ก
while amountchild < children_amount: # while loop ถ้า amountchild น้อยกว่า children_amount
    print("Children #{}".format(amountchild + 1)) # แสดงลำดับ
    # รับค่าน้ำหนัก แล้วเพิ่มใน list weight_children
    weight_children.append(float(input("Enter weight(kg): "))) 
    # รับค่าส่วนสูง แล้วเพิ่มใน list height_children
    height_children.append(float(input("Enter height(M): ")))
    amountchild += 1 # บวกเพิ่มอีก 1
    print("-"*52)
weight = 0 # กำหนด weight = 0
height = 0 # กำหนด height = 0
for we in weight_children: # for loop 
    weight += we # บวกค่าเพิ่มไปใน weight
for he in height_children: # for loop 
    height += he # บวกค่าเพิ่มไปใน height
avg_weight = weight / amountchild # คำนวณค่าเฉลี่ยน้ำหนัก
avg_height = height / amountchild # คำนวณค่าเฉลี่ยส่วนสูง
print("Average of weight = {:.2f} kg".format(avg_weight)) # แสดงค่าเฉลี่ยน้ำหนักของเด็กเล็ก
print("Average of height = {:.2f} M".format(avg_height)) # แสดงค่าเฉลี่ยส่วนสูงของเด็กเล็ก
print("-"*52)
