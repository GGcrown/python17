# @Time    : 2017/11/14 19:14
# @Author  : Crown
# @File    : dictionary.py

# 字典  key-value 无序
'''
info = {
    'stu1101': "Tenglan Wu",
    'stu1102': "Luola LongZe",
    'stu1103': "Maliya Xiaoze"
}
print(info)
# print(info['stu1101'])
info['stu1101']="武藤兰"#如果存在key就修改，不存在添加
# info['stu1104']="苍老师"
#删除
# del info["stu1101"]
# info.pop("stu1101")
# info.popitem()#随机删除

print(info.get('stu11011'))
print('stu11033' in info)#判断是否存在
print(info)

av_catalog = {
    "欧美": {
        "www.youporn.com": ["很多免费的,世界最大的", "质量一般"],
        "www.pornhub.com": ["很多免费的,也很大", "质量比yourporn高点"],
        "letmedothistoyou.com": ["多是自拍,高质量图片很多", "资源不多,更新慢"],
        "x-art.com": ["质量很高,真的很高", "全部收费,屌比请绕过"]
    },
    "日韩": {
        "tokyo-hot": ["质量怎样不清楚,个人已经不喜欢日韩范了", "听说是收费的"]
    },
    "大陆": {
        "1024": ["全部免费,真好,好人一生平安", "服务器在国外,慢"]
    }
}
av_catalog["大陆"]["1024"][1]="可以在国内做镜像"
#key尽量别写中文
print(av_catalog)
# print(av_catalog.values())
# print(av_catalog["大陆"].keys())
av_catalog.setdefault("taiwan",{"www.baidu.com":[1,2]})
av_catalog.setdefault("大陆",{"www.baidu.com":[1,2]})
 print(av_catalog)

info = {
    'stu1101': "Tenglan Wu",
    'stu1102': "Luola LongZe",
    'stu1103': "Maliya Xiaoze"
}
b = {
    'stu1101': "Alex",
    1: 3,
    2: 2
}

# c = dict.fromkeys([6, 7, 8], "test")  # 初始化一个字典
# print(c)
d = dict.fromkeys([6, 7, 8], [1, {'name': 'alex'}, 444])  # 共享一个内存，一变全变
print(d)
d[7][1]['name'] = 'Jack Cheng'
print(d)
# print(c)
# info.update(b)  # 字典合并，
# print(info)
# print(info.items())  # 字典转列表'''

info = {
    'stu1101': "Tenglan Wu",
    'stu1102': "Luola LongZe",
    'stu1103': "Maliya Xiaoze"
}
for i in info:#最基本的循环 比下面的高效
    print(i,info[i])

for k,v in info.items():
    print(k,v)


