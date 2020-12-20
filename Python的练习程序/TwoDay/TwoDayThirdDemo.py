"""
date:2020-12-20
author:王久铭
"""
import random
# 记录每次猜数的次数
count = 0
# 数为1-100中的随机数
num = random.randint(1,100)
# print(num)
while True :
    ans = int(input("Input Number："))
    if ans == num :
        print("You Win")
        break
    elif count >= 4 :
        print("You lose")
        break
    else:
        count = count + 1






