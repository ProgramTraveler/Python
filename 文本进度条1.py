#-------------------------------------------------------------------------------
# Name:        文本进度条
# Purpose:
#
# Author:      王久铭
#
# Created:     17/07/2019
# Copyright:   (c) 王久铭 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import time
scale = 100
print("执行开始".center(scale // 2,"-"))
start = time.perf_counter()
for i in range(scale + 1):
    a = "*" * i
    b = "." * (scale - i)
    c = (i / scale) * 100
    dur = time.perf_counter() - start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end = "")
    time.sleep(1)
print("\n"+"执行结束".center(scale // 2,"-"))
