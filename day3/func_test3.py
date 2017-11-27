# @Author  : Crown
# @Time    : 2017/11/20 14:16
# @File    : func_test3.py

def test1():
    print('in the test1')

def test2():
    print('in the test2')

def test3():
    print('in the test3')
    return test2()
def fff():
    pass

x=test3()

# print(x)
