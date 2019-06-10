"""==========================条件语句======================="""
# ======================条件语句================
name = input("What's your name?")
status = "friend" if name.endswith("Gumby") else "stranger"  # 三目运算符
print("Hello,", status + "!")
# ===========================更复杂的条件==================
# 链式比较
age = 21
print(0 < age < 200)
# 两个布尔运算符：or和not
print(56 > 0 and 56 < 100)  # True
# is运算符
x = y = [1, 2, 3]
z = [1, 2, 3]
print(x is y)
print(x is z)  # False  ==用来检查两个对象是否相等，而is用来检查两个对象是否相同（是同一个对象）。
print(x == z)
# 字符串和序列的比较
print('slpa' < 'bedj')  # False
# 断言
age = -1
assert 0 < age < 100, 'The age must be realistic!!!'
