# @Author  : Crown
# @Time    : 2017/11/17 8:54
# @File    : func_test1.py


#定义一个函数
def func1():
    """testing1"""
    print("in the func1")
    return 0

#过程 过程就是没有返回值的函数
def func2():
    """testing2"""
    print("in the func2")


x=func1()
y=func2()
print(x,y)