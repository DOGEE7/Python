# ============================分析文本=============================
# 计算一个文件大致包含多少个单词
def count_words(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry,the file does not exit!"
        print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        print('content:' + str(words))
        print('num_words:' + str(num_words))

filename = 'file/file.txt'
count_words(filename)


# =========================存储数据=======================
import json

# json.dump() json.load()
numbers = [2, 3, 4, 6, 8, 9, 21, 45]
# strings = ['American', 'China', 'Canada', 'Japanese', 'France']
filename = 'file/number.json'
with open(filename, 'w')as f_obj:
    json.dump(numbers, f_obj)
    # json.dump(strings, f_obj)

with open(filename)as f_obj1:
    number = json.load(f_obj1)
print(number)

# 保存和读取用户生成的数据
username = input('What is your name?')
filename1 = 'file/username.json'
with open(filename1, 'w')as f_obj2:
    json.dump(username, f_obj2)
    print("We'll remember you when you come back," + username + '!')

with open(filename1)as f_obj3:
    username1 = json.load(f_obj3)
print("Welcome back!" + username1)

# 合二为一
filename2 = 'file/username.json'
try:
    with open(filename2)as f_obj4:
        username2 = json.load(f_obj4)
except FileNotFoundError:
    username2 = input("what is your name?")
    with open(filename2, 'w')as f_obj4:
        json.dump(username2, f_obj4)
        print("We'll remember you when you come back," + username2 + '!')
else:
    print("Welcome back!" + username2)


# ============================单元测试和测试用例=====================

