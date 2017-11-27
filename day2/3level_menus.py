# @Time    : 2017/11/15 9:16
# @Author  : Crown
# @File    : 3level_menus.py

data = {
    '北京': {
        "昌平": {
            "沙河": ["oldboy", "test"],
            "天通苑": ["链家地产", "我爱我家"]
        },
        "朝阳": {
            "望京": ["奔驰", "陌陌"],
            "国贸": ["CICC", "HP"],
            "东直门": ["Advent", "飞信"],
        },
        "海淀": {},
    },
    '山东': {
        "德州": {},
        "青岛": {},
        "济南": {}
    },
    '广东': {
        "东莞": {},
        "常熟": {},
        "佛山": {},
    },
}

exit_flag = False

while not exit_flag:
    for i in data:
        print(i)
    choice = input("选择进入1>>:")
    if choice in data:
        while not exit_flag:
            for j in data[choice]:
                print("\t", j)
            choice2 = input("选择进入2>>：")
            if choice2 in data[choice]:
                while not exit_flag:
                    for k in data[choice][choice2]:
                        print("\t\t", k)
                    choice3 = input("选择进入3>>：")
                    if choice3 in data[choice][choice2]:
                        for l in data[choice][choice2][choice3]:
                            print("\t\t\t", l)
                        choice4 = input("是否继续，按b返回>>：")
                        if choice4 == 'b':
                            pass  # 什么也不做
                        elif choice4=='q':
                            exit_flag=True
                    if choice3 == 'b':
                        break
                    elif choice3 == 'q':
                        exit_flag = True
            if choice2 == 'b':
                break
            elif choice2 == 'q':
                exit_flag = True
    if choice=='q':
        exit_flag=True


print("恭喜退出 ")