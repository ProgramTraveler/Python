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

n=input()
m=input()
c=int(m)
for i in n :
    if ord("A") <= ord(i) <= ord("Z") :
         print(chr(ord("A")+(ord(i)-ord("A")+c)%26),end ='')
    elif ord("a") <= ord(i) <= ord("z") :
         print(chr(ord("a")+(ord(i)-ord("a")+c)%26),end ='')
    else :
         print(i,end ='')
#print(c)