"""=========================print,import和赋值====================="""
from math import sqrt as foobar

# ==========================print和import===============
# 打印多个参数
print("age", 15)
print('Hello' + ',', 'Mr.' + 'Gumby')
print("I", "wish", "to", "register", "a", "complaint", sep="_")
print('Hello,', end='')  # 自定义结束字符串，以替换默认的换行符。例如，如果将结束字符串指定为空字符串，以后就可继续打印到当前行。
print('world!')
# 导入时重命名
print(foobar(4))
# =============================赋值=================
# 序列包赋值
x, y, z = 1, 2, 3
print(x, y, z)
x, y = y, x
print(x, y, z)
scoundrel = {'name': 'Robin', 'girlfriend': 'Marion'}
key, value = scoundrel.popitem()
print(key, value)
a, b, *rest = [1, 2, 3, 4]  # 可使用星号运算符（*）来收集多余的值，这样无需确保值和变量的个数相同
print(rest)
name = "Albus Percival Wulfric Brian Dumbledore"
first, *middle, last = name.split()
print(middle)
a, *b, c = "abc"
print(a, b, c)  # a ['b'] c
# 链式赋值
x = y = 2
print(x, y)
# 增强赋值
x = 2
x += 1
x *= 2
print(x)