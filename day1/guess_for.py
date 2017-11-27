# Auhtor:crown

age_of_oldboy = 56

for i in range(3):
    guess_age = int(input('guess age:'))
    if age_of_oldboy == guess_age:
        print("yes,you got it")
        break
    elif age_of_oldboy > guess_age:
        print("think bigger")
    else:
        print('think smaller')
else:
    print("you have tried too many times.fuck off")
