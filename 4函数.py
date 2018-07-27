# abs
print(abs(-12.56))  # 12.56
# max
print(max(1, 6, 9, -5, 5, 8))  # 9
# 数据类型转换
print(int('123'))  # 123
print(int(12.35))  # 12
print(float('123.2'))  # 123.2
print(str(12.55))  # 12.55
print(bool(1))  # True
print(bool(''))  # False

# 十进制转十六进制
n1 = 255
print(hex(n1))  # 0xff

# 定义函数
import math
PI = math.pi
def circle_area(r):
    if r >= 0:
        return PI * r ** 2
    else:
        return 'Error'
x = 5
print('%.2f' % circle_area(x))

# 空函数
def nop():
    pass
age = 9
if age >= 18:
    pass