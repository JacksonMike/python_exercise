import random

lottery = random.randint(100, 1000)
guess = eval(input("Enter your lottery pick(three digits):"))

a = list()
lottery_digit1 = lottery // 100
lottery_digit2 = lottery % 100 // 10
lottery_digit3 = lottery % 10
a.append(lottery_digit1)
a.append(lottery_digit2)
a.append(lottery_digit3)

b = list()
guess_digit1 = guess // 100
guess_digit2 = guess % 100 // 10
guess_digit3 = guess % 10
b.append(guess_digit1)
b.append(guess_digit2)
b.append(guess_digit3)


def common_data(a, b):
    result = False
    for x in a:
        for y in b:
            if x == y:
                result = True
    return result


print("The lottery number is", lottery)
if guess == lottery:
    print("Exact match: you win $10,000")
elif a == b:
    print("Match all digits: you win $3,000")
elif common_data(a, b):
    print("Match one digit: you win $1,000")
else:
    print("Sorry, no match")
