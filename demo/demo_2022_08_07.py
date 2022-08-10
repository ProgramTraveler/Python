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

