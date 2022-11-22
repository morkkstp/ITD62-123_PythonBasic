import numpy as np # import numpy

# สร้าง array 3 ตัว เพื่อเก็บค่า
adult = np.array([16, 16, 19, 21, 23, 26, 28, 30, 33, 35, 37, 40, 42])
elderchild = np.array([8, 8, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20, 21])
student = np.array([14, 14, 17, 19, 21, 23, 25, 27, 30, 32, 33, 36, 38])

def pickticket(): # function เลือกตั๋ว
    ipticket = int(input(": "))
    while ipticket > 3:
        print("Don't Have Ticket {}\nPlease Try Select Again".format(ipticket))
        ipticket = int(input(": "))
    if ipticket == 1: # ถ้า ticketinput เท่ากับ 1
        fare = adult[pickstation()] # เลือก array adult,ค่าของ pickstation return
    elif ipticket == 2: # ถ้า ticketinput เท่ากับ 2
        fare = elderchild[pickstation()] # เลือก array elderchild,ค่าของ pickstation return
    elif ipticket == 3: # ถ้า ticketinput เท่ากับ 3
        fare = student[pickstation()] # เลือก array student,ค่าของ pickstation return
    print("Fare = {} THB".format(fare))
    return fare # return fare

def pickstation(): # function เลือกสถานี
    ipstation = int(input("Please select station(0-18): "))
    # ถ้า ipstation มีค่ามากกว่าหรือเท่ากับ 12 และ มีค่าน้อยกว่าหรือเท่ากับ 18
    while ipstation > 18:
        print("Don't Have Station {}\nPlease Try Select Again".format(ipstation))
        ipstation = int(input("Please select station(0-18): "))
    if ipstation >= 12 and ipstation <= 18:
        return 12 # return ค่า = 12
    elif ipstation < 12: # ถ้า ipstation น้อยกว่า 12
        return ipstation # return ipstation ที่กรอกมา

def calticket(fare): # function คำนวณค่าตั๋ว
    ipcoin = int(input("Please insert bank/coin: "))
    if ipcoin >= fare:
        print("Change {} THB\nGet your ticket, Thank you".format(ipcoin - fare))
    else:
        print("Require more cash....")
        calticket(fare) # recursion function