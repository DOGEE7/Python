# database.py
import sys, shelve


def store_person(db):
    """让用户输入数据并将其存储到shelf对象中"""
    pid = input('Enter unique ID number: ')
    person = {}
    person['name'] = input('Enter name: ')
    person['age'] = input('Enter age: ')
    person['phone'] = input('Enter phone number: ')
    db[pid] = person


def lookup_person(db):
    """让用户输入ID和所需的字段，并从shelf对象中获取相应的数据"""
    pid = input('Enter ID number: ')
    field = input('What would you like to know? (name, age, phone) ')
    field = field.strip().lower()
    print(field.capitalize() + ':', db[pid][field])  # capitalize()返回字符串副本将第一个字母大写​


def print_help():
    print('The available commands are:')
    print('store : Stores information about a person')
    print('lookup : Looks up a person from ID number')
    print('quit : Save changes and exit')
    print('? : Prints this message')


def enter_command():
    cmd = input('Enter command (? for help): ')
    cmd = cmd.strip().lower()
    return cmd


def main():
    database = shelve.open('D:\database.db')  # 你可能想修改这个名称
    try:
        while True:
            cmd = enter_command()
            if cmd == 'store':
                store_person(database)
            elif cmd == 'lookup':
                lookup_person(database)
            elif cmd == '?':
                print_help()
            elif cmd == 'quit':
                return
    finally:
        database.close()
main()
