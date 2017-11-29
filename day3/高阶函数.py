# @Author  : Crown
# @Time    : 2017/11/28 8:35
# @File    : 高阶函数.py

#把函数当成参数传入

def add(a, b, f):
    return f(a) + f(b)

res = add(-222, -333, abs)
print(res)
