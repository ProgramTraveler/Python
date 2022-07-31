#### 仓库说明
* Python语言的一些简单的练习，简单了解它的语法和使用方式

#### 对python的进一步了解
* 之前上传的内容只是对`python`语法的简单了解而且时间是在18和19年，大部分内容都已经忘记的差不多了
* 考虑到以后会对`python`语言的使用和了解，开始对`python`进行进一步的学习
* 对`python`的练习文档存放在`demo`文件中

#### 2022-07-29 变量和简单数据类型

```py
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

```

#### 2022-07-31 列表简介

```py
# 列表
a = [1, 2, 3]
print(a)

# 访问元素
print(a[0])

# 返回最后一个元素(索引指定为-1),当列表为空时才会出现错误
print(a[-1])

# 修改列表元素就和数组一样,同时也能添加列表元素(也是和平常使用的函数一样)
a.append(4)
print(a)

# 插入元素,将-1插入到下标为0的位置
a.insert(0, -1)
print(a)

# 删除元素,这个操作和之前的不一样,并不是直接调用函数
del a[0]
print(a)

# 使用pop删除元素(我还是喜欢叫它弹出元素),看来弹出的是最后的一个元素,弹出的元素当然不会在原列表中了
b = a.pop()
print(a)
print(b)

# 弹出任意位置的值(这个我在c++中没有使用过)
c = a.pop(-1)
print(c)

# 根据值来删除列表中的元素(只删除第一个在列表中出现的)
d = [1, 1, 1, 1, 0, 2, 3, 5, 6, 6, 5]
d.remove(5)
print(d)

# sort排序yyds
e = ['c', 'd', 'a', 'b', 'c', 'f']
e.sort()
print(e)

# 使用sort反序,在c++中我是直接调用reverse
e.sort(reverse=True)
print(e)

# 使用sorted临时排序,不会对原列表产生影响,注意sorted是函数,不能这样使用e.sorted()
print(sorted(e))
print(e)

# 反序打印
f = ['c', 'd', 'a', 'b', 'c', 'f']
f.reverse()
print(f)

# 列表长度len()函数
print(len(f))

```