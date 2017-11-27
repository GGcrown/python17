# @Author  : Crown
# @Time    : 2017/11/27 17:42
# @File    : func_test5.py

# 默认的参数
# 默认参数的特点：调用函数的时候，默认参数非必传

def test(x, y=2):
    print(x)
    print(y)

test(1)
