import sys
sys.path.append("D:\WU_Python")
import heading as hd
hd.headinglab("Quiz 4")
print("-"*55)

import numpy as np

def outputtable(table, days):
    print("Day {}:".format(days))
    times = 0
    for i in table:
        print("times#{}: {}".format(times+1, i))
        times += 1
    average = sum(table) / len(table)
    print("Average: {:.1f}".format(average))
    print("-"*55)

days1 = np.array([70, 75, 80, 88, 72, 92])
days2 = np.array([99, 101, 80, 85, 79, 82])
days3 = np.array([100, 89, 95, 120, 122, 99])

outputtable(days1, 1)
outputtable(days2, 2)
outputtable(days3, 3)