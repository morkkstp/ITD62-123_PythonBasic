from datetime import datetime # daretime object containing current date and time
now = datetime.now()
dt_string = now.strftime("%d%m%Y %H:%M:%S") # dd/mm/YY H:M:S
print("Exrcuted time: ", dt_string)
name = 'Setthapong Kiankhao'
std_id = '64114069'
lab = 'LP01-1'
print(lab +' Name: '+name+' Student ID:'+ std_id)
print('----------------------------------------------------')

# variables declaration
number1 = 50
number2 = 35
summation = 0

# command script
print('Hello World')
print('This is my first program')

summation = number1+number2
txtPrint = '{} + {} = {}'
print(txtPrint.format(number1,number2,summation))