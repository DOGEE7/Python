"""=========camth和math==========="""
import cmath
import math

# print(math.sqrt(-1))
print(cmath.sqrt(-1))
print((1 + 3j) * (3 - 8j))
"""========turtle============"""
from turtle import *

forward(100)
left(120)
forward(100)
left(120)
forward(100)
right(120)
penup()
# pendown()

"""===========字符串==============="""
print('a', 'b')
print('a' 'b')
print('a' + 'b')
print('"Hello!"She said.')
print("Let's go")
print('Let\'s go')
print("\"Hello!\"She said.")

""" =============str和repr=============="""
print("Hello,\nworld!")
print(str("Hello,\nworld!"))
print(repr("Hello,\nworld!"))

"""=============长字符串，原始字符串和字节============"""
# 长字符串
print('''This is a very long string. It continues here.
And it's not over yet. "Hello, world!"
Still here.''')
print("""This is a very long string. It continues here.
And it's not over yet. "Hello, world!"
Still here.""")
print("Hello, \
 world!")
print(1 + 2 + \
      4 + 5)
print \
    ('Hello,world!')
# 原始字符串
print('C:\\nowhere')
print(r'C:\nowhere')
print(r'C:\Program Files\fnord\foo\bar\baz\frozz\bozz')
print(r'Let\'s go!')
# print(r"This is illegal\")
# 请注意，指定原始字符串时，可使用单引号或双引号将其括起，还可使用三引号将其括起。

# Unicode/bytes/bytearray
# 指定Unicode字符的通用机制：使用16或32位的十六进制字面量（分别加上前缀\u或\U）或者使用字符的Unicode名称（\N{name}）。
print("\u00c6")
print("\U0001F60A")
print("This is a cat: \N{Cat}")
print("This is a dog:\N{Dog}")
# 不可变的bytes和可变的bytearray。
print(b'Helle,world!')
# 使用ASCII、UTF-8和UTF-32编码将字符串转换为bytes。
print("Hello,world!".encode("ASCII"))
print("Hello, world!".encode("UTF-8"))
print("Hello, world!".encode("UTF-32"))
print(len("Hello, world!".encode("UTF-8")))
print(len("Hello, world!".encode("UTF-32")))
# print("Hællå, wørld!".encode("ASCII"))
print("Hællå, wørld!".encode("UTF-8"))
print("Hællå, wørld!".encode("ASCII", "ignore"))
print("Hællå, wørld!".encode("ASCII", "replace"))
print("Hællå, wørld!".encode("ASCII", "backslashreplace"))
print("Hællå, wørld!".encode("ASCII", "xmlcharrefreplace"))
print("Hællå, wørld!".encode())
print(b'H\xc3\xa6ll\xc3\xa5, w\xc3\xb8rld!'.decode())
print(bytes("Hællå, wørld!", encoding="utf-8"))
print(str(b'H\xc3\xa6ll\xc3\xa5, w\xc3\xb8rld!', encoding="utf-8"))
# Python还提供了bytearray，它是bytes的可变版
x = bytearray(b"Hello!")
x[1] = ord(b"u")
print(x)

# =================函数=============
# help()
name = input("What's your name?")
print("Hello! " + name)
print(math.ceil(32.5))
print(math.floor(32.5))
print(pow(3, 5, 4))  # 返回x的y次方对z求模的结果
print(round(25.256467864, 5))  # round(number[, ndigits]) 四舍五入为指定的精度，正好为5时舍入到偶数
