#-------------------------------------------------------------------------------
# Name:        zuoye5
# Purpose:
#
# Author:      王久铭
#
# Created:     07/06/2019
# Copyright:   (c) 王久铭 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
n=input()
for i in n :
    if ord("a") <= ord(i) <= ord("z") :
         print(chr(ord("a")+(ord(i)-ord("a")+3)%26),end ='')
    else :
         print(i,end ='')
