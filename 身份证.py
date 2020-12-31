#-------------------------------------------------------------------------------
# Name:        模块1
# Purpose:
#
# Author:      王久铭
#
# Created:     23/03/2019
# Copyright:   (c) 王久铭 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import datetime
cur=datetime.datetime.now()
a=cur.year
c=int(a)
card=input()
b=int(card[6:10])
print("你出生于%s年%s月%s日"%(b,card[10:12],card[12:14]))
#print(card[10:12],"月")
d=int(card[10:12])
#print(card[12:14],"日")
e=int(card[12:14])
print("你今年%d周岁"%(c-b))
m=int(card[16:17])
if m==0 | m%2==0 :
    print("你的性别为女")
else :
    print("你的性别为男")
