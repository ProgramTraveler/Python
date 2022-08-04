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