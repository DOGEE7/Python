# ======================切片Slice=========================
L = ['a', 'b', 'c', 'd', 'f', 'e', 'g', 'f']
L1 = list(range(17))
r = []
n = 5
for i in range(n):
    r.append(L[i])
print(r)  # ['a', 'b', 'c', 'd', 'f']
print(L1[:])  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
print(L[1:3])  # ['b', 'c']
print(L[-2:])  # ['g', 'f']
print(L[-2:-1])  # ['g']
print(L[:5])  # ['a', 'b', 'c', 'd', 'f']
print(L[:6:2])  # ['a', 'c', 'f']前十个，每两个取一个
print(L[::3])  # ['a', 'd', 'g']所有数，每3个取一个
print((0, 1, 2, 3, 4, 5, 6)[:4])  # (0, 1, 2, 3)
print('ABCDEFGH'[::3])  # ADG
# 练习  利用切片操作，实现一个trim()函数，去除字符串首尾的*字符
def trim(sentence):
    n = len(sentence)
    a = 0
    b = n
    for i in range(n):
        if sentence[i] == '*':
            a = i+1
        else:
            break
    j = n - 1
    while sentence[j] == '*':
        j -= 1
    b = j + 1
    return sentence[a:b]
l = '***This is Python!****'
print(trim(l))

# =====================迭代=======================
d = {'city': 'Xiamen', 'college': 'HQU', 'age': 20, 'profession': 'Network Engineer'}
for k, v in d.items():
    print(str(k) + ':' + str(v))
# city:Xiamen
# college:HQU
# age:20
# profession:Network Engineer

from collections import Iterable,Iterator
print(isinstance('abc', Iterable))  # str是否可迭代 True
print(isinstance([1, 2, 3, 4], Iterable))  # list是否可迭代 True
print(isinstance(123, Iterable))  # False

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
# city:Xiamen
# college:HQU
# age:20
# profession:Network Engineer

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)
# 1 1
# 2 4
# 3 9

# 练习
def findMinAndMax(L):
    max = L[0]
    min = L[0]
    for index, value in enumerate(L):
        if min > L[index]:
            min = L[index]
            # print('min=' + str(min))
        if max < L[index]:
            max = L[index]
            # print('max=' + str(max))
    T = (min, max)
    print(T)
L = [55, 96, 22, 57, 45, 36, 16, 20]
findMinAndMax(L)    # (16, 96)

# ========================列表生成式=====================
print(list(range(1, 11)))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print([x * x for x in range(1, 11)])  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print([x * x for x in range(1, 11) if x % 2 == 0])  # [4, 16, 36, 64, 100]
print([m + n for m in 'ABC' for n in 'XYZ'])  # 两层循环 ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([k + '=' + v for k, v in d.items()])  # ['x=A', 'y=B', 'z=C']

Li = ['hello', 'world', 'imb', 'apple']
print([s.upper() for s in Li])  # ['HELLO', 'WORLD', 'IMB', 'APPLE']

L1 = ['hello', 'world', 'apple', 18, None]
[s1.upper() for s1 in L1 if isinstance(s1, str)]  # ['HELLO', 'WORLD', 'IMB', 'APPLE']


# ============================生成器==============================
g = (x * x for x in range(10))
for n in g:
    print(n)
# 0
# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81

# 斐波拉契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        # print(b)
        yield (b)
        a, b = b, a + b
        n = n + 1
    return 'done'
print(fib(10))  # <generator object fib at 0x0339BB30>
for num in fib(6):
    print(num)
# 1
# 1
# 2
# 3
# 5
# 8

# 练习：杨辉三角
def triangle(n):
    L1 = [1]
    yield L1
    for i in range(n - 1):
        L2 = [1]
        # if n > 2:
        for j in range(i):
            add = L1[j] + L1[j + 1]
            L2.append(add)
        L2.append(1)
        yield L2
        L1 = L2
list1 = triangle(6)
for list_1 in list1:
    print(list_1)
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]

# =========================迭代器====================
from collections import Iterator, Iterable

# 这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。
# 可以使用isinstance()判断一个对象是否是Iterable对象
print(isinstance([], Iterable))  # True
print(isinstance({}, Iterable))  # True
print(isinstance('abc', Iterable))  # True
print(isinstance((x for x in range(10)), Iterable))  # True
print(isinstance(100, Iterable))  # False

# 使用isinstance()判断一个对象是否是Iterator(迭代器)对象
print(isinstance((x for x in range(10)), Iterator))  # True
print(isinstance([], Iterator))  # False
print({}, Iterator)  # {} <class 'collections.abc.Iterator'>
print('abc', Iterator)  # abc <class 'collections.abc.Iterator'>

# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数
print(isinstance(iter([]), Iterator))  # True
print(isinstance(iter({}), Iterator))  # True
print(isinstance(iter('abc'),Iterator)) # True
