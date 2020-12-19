"""
date:2020-12-19
author:王久铭
"""
a = input("Input Number:");
# input输入的默认为字符串类型
ans = int (a)
if (ans % 2 == 0) :
    ans = ans **  2;
else :
    ans = ans ** 3
print(ans)