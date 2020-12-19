"""
date:2020-12-19
author:王久铭
"""
temp = input("Input your grade：")
res = int (temp)
if (res > 90) :
    print("A")
elif (res > 80) :
    print("B")
elif (res > 70) :
    print("C")
elif (res >60) :
    print("D")
else :
    print("E")