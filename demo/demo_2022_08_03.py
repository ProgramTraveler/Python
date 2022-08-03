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
