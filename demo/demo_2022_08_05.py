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


