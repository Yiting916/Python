import random
guess = random.randint(1,5)
print(guess)
keyin = eval(input('請猜一1到5的號碼:'))

if guess == keyin:
    print('你猜對了! 答案正是', guess)
else:
    print('你猜錯了喔~ 答案其實是', guess)
