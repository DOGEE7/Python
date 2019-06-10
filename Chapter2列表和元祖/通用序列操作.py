"""====================通用序列操作================"""
'''列表、字符串和元组都属于序列，其中列表是可变的（你可修改其内容），
而元组和字符串是不可变的（一旦创建，内容就是固定的）'''
# 索引
edward = ['Edward Gumby', 24]
john = ['John Smith', 50]
database = [edward, john]
print(database)
greetings = 'Hello'
print(greetings[0])
print(greetings[-1])
year = input('Year:')[2:4]
print(year)

# 切片
tag = '<a href="http://www.python.org">Python web site</a>'
print(tag[9:30])  # 第一索引值可取，第二索引值丢弃
print(tag[32:-4])
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[3:6])
print(numbers[0:1])
print(numbers[7:10])
print(numbers[-3:-1])
print(numbers[-3:0])  # []
print(numbers[-3:])
print(numbers[:3])
print(numbers[:])  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[::3])  # 步长
print(numbers[8:3:-2])
print(numbers[::-3])
print(numbers[0:10:-2])
print(numbers[5::-2])
print(numbers[:5:-2])

# 序列相加拼接
print(numbers[:3] + numbers[3:6])
print('Hello,' + 'world!')
# print('Hello' + [1, 2, 3])  # TypeError: can only concatenate str (not "list") to str

# 乘法
print('python ' * 5)
print([0, 1, 0] * 5)
sequence = [None] * 10
print(sequence)

# 成员资格
permissions = 'dewfd'
print('w' in permissions)
users = ['Yanir', 'Alice', 'Cindy']
print(input('Enter your user name:') in users)
subject = '$$$ Get rich now!!! $$$'
print('$$$' in subject)
# 检查用户名和PIN码
database = [
    ['albert', '1234'],
    ['dilbert', '4242'],
    ['smith', '7524'],
    ['jones', '9843']
]
username = input('User name: ')
pin = input('PIN code: ')
if [username, pin] in database: print('Access granted')
lists = [22, 45, 432, 12]
print(len(lists))
print(max(lists))
print(min(lists))

