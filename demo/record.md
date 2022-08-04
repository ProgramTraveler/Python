### python 的学习过程

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

#### 2022-08-02 操作列表

```py

# 遍历列表
a = [1, 2, 3, 5, 7, 8]
# py属性默认为换行符\n，此时将end属性改为‘’，就不会自动换行了。
for i in a:
    print(i, end="")
print("")

b = ['help', 'peter', 'java']
for i in b:
    # title会使字母开头大写
    print(f"{i.title()}, that is good")

# 使用range()创建数值,rang(1, 5)只会显示1234,属于前包后开的形式
for value in range(1, 5):
    print(value, end="")
print("")
# 也可以使用一个参数,输出的结果为0-4
for value in range(5):
    print(value, end="")
print("")

# 使用list创建数值列表
num = list(range(1, 5))
print(num)

# 使用range()可以指定步长,从2开始,每次加2直到超出规定值11
num = list(range(2, 11, 2))
print(num)

# demo
sq = []
for value in range(1, 5):
    sq.append(value ** 2)
print(sq)

# 对数字列表的简单统计,最小值 最大值 求和
digits = [1, 2, 3, 4, 5, 6]
print(min(digits), f"", max(digits), f"", sum(digits))

# 列表的解析(代码简洁)
sq = [i ** 2 for i in range(1, 5)]
print(sq)

# 使用代码的一部分
digits = [1, 2, 3, 4, 5, 6]
# 对列表进行切片操作
print(digits[0:3])
# 如果没有指定第一个索引,py自动从列表头开始
print(digits[:3])
# 如果没有指定最后一个索引,将自动执行到最后一个
print(digits[0:])
# 显示列表后三个
print(digits[-3:])

# 遍历切片
pl = ['a', 'b', 'c', 'd', 'f']
for i in pl[0:3]:
    print(i, f"", end="")
print("")

# 复制列表(这里是将temp的副本赋给temp_copy,temp和temp_copy是两个独立的列表)
temp = ['a', 'b', 'c', 'd', 'f']
# [:]表示从第一个切片到最后一个元素
temp_copy = temp[:]
temp.append("help")
temp_copy.append("copy")
print(temp, f"", temp_copy)

# 将temp赋给temp_copy,两个变量的值指向同一个列表
temp_copy = temp
temp.append("help")
temp_copy.append("copy")
print(temp, f"", temp_copy)

# 元组
dim = (13, 20)
print(dim[0], f"", dim[1])

# 修改元组的值(会报错,元组的值无法修改)
# dim[0] = 15
# print(dim[0], f"", dim[1])

# 元组是由逗号标识的,如果你要定义只含一个元素的元组,必须在这个元素后面加上逗号
my_t = [1, ]
print(my_t)

# 遍历元组中的所有值
for i in dim:
    print(i, f"", end="")
print("")

# 无法修改元组中的元素值,但可以重新定义元组中的值
dim = [1, 2]
dim = [3, 4]
print(dim)

```

#### 2022-08-03 if语句

```py

# if语句
a = [1, 2, 3]
for i in a:
    if i == 1:
        print("true")
    else:
        print("false")


# 检查多个条件 逻辑与 and 按位与 & 逻辑或 or 按位或 |
for i in a:
    # if i > 0 and i < 2:
    # 可以简化比较
    if 0 < i < 2:
        print("true")

# 检查特定值是否在列表中,关键字 in
print(4 in a)

# 检查特定值是否不在列表中,关键字 not in
print(4 not in a)

# 布尔表达式(要大写)
b = False
c = True

# if-else-else 结构,中间使用elif
age = 12
if age < 3:
    print("1-3")
elif 3 < age < 4:
    print("3-4")
else:
    print("4-")

```

#### 2022-08-03 字典

```py
# 字典 键值对
alien = {'color': 'green', 'points': 5}
print(alien['color'])
print(alien['points'])

# 字典是一个动态结构,可以随时添加键值对
print(alien)
alien['x_position'] = 0
alien['y_position'] = 25
print(alien)

# 也可以先创建一个空的字典,再向里面添加值
# alien_0 = {}
# 为了美化代码也可以这样写 dict()
alien_0 = dict()
alien_0['color'] = 'red'
alien_0['points'] = 1
print(alien_0)

# 修改字典中的值
alien_0['color'] = 'blue'
print(f"the aline is now {alien_0['color']}")

# 删除键值对
del alien_0['points']
print(alien_0)

# 类似对象组出的字典
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'ad_ward': 'ruby',
    'phil': 'python',
}
print(favorite_languages['jen'].title())

# 使用get()来访问值,使用get()在指定的键不存在的时候返回一个默认值
# 如果有该键,返回与之相关联的的值
print(alien_0.get('points', 'no point value assigned'))
print(alien_0.get('points',))

# 遍历字典
for key, value in favorite_languages.items():
    print(f"{key} : {value}")

# 遍历字典中的所有键
print("")
for ke in favorite_languages.keys():
    print(f"{ke}")

# 遍历字典时会默认遍历所有的键
print("")
for name in favorite_languages:
    print(name)

# keys()并非只能用于遍历,它返回的是一个列表,因此还可以查看是否含有键
print("")
if 'peter' not in favorite_languages.keys():
    print('error')

# 遍历字典中的值
print("")
for val in favorite_languages.values():
    print(val)

# 上述做法提取字典中的所有值,但没有考虑是否重复,可以使用set
print("")
for val in set(favorite_languages.values()):
    print(val)

# 嵌套 可以将字典嵌套在列表中,也可以将列表嵌套在字典中
# 在列表中嵌套字典
print("")
a_0 = {'c': 'green', 'p': 6}
a_1 = {'c': 'red', 'p': 3}
a_2 = {'c': 'blue', 'p': 9}

aliens = [a_0, a_1, a_2]

for alien in aliens:
    print(alien)

# 在字典中嵌套列表
pizza = {
    'cru': 'thick',
    'top': ['mushrooms', 'extra cheese'],
}

# 在字典中嵌套字典
user = {
    'help': {
        'level': 'high',
        'love': 'none',
    },
    'peter': {
        'level': 'mid',
        'love': 'none',
    },
}

```

#### 2022-08-04 用户输入和while循环

```py

# input()函数
"""

message = input("tell me something")
print(message)

"""

"""

# 使用int()来获取数值的输入,input()会将输入的解读为字符串
age = input("tell me your age: ")
print(age)
print(int(age) + 2)

"""

# while循环
current_num = 1
while current_num <= 5:
    print(current_num)
    current_num += 1

# 使用while处理列表和字典
user_con = ['peter', 'help', 'tom']
while user_con:
    print(f"{user_con.pop()}", '---', end="")
print("")

# 删除为指定值的所有列表元素
num_list = [1, 1, 1, 2, 2, 3, 4, 5]
while 1 in num_list:
    num_list.remove(1)
print(num_list)

```