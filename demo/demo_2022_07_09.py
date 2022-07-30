demo_1 = 'first'
demo_2 = 'second'

# 字符串的自带的函数
print(demo_1.upper())
print(demo_1.lower())

demo_3 = 'love'

# f 合并字符串的标志
print(f"{demo_1} {demo_2}")

# 删除空格的方方法(只能删除首和尾)
print(f" {demo_1} {demo_2} ,".rstrip())  # 看来这样不能用

# 看来只能删除字符串的末尾空格，头的空格并没有删掉
demo_4 = ' hello , '
print(demo_4.rstrip() + 'boy')
print(demo_4 + 'boy')

# 这个次方运算的方式
a = 2 ** 3
print(a)

# float * int = float(而且会以float的方式表现出来，哪怕结果是整数)
print(5.0 * 2)

# 数字分组(感觉就是方便查看)
print(130_11111_1111)

# 多变量赋值
x, y, z = 1, 2, 3

print(x, y, z)

# 注意常量的命名要全部大写这是规范

# 注释方法
'''
i am
'''
