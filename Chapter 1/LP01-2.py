#โปรแกรมเปลี่ยนค่าเงิน USD To THB
from datetime import datetime # daretime object containing current date and time

now = datetime.now()
dt_string = now.strftime("%D%m%Y %H:%M:%S") # dd/mm/YY H:M:S
print("Exrcuted time: ", dt_string)
name = 'Setthapong Kiankhao'
std_id = '64114069'
lab = 'LP01-2'
print(lab +' Name: '+name+' Student ID:'+ std_id)
print('----------------------------------------------------')

#Command Script & Variable
print("Welcome to Exchange kiosk")
exchange_rate = float(input("Today THB-USD exchange rate: ")) # รับค่าอัตราการแลกเปลี่ยน
usd = int(input("$USD amount: ")) # รับค่าเงินดอลล่าร์ (USD)
print("----------------------------------------------------")
thb = int(usd * exchange_rate) # สูตเปลี่ยนเป็นเงินไทย
fee = thb * 0.02 # สูตรหาค่าธรรมเนียม
net = int(thb - fee) # สูตรหาค่าเงินสุทธิ
textform = "{} USD = {} THB, Fee = {:.2f} THB \nNet {} THB" # form
print(textform.format(usd, thb, fee, net)) # แสดงแบบฟอร์มจาก textform โดยใช้ฟังก์ชั่น format และเรียงตัวแปรตามลำดับ
print("----------------------------------------------------")
print("Bank note and coin")
bntext = "Banknote {} : {}" # form
ctext = "Coin {} : {}" # form
money = [1000, 500, 100, 50, 20, 10, 5, 2, 1] # list สำหรับเก็บค่าเงินต่างๆ
for m in money: # m แทน money
    if m >= 20: # ตรวจสอบเงื่อนว่าตัวแปร m มีค่ามากว่าหรือเท่ากับ 20 หรือไม่
        print(bntext.format(m, int(net / m))) # ปริ้นโดยการนำค่า net / m
        net %= m # นำค่าเงินสุทธิ (net) มา Mod กับ money
    else:
        print(ctext.format(m, int(net / m))) # ปริ้นโดยการนำค่า net / m
        net %= m # นำค่าเงินสุทธิ (net) มา Mod กับ money
print("----------------------------------------------------")
