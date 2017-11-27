# @Time    : 2017/11/15 11:19
# @Author  : Crown
# @File    : gather.py

# 集合    无序的
list_1 = [1, 2, 3, 6, 7, 8, 9]
print(type(list_1))
list_1 = set(list_1)
print(list_1, type(list_1))

list_2 = set([2, 5, 6, 3, 8, 9])
print(list_2)
# 交集
print(list_1.intersection(list_2))
# 并集
print(list_1.union(list_2))
# 差集 in list_1 but not in list_2
print("差集:", list_1.difference(list_2))
print("差集:", list_2.difference(list_1))

list_3 = set([1, 2, 3])
# 子集 if list_1 include list_2 all items return True else return False
print(list_2.issubset(list_1))
print(list_3.issubset(list_1))
# 父集
print(list_2.issuperset(list_1))
print(list_1.issuperset(list_3))

# 对称差集      互相没交集的取出来
print(list_1.symmetric_difference(list_2))

print("-------------------")
list_4 = set([1, 5, 6, 7])
""" Return True if two sets have a null intersection. """
print(list_3.isdisjoint(list_4))  # 判断是否有交集

# 交集
print(list_1 & list_2)
# union 并集
print(list_1 | list_2)
# difference 差集
print(list_1 - list_2)  # in list_1 but not in list_2
# 对称差集
print(list_1 ^ list_2)  # Return True if two sets have a null intersection.

#添加
list_1.add(123)
print(list_1)
#添加多个
list_1.update([99,66,11,33])
print(list_1)
#删除
# list_1.remove(1)
# list_1.discard(1)
#判断是否在这个里面  集合 字典 列表都是这样写
print(1 in list_1)
print(list_1)










