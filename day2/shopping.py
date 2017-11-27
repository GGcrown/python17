# Auhtor:Crown

product_list = [
    ('iPhoneX', 8800),
    ('Mac Pro', 9800),
    ('Bike', 800),
    ('Coffee', 30),
    ('Alex Python', 120)
]
shopping_list = []
salary = input("Please input your salary:")
if salary.isdigit():
    salary = int(salary)
    while True:
        # 枚举
        for index, item in enumerate(product_list, 1):
            # print(product_list.index(item),item)
            print(index, item)
        user_choice = input("choose want buy goods:")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product_list) and user_choice > 0:
                p_item = product_list[user_choice]
                if p_item[1] <= salary:  # 买得起
                    shopping_list.append(p_item)
                    print("salary:", salary, "----", p_item[1])
                    salary -= p_item[1]
                    print("Added %s into shopping cart , your current balanc is \033[31;1m%s\033[0m" % (p_item, salary))
                else:
                    print("\033[41;1m你的余额只剩[%s]啦，还买个毛线啊\033[0m" % (salary))
            else:
                print("pruduct is not exit")
        elif user_choice == "q":
            print("---------------------------")
            for p in shopping_list:
                print(p)
            print("Your current balance:", salary)
            print("---------------------------")
            exit()
else:
    print("you input is not digit!!!")
