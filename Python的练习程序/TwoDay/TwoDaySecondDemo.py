"""
date:2020-12-20
author:王久铭
"""
# 获得1-100的一组列表
num = range(1,100)
# 记录满足条件的数
res = [w for w in num if w % 10 == 3]
print(res)