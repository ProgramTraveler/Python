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

#### 2022-08-04 字典

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

#### 2022-08-05 用户输入和while循环

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

#### 2022-08-06 函数

```py

import Pizza

from Pizza import greet as g

# 定义函数


def greet_user():
    print("hello")

# 调用函数前空两行空白行


greet_user()

# 向函数传递信息


def greet_user(name):
    print(f"hello,{name.title()}")


greet_user('help')

# 传递实参
# 位置实参,就是实参位置和形参位置相对应


def describe_pet(animal_type, pet_name):
    """
    显示宠物信息
    """
    print(animal_type, " ", pet_name)


describe_pet('dog', 'peter')
# 关键字实参,就是直接在实参中将名称和值关联起来


describe_pet(animal_type='hamster', pet_name='harry')

# 默认值


def pet(animal_type, pet_name='peter'):
    print(animal_type, " ", pet_name)


pet(animal_type='cat')

# 返回值


def get_name(name):
    return name.title()


print(get_name('peter'))

# 返回字典


def build_person(first_name, last_name):
    person = {'first': first_name, 'last': last_name}
    return person


print(build_person('xiao', 'ming'))

# 传递列表


def greet_user(name):
    for n in name:
        msg = f"hello, {n.title()}"
        print(msg)


user = ['peter', 'snake', 'margot']
greet_user(user)

# 在函数中修改列表,在函数中对列表所做的任何修改都是永久的
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']


def update(temp):
    temp.append('add')
    return temp


print(update(unprinted_designs), "---", unprinted_designs)

# 禁止函数修改列表,切片表示法[:]创建列表的副本,不影响原件


def function_name(list_name):
    list_name.append('add.')
    return list_name


print(function_name(unprinted_designs[:]), "---", unprinted_designs)

# 传递任意数量的实参,形参*toppings让python创建一共名为toppings的空元组,并将收到的所有值都封装到这个元组中


def make_thing(*toppings):
    print(toppings)


make_thing('pepperoni')
make_thing('mushrooms', 'green peperoni', 'extra cheese')

# 使用任意数量的关键字实参,形参**user_info,中的两个星号让python创建一个名为user_info的空字典


def build_profile(first, last, **user_info):
    user_info['first'] = first
    user_info['last'] = last
    return user_info


print(build_profile('albert', 'einstein', location='princeton', field='physics'))

# 将函数存储在模块中,模块是扩展名为.py的文件,见第一行


Pizza.make_pizza(16, 'mushrooms', 'green peperoni', 'extra cheese')

# 导入特定函数,见第一行


Pizza.greet()

# 使用as给函数指定别名,见第一行

g()

# 导入模块中的所有函数 from Pizza import *
```

```py
# demo_2022_08-06的函数模块


def make_pizza(size, *toppings):
    print(size)
    for i in toppings:
        print(f"-{i}")


def greet():
    print(f"---hello---")
```

#### 2022-08-07 类

```py
# 创建类
class Dog:
    # 这个初始化的结构似乎是固定的(左右都是两个下划线)
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def sitting():
        print("the dog is sitting")

    def set_name(self, new_name):
        self.name = new_name

    def add_age(self):
        self.age += 1


my_dog = Dog('peter', 5)
print(f"my dog is {my_dog.name}, he is {my_dog.age} years old")
my_dog.sitting()

# 修改属性的值
# 直接访问属性的值进行修改
my_dog.name = 'forma'
print(f"my dog now is {my_dog.name}")
# 通过方法来修改属性的值
my_dog.set_name("chrom")
print(f"my dog now is {my_dog.name}")
# 通过使用方法来对属性值进修改
my_dog.add_age()
print(f"my dog is {my_dog.age} years old")

# 继承


class ElectricDog(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)
        # 给子类定义属性
        self.color = 'red'

    # 给子类定义方法
    def jumping(self):
        print(f"{self.name} is jumping")

    # 对父类方法进行重写
    def sitting(self):
        print(f"{self.name} is sitting")


my_new_dog = ElectricDog('volt', 10)
print(f"my new dog is {my_new_dog.name}, he is {my_new_dog.age} years old")
print(f"he is {my_new_dog.color}")
my_new_dog.jumping()
my_new_dog.sitting()
```

#### 2022-08-10

```py
import json

# 从文件中读取数据
# 读取整个文件
with open('digits.txt') as file_object:
    contents = file_object.read()

# 不使用strip()的话,在输出的末尾(不是下一行)多出一个空行,因为read()在到达文件末尾时返回一个空字符串,而将这个字符串显示出来时就是一个空行(但是好像没有效果)
print(contents.rstrip())
print("---")
# 文件路径
# with open('文件路径') as file_object

# 逐行读取
file_name = 'digits.txt'
with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())
print("---")

# 创建一个包含各文件各行内容的列表
with open(file_name) as file_object:
    lines = file_object.readlines()

for i in lines:
    print(i.rstrip())
print("---")

# 使用文件的内容
pi_string = ''
for i in lines:
    pi_string += i.rstrip()
print(f"{pi_string} ---- {len(pi_string)}")

# 写入文件(如果写入的文件不存在,函数open()将自动创建它),在写入模式下,如果指定的文件已经存在,python将在返回文件对象前清空该文件的内容
file_name = 'input.txt'
with open(file_name, 'w') as file_object:
    file_object.write("i love programming")

# 写入多行,函数write()不会在写入的文本末尾添加换行符
with open(file_name, 'w') as file_object:
    file_object.write("today is a good day,")
    file_object.write("so i am happy.\n")
    file_object.write("i can do anything.\n")

# 附加到文件
with open(file_name, 'a') as file_object:
    file_object.write("I also love creating apps")
print("---")

# 异常
# 处理ZeroDivisionError异常
try:
    print(5/0)
except ZeroDivisionError:
    print("you can't divide by zero")
print("---")

# else代码块
first_num = 10
second_num = 2
try:
    answer = first_num / second_num
except ZeroDivisionError:
    print("you can't divide by zero")
else:
    print(answer)
print("---")

# 处理
file_name = 'no.txt'
try:
    with open(file_name, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    # 如果想要执行except什么都不要发生,可以使用pass
    print(f"the file {file_name} does not exist")

# 存储数据
# 使用json.dump()和json.load() 需要导入json
numbers = [2, 3, 4, 5, 6]
file_name = 'numbers.json'
with open(file_name, 'w') as f:
    json.dump(numbers, f)
print("---")

# 将列表读取到内存中
with open(file_name, 'r') as f:
    temp_num = json.load(f)
    print(temp_num)
```