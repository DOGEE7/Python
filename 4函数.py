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

def circle_area(r):
    if not isinstance(r, (int, float)):
        raise TypeError('bad operand type')
    if r >= 0:
        return PI * r ** 2
    else:
        return 'Error'
x = 8
print('%.2f' % circle_area(x))  # 201.06


# 空函数
def nop():
    pass

age = 9
if age >= 18:
    pass  # 输出空白


# 返回多个值
def move(x, y, step, angle):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
print(move(4, 5, 6, PI / 2))  # (4.0, -1.0)  # 原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple
# ，按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。


# 练习
def quadratic(a, b, c):
    x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    return x1, x2
print(quadratic(1, -3, 2))      # (2.0, 1.0)


