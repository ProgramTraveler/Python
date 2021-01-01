#-------------------------------------------------------------------------------
# Name:        模块2
# Purpose:
#
# Author:      王久铭
#
# Created:     17/07/2019
# Copyright:   (c) 王久铭 2019
# Licence:     <your licence>
#--------------------
import time
for i in range(100):
    # 进度条
    print('>>>正在处理中: %.2f%%\r' % ((i + 1) / 100),end='') # end='' 不换行输出，默认是换行
    time.sleep(0.05) # 实际不需要这句（只是为了演示）

print('>>>处理完成！\n')
exit(0)
