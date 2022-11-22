# LP03-1.2
# โปรแกรมเก็บเกรดเฉลี่ยของนักศึกษา ITD
from datetime import datetime # daretime object containing current date and time
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S") # dd/mm/YY H:M:S
print("Exrcuted time: ", dt_string)
name = "Setthapong Kiankhao"
std_id = "64114069"
lab = "LP03-1"
print(lab +" Name: "+name+" Student ID:"+ std_id)
print("-"*52)
ITD_StdScore = [] # list(ITD_StdScore)
std = 1 # จำนวนนักศึกษา
while std <= 10: # while Loop ถ้านักศึกษาน้อยกว่าหรือเท่ากับ 10
    # รับค่าเกรดเฉลี่ยของนักศึกษาโดยเพิ่มข้อมูลใน list(ITD_StdScore)
    ITD_StdScore.append(float(input("Enter GPAX of Student No.{}: ".format(std))))
    std += 1 # เพิ่มจำนวนนักศึกษา
print(ITD_StdScore) # แสดงข้อมูลใน list(ITD_StdScore)
print("-"*52)
# คำนวณค่าเฉลี่ยของนักศึกษาคนที่ 2, 3, 5 โดยบวกเกรดของนักศึกษา 3 คนแล้วหาร 3
average = (ITD_StdScore[1] + ITD_StdScore[2] + ITD_StdScore[4]) / 3
print("Average of GPAX: {:.2f}".format(average)) # แสดงค่าเฉลี่ยของนักศึกษา 3 คน
print("-"*52)
maxscore = ITD_StdScore[0] # กำหนด maxscore เท่ากับ index 0 ใน ITD_StdScore
minscore = ITD_StdScore[0] # กำหนด minscore เท่ากับ index 0 ใน ITD_StdScore
for i in ITD_StdScore: # Loop โดย i เท่ากับ ITD_StdScore
    if i > maxscore: # ถ้า i มีค่ามากกว่า maxscore
        maxscore = i # maxscore จะมีค่าเท่ากับ i
    elif i < minscore: # ถ้า i มีค่าน้อยกว่า maxscore
        minscore = i # maxscore จะมีค่าเท่ากับ i
print("Max GPAX: {}".format(maxscore)) # แสดงเกรดที่เยอะที่สุด
print("-"*52)
print("Min GPAX: {}".format(minscore)) # แสดงเกรดที่น้อยที่สุด
print("-"*52)
