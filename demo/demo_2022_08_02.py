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




