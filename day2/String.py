# Auhtor:Crown


name = "my name is {name} and i am {year} old"
print(name.capitalize())  # 首字母大写
print(name.count("a"))  # 统计a的个数
print(name.center(50, "-"))  # -----------------------alex-----------------------
print(name.endswith("e"))  # 判断结尾是否存在
print(name.expandtabs(30))  # ale\t
print(name.find("e"))
print(name[name.find("name"):])  # String也能切片
print(name.format(name="alex", year=33))
print(name.format_map({"name": "alex", "year": 12}))  # 字典
print(name.index("is"))  # 索引
print("1213".isalnum())  # 是阿拉伯数字
print("fafafa".isalpha())  # 判断是否是纯英文字母
print("1121.0".isdecimal())  # 判断十进制
print("111".isdigit())  # 判断是整数
print("_df".isidentifier())  # 判断是不是一个合法的标识符
print("0x33".isnumeric())  # 判断是只有数字
print("    ".isspace())  # 是不是空格
print("My Name Is".istitle())  # 是不是标题 每个单词首字母大写
print("My Name Is".isprintable())  # 是不是可打印的
print("SSFDSFSDF".isupper())  # 是不是大写
print('+'.join(["1", "2", "3", "4"]))  # 是不是大写1+2+3+4连接
print('+'.join("1234"))  # 是不是大写
print(name.ljust(50, '*'))  # my name is {name} and i am {year} old*************
print(name.rjust(50, '*'))  # *************my name is {name} and i am {year} old
print("I am sss".lower())  # 大写转小写
print("I am sss".upper())  # 小写转大写
print("\n  I am sss\n".lstrip())  # 去掉左边空格回车
print("----")
print("\n  I am sss\n".rstrip())  # 去掉右边空格回车
print("----")
print("\n  I am sss\n".strip())  # 去掉两边空格回车
print("----")
p = str.maketrans("abcdef123456", "123456abcdef")  # 自定义翻译
translate = "alex li".translate(p)
print(translate)  # 1l5x li
p2 = str.maketrans("123456", "abcdef")
untraslate = translate.translate(p)  # 反向翻译
print(untraslate)
print("allllex".replace('l', 'L', 1))  # 替换
print("allllex".rfind('e'))  # 找到最右边的下标
print("a ll l l ex".split("l"))  # 自动按变成列表
print("a ll l l\nex".splitlines())  # 可以按换行变成列表
print("Allllex".swapcase())  #大小写互相切换
print("Alex li".title())
print("Alex li".zfill(50))#自动补位用0填充


