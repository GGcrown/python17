# Auhtor:Crown


username = input("name:")  # raw_input() 2.x    input() 3.x
age = int(input("age:"))  # input 2.x不好用
print(type(age))
info = '''
---------info of %s------------
Name：%s
Age:%d
''' % (username, username, age)

print(info)

info2 = '''
---------info2 of {_name}------------
Name：{_name}
Age:{_age}
'''.format(_name=username, _age=age)

print(info2)

info3='''
---------info3 of {0}------------
Name：{0}
Age:{1}
'''.format(username,age)

print(info3)