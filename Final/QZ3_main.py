import sys
sys.path.append("D:\WU_Python")
import heading as hd
hd.headinglab("Quiz 3")
print("-"*55)

import QZ3_function as QZ3_func

call = int(input("Enter amount of calling(minute): "))
data = float(input("Enter amount of data(GB): "))
mobile = QZ3_func.mobile_billing(call, data)
discount = QZ3_func.discount(mobile)
sum = mobile - discount
tax = QZ3_func.vatable(sum)
print("Current charge {:.2f} THB".format(mobile))
print("Discount {:.2f} THB".format(discount))
print("Charge excluded vat. {:.2f} THB".format(sum))
print("Total payment {:.2f} THB (vat.7% Included)".format(sum + tax))