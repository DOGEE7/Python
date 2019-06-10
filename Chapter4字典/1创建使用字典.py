"""===================创建使用字典================="""
# 函数dict
items = [('name', 'Gumby'), ('age', 42)]
d = dict(items)
print(d)
d = dict(name="Cindy", age=34)
print(d)
people = {
    'Alice': {
        'phone': '2341',
        'addr': 'Foo drive 23'
    },
    'Beth': {
        'phone': '9102',
        'addr': 'Bar street 42'
    },
    'Cecil': {
        'phone': '3158',
        'addr': 'Baz avenue 90'
    }
}
labels = {
    'phone': 'phone number',
    'addr': 'address'
}
name = input("name:")
label = input("Do you want to known Phonenumber(p) or Address(a):")
if label == 'p': key = 'phone'
if label == 'a': key = 'addr'
if name in people: print("{}'s {} is {}".format(name, labels[key], people[name][key]))

# 将字符串格式设置功能用于字典
phonebook = {'Beth': '9102', 'Alice': '2341', 'Cecil': '3258'}
print("Cecil's phone number is {Cecil}.".format_map(phonebook))

template = '''<html>
<head><title>{title}</title></head>
<body>
<h1>{title}</h1>
<p>{text}</p>
</body>'''
data = {'title': 'My Home Page', 'text': 'Welcome to my home page!'}
print(template.format_map(data))

# -------------------字典方法------------------
# clear
d = {'age': 42, 'name': 'Gumby'}
print(d)
d.clear()
print(d)
x = {}
y = x
x['key'] = 'value'
x = {}
print(x)  # {}
print(y)  # {'key': 'value'} x,y各自指向一个场景
x = {}
y = x
x['key'] = 'value'
print(y)  # {'key': 'value'}
x.clear()
print(y)  # {}  x,y指向同一个场景
# copy
x = {'username': 'admin', 'machines': ['foo', 'bar', 'baz']}
y = x.copy()  # 潜复制
y['username'] = 'mlh'
y['machines'].remove('bar')
print(x)
print(y)
from copy import deepcopy

d = {}
d['names'] = ['Alfred', 'Bertrand']
c = d.copy()
dc = deepcopy(d)  # 深复制
d['names'].append('Clive')
print(c)
print(dc)
# get
d = {}
print(d.get('name'))  # None
print(d.get('name', 'N/A'))  # name键值若不存在，则默认N/A
# items
d = {'title': 'Python Web Site', 'url': 'http://www.python.org', 'spam': 0}
print(d.items())  # 返回值属于一种名为字典视图的特殊类型
it = d.items()
d['spam'] = 1  # 视图的一个优点是不复制，它们始终是底层字典的反映，即便你修改了底层字典亦如此。
print(('spam', 0) in it)
d['spam'] = 0
print(('spam', 0) in it)
print(list(d.items()))
# keys
print(d.keys())
# pop
print(d.pop('title'))
print(d)
# popitem
d = {'url': 'http://www.python.org', 'spam': 0, 'title': 'Python Web Site'}
print(d.popitem())
print(d)
# setdefault
d = {}
d['name'] = 'Gumby'
d.setdefault('name', 'N/A')
print(d)
# update
d = {
    'title': 'Python Web Site',
    'url': 'http://www.python.org',
    'changed': 'Mar 14 22:09:15 MET 2016'
}
x = {'title': 'Python Language Website'}
d.update(x)
print(d)
# values
d = {1: 1, 2: 2, 3: 3, 4: 1}
print(d.values())
