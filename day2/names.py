# Auhtor:Crown
'''
# names="ZhangYang GuYun XiangPeng XuLiangchen"
names = ["ZhangYang", "GuYun", "XiangPeng", "XuLiangchen", "YeLiangchen"]
names.append("LeiHaidong")#追加
names.insert(1,"ChenRonghua")#插入指定位置
names.append("XinZhiyu")#插入指定位置
names[2]="XieDi"#修改
names[2]="XieDi"#修改
# names.remove("ChenRonghua")#删除
# names.remove(1)#删除
names.pop(0)#默认删除最后一个
print(names)

# print(names[0], names[1])
# print(names[1:3])  # 切片 前包后不包，顾头不顾尾
# print(names[-1])  # -1 倒着数第一个值
# print(names[-3:-1])#从左往右数  从小到大
# print(names[-2:])#从左往右数  从小到大
# print(names[0:3])
# print(names[:3])  # 0可以忽略


print(names[names.index("XieDi")])
print(names.count("XieDi"))


# names.reverse();#反转
# names.clear()#清空
names.sort()#排序 编码排序
print(names)


names2=[1,2,3,4]
names.extend(names2)

# del names
print(names,names2)'''

'''import copy
studen = ["ZhangYang", "GuYun", "XiangPeng", ["alex", "jack"], "XuLiangchen", "YeLiangchen"]
# studen2 = studen.copy()  # 潜copy 只拷贝第一层
studen2 = copy.deepcopy(studen)  # 深copy 只拷贝第一层
print(studen)
print(studen2)
studen[2] = "象鹏"
studen[3][0] = "ALEX"
print(studen)
print(studen2)'''

people = ["ZhangYang", "GuYun", "XiangPeng", ["alex", "jack"], "XuLiangchen", "YeLiangchen"]
for i in people:
    print(i)

#range(0,10,2)
print(people[0:-1:2])#0和-1可以省略
print(people[::2])
print(people[:])