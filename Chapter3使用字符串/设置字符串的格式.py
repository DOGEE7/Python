"""============================设置字符串的格式=========================="""
import math
from math import pi
from string import Template
from math import e

website = 'http://www.pythoon.org'
# website[-3:] = 'com'  # 字符串是不可变的，因此所有的元素赋值和切片赋值都是非法的。
print(website)

# 转换说明符
format = "Hello,%s. %s enough for you?"
value = ('world', 'Hot')
print(format % value)
format = "Pi with three decimals:.%.3f"
print(format % pi)

# 模板字符串
tmpl = Template("Hello.$who! $what enough for you?")
print(tmpl.substitute(who="Mars", what="Dusty"))
print("{},{} and {}".format("first", "second", "third"))
# 字符串方法format
print("{0},{1} and {0}".format("first", "second", "third"))  # first,second and first
print("{3} {0} {2} {1} {3} {0}".format("be", "not", "or", "to"))
print("{name} is approximately {value:.2f}.".format(value=pi, name="π"))
print(f"Euler's constant is roughly {e}")
print("Euler's constant is roughly {v}.".format(v=e))

# -------------详述format------------
# 替换字段名
print("{foo} {} {bar} {}".format(1, 2, bar=4, foo=3))
print("{foo} {0} {bar} {1}".format(2, 4, bar=3, foo=1))
fullname = ["Alfred", "Smoketoomuch"]
print("Mr {name[1]}".format(name=fullname))
tmpl = "The {mod.__name__} module defines the value {mod.pi} for π"
print(tmpl.format(mod=math))
# 基本转换
print("{pi!s} {pi!r} {pi!a}".format(pi='π'))  # r（表示repr）、s（表示str）和a（表示ascii）
print("The number is {num}".format(num=42))
print("The number is {num:f}".format(num=42))
print("The number is {num:b}".format(num=42))
# 宽度、精度和千位分隔符
print("{num:10}".format(num=3))
print("{name:10}".format(name="Bob"))
print("Pi day is {pi:.2f}".format(pi=pi))
print("{pi:10.2f}".format(pi=pi))
print("{:.5}".format("Guido van Rossum"))
print("One goolol is {:,}".format(10 ** 100))
# 符号、对齐和用0 填充
print('{:010.2f}'.format(pi))
print("{0:<10.2f}\n{0:^10.2f}\n{0:>10.2f}".format(pi))
print("{:$^15}".format(" WIN BIG "))
print('{0:10.2f}\n{1:10.2f}'.format(pi, -pi))
print('{0:10.2f}\n{1:=10.2f}'.format(pi, -pi))
print("\n")        # 如果要给正数加上符号，可使用说明符+（将其放在对齐说明符后面），而不是默认的-。如果将符号说明符指定为空格，会在正数前面加上空格而不是+
print('{0:-.2}\n{1:-.2}'.format(pi, -pi))  # 默认设置
print('{0:+.2}\n{1:+.2}'.format(pi, -pi))
print('{0: .2}\n{1: .2}'.format(pi, -pi))
print("{:b}".format(42))    # 转换细节随类型而异。例如，对于二进制、八进制和十六进制转换，将加上一个前缀。
print("{:#b}".format(42))
print("{:g}".format(42))    # 对于各种十进制数，它要求必须包含小数点（对于类型g，它保留小数点后面的零）。
print("{:#g}".format(42))