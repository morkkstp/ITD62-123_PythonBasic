# Class Acticity 3 ข้อที่ 2
deposit = int(input("Enter deposit: "))
if deposit >= 1 and deposit <= 10000:
    interest = int(deposit * 0.02)
elif deposit >= 10001 and deposit <= 50000:
    interest = int(deposit * 0.03)
elif deposit >= 50001 and deposit <= 100001:
    interest = int(deposit * 0.04)
else:
    interest = int(deposit * 0.05)
textform = "interest = {}"
print(textform.format(interest))
