# -*- coding:gbk -*-
# @Author  : Crown
# @Time    : 2017/11/16 11:06
# @File    : encode.py


s = "同一个世界，同一个梦想"

print(s)
print(s.encode().decode("gbk"))
print(s.encode())  # 转码变成byte类型
