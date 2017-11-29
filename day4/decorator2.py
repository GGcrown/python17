# @Author  : Crown
# @Time    : 2017/11/29 12:58
# @File    : decorator2.py

# 函数即变量

import time


# 实现了装饰器的功能，但违反了装饰器的原则
# def foo():
#     time.sleep(3)
#     print('in the foo')
#
#
# def test1(func):
#     start_time=time.time()
#     print("start")
#     func()
#     end_time=time.time()
#     print("end")
#     print(end_time-start_time)
#
# test1(foo)
# # foo()



def foo():
    time.sleep(3)
    print('in the foo')

def test2(fuc):
    print(fuc)
    return fuc

# print(test2(foo))
test2(foo)()



