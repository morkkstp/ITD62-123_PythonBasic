print("-"*55)
# 1
lotto_list = [] # list
r = 0 # r = round(กำหนดรอบ)
while r < 10: # ตรวจสอบ r(round) น้อยกว่า 10 หรือไม่
    lotto = int(input("Number lotto: ")) # รับตัวเลข lotto
    lotto_list.append(lotto) # เพิ่มค่าเข้าไปใน list
    r += 1 # เพิ่มรอบไปที่ r = round(กำหนดรอบ)
print(lotto_list) # แสดงข้อมูล lotto_list
print("-"*55)

# 2
score_list = [3.6, 5.5, 8.7, 9.9, 10.0]
sum = 0 # รวมผลรวม
nstd = 0 # จำนวนนักเรียน
for sl in range(5): # กำหนดรอบ
    sum += score_list[sl] # เพิ่มคะแนนใน list ไปที่ sum
    nstd += 1 # เพิ่มจำนวนนักเรียนไปที่ nstd
print("Average Score Student = {:.2f}".format(sum/nstd)) # แสดงค่าเฉลี่ยโดยนำ sum/nstd
print("-"*55)

# 3
score_list = [3.6, 5.5, 8.7, 9.9, 10.0]
sum = 0 # รวมผลรวม
nstd = 0 # จำนวนนักเรียน
for sl in range(5): # กำหนดรอบ
    if score_list[sl] < 9.0: # ตรวจสอบคะแนนว่าได้น้อยกว่า 9 หรือไม่
        sum += score_list[sl] # เพิ่มคะแนนใน list ไปที่ sum
        nstd += 1 # เพิ่มจำนวนนักเรียนไปที่ nstd

# แสดงค่าเฉลี่ยของนักเรียนที่ได้คะแนนน้อยกว่า 9 โดยนำ sum/nstd
print("Average Score Student < 9 = {:.2f}".format(sum/nstd))
print("-"*55)