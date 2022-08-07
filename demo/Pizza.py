# demo_2022_08-06的函数模块


def make_pizza(size, *toppings):
    print(size)
    for i in toppings:
        print(f"-{i}")


def greet():
    print(f"---hello---")
