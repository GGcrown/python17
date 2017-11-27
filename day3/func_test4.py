# @Author  : Crown
# @Time    : 2017/11/20 14:22
# @File    : func_test4.py



# def test(x, y=0):
#     print("x",x)
#     print(y)
#
#
# test(y=100,x=0)

# 不定参数   参数组
# def test(a,*args):
#     print(a)
#     print(len(args))
#     print(args)
#(1,2,2,3,4,5)
# test
# test(*[1,2,2,3,4,5,1])


# **kwargs 把n个关键字参数，转换成字典方式
def test2(**kwargs):
    print(kwargs)
    print(kwargs['name'])


test2(name='alex', age=8, sex='F')
test2(**{"name": "alex", "age": 7})
