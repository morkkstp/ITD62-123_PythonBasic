# 1
print("School of Informatics")

# 2(Method 1)
iPhonePrice = 27000
GPAX = 4
textform1 = "Iphone price is {} Bath"
textform2 = "My GPAX is {:.2f}"
print(textform1.format(iPhonePrice))
print(textform2.format(GPAX))

# 3(Method 2)
Student_name = "Setthapong Kiankhao"
student_id = "64114069"
textform3 = "Name:{} ID:{}"
print(textform3.format(Student_name, student_id))

# 4(Method 3)
university_name = input("University: ")
faculty_name = input("Faculty:")
textform4 = "University:{1} Faculty:{0}"
print(textform4.format(faculty_name, university_name))
