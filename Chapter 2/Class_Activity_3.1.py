# Class Acticity 3 ข้อที่ 1
number1 = int(input("Enter Number: "))
number2 = int(input("Enter Number: "))
sum = number1 + number2
textform = "{} + {} = {}"
print(textform.format(number1, number2, sum))
if sum > 50:
    print("Greater than 50")
