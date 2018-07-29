# -----------------------调用函数---------------------
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


# --------------------------定义函数-------------------------
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

# ----------------------------------函数的参数-------------------------------
# 默认参数
def enroll(name, gender, age=16, city="Fujian"):
    print("name:", name)
    print("gender:", gender)
    print('age:', age)
    print('city:', city)
print(enroll('小红', '女'))
    # name: 小红
    # gender: 女
    # age: 16
    # city: Fujian
    # None
# 必选参数在前，默认参数在后；把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数

def add_end(L=[]):
    L.append('END')
    return L
print(add_end([1, 2, 3]))   # [1, 2, 3, 'END']
print(add_end())            # ['END']
print(add_end())            # ['END', 'END']
# 默认参数必须指向不变对象！
# 修改
def add_end2(L = None):
    if L is None:
        L = []
    L.append('END')
    return L
print(add_end2())   # ['END']
print(add_end2())   # ['END']

# 可变参数
def calc(numbers):
    sum = 0
    for n in numbers:
        sum += n ** 2
    return sum
ns = [1, 2, 3, 4]
ns2 = (1, 2, 3, 4, 5)
print(calc(ns))  # 30
print(calc(ns2))  # 55
print(calc([1, 2, 3, 4]))  # 30
print(calc((1, 4, 7, 8, 5)))  # 155
# print(calc(1, 8, 9, 5, 6))

def calc2(*numbers):
    sum = 0
    for n in numbers:
        sum += n ** 2
    return sum
print(calc2(*ns))   # 30
print(calc2(*ns2))  # 55
# print(calc2([1, 2, 3, 4]))
print(calc2(1, 2, 3, 4, 8))     # 94
# print(calc2((1, 4, 7, 8, 5)))


# 关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
print(person('Alice', 30))  # name: Alice age: 30 other: {}
print(person('Bob', 55, city='Beijing'))  # name: Bob age: 55 other: {'city': 'Beijing'}
print(person('Adam', 45, gender='M', job='Engineer'))  # name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}
extra = {'city': 'Xiamen', 'job': 'student'}
print(person('Cidy', 20, **extra))  # name: Cidy age: 20 other: {'city': 'Xiamen', 'job': 'student'}


# 命名关键字参数
def person2(name, age, **kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:', name, 'age:', age, 'other:', kw)
person2('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)  # 调用者仍可以传入不受限制的关键字参数 name: Jack age 24 other: {'city': 'Beijing', 'addr': 'Chaoyang', 'zipcode': 123456}

def person3(name, age, *, city, job):
    print(name, age, city, job)
person3('Jack', 24, city='Beijing', job='Engineer3')  # *后面的参数被视为命名关键字参数 Jack 24 Beijing Engineer3

def person4(name, age, *args, city, job):
    print(name, age, args, city, job)
person4('Jack', 24, city='Beijing', job='Network Engineer')  # 命名关键字参数必须传入参数名，这和位置参数不同。Jack 24 () Beijing Network Engineer

def person5(name, age, *, city='Beijing', job):
    print(name, age, city, job)
person5('Jack', 24, job='Software Engineer')        # 由于命名关键字参数city具有默认值，调用时，可不传入city参数 Jack 24 Beijing Software Engineer


#  参数组合
# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
def f1(a, b, c=0, *args, **kw):
    print('a=', a, 'b=', b, 'c=', c, 'args=', args, 'kw=', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a=', a, 'b=', b, 'c=', c, 'd=', d, 'kw', kw)

f1(1, 2)  # a= 1 b= 2 c= 0 args= () kw= {}
f1(1, 2, c=3)  # a= 1 b= 2 c= 3 args= () kw= {}
f1(1, 2, 3, 'a', 'b')  # a= 1 b= 2 c= 3 args= ('a', 'b') kw= {}
f1(1, 2, 3, 'a', 'b', x=99)  # a= 1 b= 2 c= 3 args= ('a', 'b')可变参数 kw= {'x': 99} 命名参数
f2(1, 2, d=99, ext=None)  # a= 1 b= 2 c= 0 d= 99命名参数 kw {'ext': None}命名关键字参数

# 练习：任意几个数相乘
def product(x, *args):
    sum = 1
    if args:
        for arg in args:
            sum = sum * arg
    sum = sum * x
    # print(sum)
    return sum
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')


# -------------------------------------------递归函数-----------------------------------
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)
print(fact(10))     # 3628800

# 汉诺塔
def move(n, A, B, C):
    if n == 1:
        print(A, '-->', C)
    else:
        move(n - 1, A, C, B)        # 把n-1个盘子移动到B
        print(A, '-->', C)          # 把最“大”的盘子移动到C
        move(n-1, B, A, C)          # 把B中n-1个盘子移动到C
print(move(3, 'A', 'B', 'C'))

