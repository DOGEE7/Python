# python基础
# 模板
import math

print(int(math.floor(32.9)))

# input
name = input("What is your name?")
# name = 'Alice'
print("Hello, " + name + "!")

# 格式化字符串
print("%05d-%08d" % (3, 1))  # 输出：00003-00000001
print("%.2f" % 3.1415926)  # 输出：3.14
# format()
print("hello,{0},成绩上升了{1:.1f}%".format("小米", 15.256))  # 输出：hello,小米,成绩上升了15.3%

# 序列集合list和tuple
# 可变序列集合
language = ["java", "python", "C++", "PHP", "javascript"]
print("\n" + language[3])  # PHP
print(language.pop())  # javascript
print(language.pop(2))  # C++
print(language)  # ['java', 'python', 'PHP']
language[1] = "C"
print(language)  # ['java', 'C', 'PHP']

print("\n")
List = ["Apple", 123456, True]
print(List)  # ['Apple', 123456, True]
s = ["python", "java", ["asp", "php"], "scheme"]
print(len(s))  # 4
s.insert(2, "Apple")
print(s)  # ['python', 'java', 'Apple', ['asp', 'php'], 'scheme']
s.append("java")
print(s)  # ['python', 'java', 'Apple', ['asp', 'php'], 'scheme', 'java']

# 不可变序列
print("\n")
t = (1, 2, 3)
print(t)  # (1, 2, 3)
t2 = ()
print(t2)  # ()
t3 = (1,)
print(t3)  # (1,)
t4 = ('s', 'sq', 'dw', ['swe', 'ewr'])
print(t4)  # ('s', 'sq', 'dw', ['swe', 'ewr'])
print(len(t4))  # 4

# 条件判断if
print("\n")
age = 20
print('your age is', age)
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

# input
s = input('birth:')
# s = 2000
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')
# 例子
h = input('身高（m)：')
w = input('体重(kg)：')
# h = 1.75
# w = 56
bmi = float(w) / float(h)
print('结果：')
if bmi < 18.5:
    print('过轻')
elif bmi < 25:
    print('正常')
elif bmi < 28:
    print('过重')
elif bmi < 32:
    print('肥胖')
else:
    print('严重肥胖')

# 循环
names = ['Bob', 'Alice', 'Cindy']
for name in names:
    print(name)

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum += x

print(sum)  # 55
print(range(5))  # range(0, 5)
print(list(range(5)))  # [0, 1, 2, 3, 4]

x = range(10)
sum1 = 0
for xi in x:
    sum1 += xi
print(sum1)  # 45

sum2 = 0
n = 99
while n > 0:
    sum2 += n
    n -= 2
print(sum2)  # 2500

# dict
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Bob'])  # 75
print(d.get('Alice'))  # None
print(d.get('Tracy'))  # 85
print(d.pop('Bob'))  # 75
print(d)  # {'Michael': 95, 'Tracy': 85}

# set
s = set([1, 1, 2, 2, 3, 3, 4, 5])
print(s)  # {1, 2, 3, 4, 5}
s.add(9)
print(s)  # {1, 2, 3, 4, 5, 9}
s.remove(5)
print(s)  # {1, 2, 3, 4, 9}

# str是不变对象，而list是可变对象
li = ['a', 'c', 'y', 'v', 'b']
st = 'abch'
li.sort()
print(li)  # ['a', 'b', 'c', 'v', 'y']
st.replace('h', 'd')
print(st)  # abch
