#-------------------------------------------------------------------------------
# Name:        zuoye2
# Purpose:
#
# Author:      王久铭
#
# Created:     07/06/2019
# Copyright:   (c) 王久铭 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
n=int(input())
for i in range(1,n+1):
    m=int(input())
    if m%2!=0:
        print(0,0)
    else:
        a=int(m/2)
        b=int(m/4)
        print(b,a)