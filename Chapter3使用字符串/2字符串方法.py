"""========================"字符串方法==============="""
# center
import string

print("The Middle by Jimmy Eat World".center(39))
print("The Middle by Jimmy Eat World".center(39, "*"))
# find
print('With a moo-moo here, and a moo-moo there'.find('moo'))
title = "Monty Python's Flying Circus"
print(title.find("Monty"))
print(title.find("Python"))
print(title.find("Flying"))
print(title.find("Zirquss"))
subject = '$$$ Get rich now!!! $$$'
print(subject.find("$$$"))
print(subject.find("$$$", 1))
print(subject.find("!!!"))
print(subject.find("!!!", 0, 16))  # 请注意，起点和终点值（第二个和第三个参数）指定的搜索范围包含起点，但不包含终点。这是Python惯常的做法。
# join
a = ['1','2', '3', '4', '5']
b = "+"
print(b.join(a))
dirs = '', 'usr', 'bin', 'env'
print('C:'+'\\'+'\\'.join(dirs))
# lower
print('TRondheim Hammer Dance'.lower())
print("that's all folks".title())
print(string.capwords("that's all, folks"))
# replace
print('This is a test'.replace('is', 'eez'))
# split
print('1+2+3+4+5'.split('+'))
print('/usr/bin/env'.split('/'))
print('Using the default'.split())
# strip
print(' internal whitespace is kept '.strip())




