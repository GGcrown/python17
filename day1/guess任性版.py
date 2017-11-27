# Auhtor:crown

# age_of_oldboy = 56
# count = 0
# while count < 3:
#     guess_age = int(input('guess age:'))
#     if age_of_oldboy == guess_age:
#         print("yes,you got it")
#         break
#     elif age_of_oldboy > guess_age:
#         print("think bigger")
#     else:
#         print('think smaller')
#     count += 1
#     if count == 3:
#         continue_confirm = input("Do you want gussing?")
#         if continue_confirm != "n":
#             count = 0

#
# for i in range(0,10):
#     if i<5:
#         print("loop",i)
#     else:
#         continue
# print("hehe..")

for i in range(10):
    print("-------------", i)
    for j in range(10):
        print(j)
        if j>5:
            break
