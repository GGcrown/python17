# @Author  : Crown
# @Time    : 2017/11/27 18:05
# @File    : localVariable.py



# 局部变量只在函数中起作用
def change_name(name):
    print("before change", name)
    # 这个函数就是这个变量的作用域
    name = "Alex"
    print("after change", name)




name = "Corwn"
change_name(name)
print("name:" + name)
