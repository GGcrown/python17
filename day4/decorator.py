# @Author  : Crown
# @Time    : 2017/11/29 12:39
# @File    : decorator.py

# 修饰器
import time


def timmer(func):
    def warpper(*args, **kawargs):
        start_time = time.time()
        func()
        stop_time = time.time()
        print('the func run time is %s' % (stop_time - start_time))

    return warpper


@timmer
def test1():
    time.sleep(3)
    print('in hte test1')


test1()
