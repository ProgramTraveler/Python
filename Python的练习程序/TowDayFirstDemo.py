"""
date:2020-12-20
author:王久铭
"""
import random
#获取1-16中的一个随机数
Blue = random.randint(1,16)
# 获取1-33的一组列表
list = range(1,33)
# 截取其中的6个数
Red = random.sample(list,6)
# 打印结果
print("蓝球信息：" ,Blue , "红球信息：" , Red)
