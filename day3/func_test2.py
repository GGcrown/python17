# @Author  : Crown
# @Time    : 2017/11/17 9:11
# @File    : func_test2.py
import time


def logger():
    time_formate = "%Y-%m-%d %X"
    time_current = time.strftime(time_formate)
    with open("a.txt", "a") as f:
        f.write("%s end action\n" % time_current)
        f.close()


def test1():
    print("in the test1")
    logger()


def test2():
    print("in the test2")
    logger()


def test3():
    print("in the test3")
    logger()


test1()
test2()
test3()
