"""===================循环==================="""
# =================while================
name = ''
while not name.strip():
    name = input('Please enter your name:')
print('Hello,{}!'.format(name))
# ================for循环=============
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    print(number)

print(list(range(0, 10)))
for number in range(1, 100):
    print(number)  # 1-99  包头不包尾
# ==============迭代字典===========
d = {'x': 1, 'y': 2, 'z': 3}
for key in d:
    print(key, 'corresponds to', d[key])
for key, value in d.items():
    print(key, 'corresponds to', value)
# =============迭代工具===============
# 并行迭代zip
names = ['anne', 'beth', 'george', 'damon']
ages = [12, 45, 32, 102]
print(list(zip(names, ages)))  # [('anne', 12), ('beth', 45), ('george', 32), ('damon', 102)]
for name, age in zip(names, ages):
    print(name, 'is', age, 'years old')
print(list(zip(range(5), range(100000000))))
# 迭代时获取索引enumerate
strings = list(zip(names, ages))
for index, string in enumerate(strings):
    if 'beth' in string:
        strings[index] = ('alice', 52)
print(strings)  # [('anne', 12), ('alice', 52), ('george', 32), ('damon', 102)]
# 反向迭代和排序后再迭代
print(sorted([4, 3, 6, 8, 3]))
print(sorted('Hello, world!'))
print(list(reversed('Hello, world!')))  # reversed像zip那样返回一个更神秘的可迭代对象
print(''.join(reversed('Hello, world!')))
print(sorted("aBc", key=str.lower))
# ================简单推导==========================
print([x * x for x in range(10)])
print([x*x for x in range(10) if x % 3 == 0])
print([(x, y) for x in range(3) for y in range(3)])

girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold', 'bob']
letterGirls = {}
for girl in girls:
    letterGirls.setdefault(girl[0], []).append(girl)
print([b+'+'+g for b in boys for g in letterGirls[b[0]]])



