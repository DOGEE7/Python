"""================列表================="""
# 函数list
lists = list('Hello')
print(lists)
print(''.join(lists))

# 基本的列表操作
x = [1, 1, 3]  # 给元素赋值
x[1] = 2
print(x)
names = ['Alice', 'Bob', 'Cindy', 'Davi']  # 删除元素
del names[3]
print(names)
name = list('Perl')  # 给切片赋值
print(name)
name[2:] = list('ar')
print(name)
name[1:] = list('ython')
print(name)
numbers = [1, 5]
numbers[1:1] = [2, 3, 4]
print(numbers)  # [1, 2, 3, 4, 5]
numbers[1:4] = []
numbers = numbers * 5
print(numbers)
numbers[1:10:4] = [11, 9, 99]
print(numbers)  # [1, 11, 1, 5, 1, 9, 1, 5, 1, 99]

# 列表方法
lst = [1, 2, 3]
lst.append(4)  # append对象并返回
print(lst)
lst.clear()  # <==>lst[:]=[] clear对象并返回
print(lst)
a = [9, 8, 7, 6]
b = a  # 常规复制只是将另一个名称关联到列表（a,b指向同一个列表）
b[1] = 22
print(b)
print(a)
c = a.copy()  # copy
c[1] = 90
print(c)
print(a)
x = [[1, 2, 3], 1, 2, 3, 3, 2, 2, 2, [2, 3, 4]]
print(x.count(3))  # count
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)
print(a)  # a未被修改
a.extend(b)  # extend对象并返回
print(a)
knights = ['We', 'are', 'the', 'knights', 'who', 'say', 'ni']
print(knights.index('who'))  # index
knights.insert(3, 4)  # insert对象被返回
print(knights)
x.pop()  # pop对象并返回----------pop是唯一既修改列表又返回一个非None值的列表方法。
print(x)
print(x.pop(0))
print(x)
x = ['to', 'be', 'or', 'not', 'to', 'be']
x.remove('be')  # remove对象第一个元素并返回
print(x)
x = [1, 2, 3]
x.reverse()  # reserve
print(x)
print(list(reversed(x)))  # reversed(x)为迭代器
x = [1, 3, 547, 7, 43, 214, 23, 56]
x.sort()  # sort
print(x)
x=['We', 'are', 'the', 'knights', 'who', 'say', 'ni']
x.sort(key=len)
print(x)
x.sort(reverse=True)
print(x)
y = sorted('Python')
print(y)  # sorted
