# @Time    : 2017/11/15 13:56
# @Author  : Crown
# @File    : file_op.py

# 读取文件
# 默认操作系统编码打开文件gbk
# w只写模式，新建文件
# r只读模式
# a append模式 追加模式 不可以读
# r+ 读写
# f = open("yesterday2", "r", encoding="utf-8")  # 文件句柄
# print(f)
# f.write("我爱北京天安门,\n")
# f.write("天安门上太阳升\n")


# f = open("yesterday", "r", encoding="utf-8")  # 文件句柄

# for i in range(5):
#     print(f.readline())

'''
# print(f.readlines())
#f.readlines()  一次全部读取----适合读小文件
for index, line in enumerate(f.readlines()):
    if index != 9:
        print(line.rstrip())
    else:
        print("-------我是分割线！-----")


for  index,line in enumerate(f):
    print(index,line.rstrip())
'''

# f = open("yesterday", "a", encoding="utf-8")  # 文件句柄
# print(f.tell())  # 打印当前的位置
# print(f.readline())
# print(f.tell())

# f.seek(0)#指定指针的位置
# print(f.readline())
# print(f.encoding)#编码格式
# print(f.isatty())#是否是终端设备  打印机。。。
# print(f.seekable())#判断是否可以seek移动
#
# print(f.flush())#强制刷新，清空内存
# f.seek(10)  # 移动没用
# print(f.truncate(11))#分割
# f.close()

#文件修改
#r+ 读写模式
#w+ 写读模式
#a+ 追加读
#wb rb二进制     网络传输必须使用二进制
# f = open("yesterday", "r+", encoding="utf-8")  # 文件句柄
# f = open("yesterday", "w+", encoding="utf-8")  # 文件句柄
# f = open("yesterday", "a+", encoding="utf-8")  # 文件句柄
f = open("yesterday", "wb")  # 二进制
f.write("hello biery".encode())
# f.write("diao1\n".center(50,"-"))
# f.write("diao2\n".center(50,"-"))
# f.write("diao3\n".center(50,"-"))
# f.write("diao4\n".center(50,"-"))
# print(f.tell())
# f.seek(10)
# print(f.tell())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# f.write("Should be at the beging secound line")
f.close()

