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
