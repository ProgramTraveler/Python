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
