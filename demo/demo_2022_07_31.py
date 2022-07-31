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


