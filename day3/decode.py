# -*- coding:gbk -*-
# @Author  : Crown
# @Time    : 2017/11/16 11:06
# @File    : encode.py


s = "ͬһ�����磬ͬһ������"

print(s)
print(s.encode().decode("gbk"))
print(s.encode())  # ת����byte����
