def square(x):
    'Calculates the square of the number x.'
    return x * x


# 给函数编写文档
print(square.__doc__)
help(square)  # 可使用它获取有关函数的信息，其中包含函数的文档字符串。


# 收集参数
def in_the_middle(x, *y, z):  # 星号意味着收集余下的位置参数。如果没有可供收集的参数，y将是一个空元组。
    print(x, y, z)


in_the_middle('Params:', 1, 2, 3, 4, z=5)


def print_param_3(**params):  # 要收集关键字参数，可使用两个星号。
    print(params)


print_param_3(x=1, y=2, z=3)  # {'x': 1, 'y': 2, 'z': 3}


# 分配参数
def add(x, y):
    return x + y


params = (1, 2)
print(add(*params))


def hello_3(greeting, name):
    print('{},{}!'.format(greeting, name))


params = {'name': 'Sir Robin', 'greeting': 'Well met'}
hello_3(**params)


# 作用域
def combine(parameter):
    print(parameter + globals()['parameter'])


parameter = 'berry'
combine('Shrub')

