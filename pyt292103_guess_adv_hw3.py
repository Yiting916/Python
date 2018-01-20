import random

Max = 100
Min = 1
ct = 0
ans = random.randint(1, 100)
keyin = 0

print('答案：', ans)
print('猜1~100之間的一數字:')
while True:
    keyin = eval(input())
    ct += 1
    if Min < keyin < Max:
        if keyin > ans:
            Max = keyin
            print('再小一點: 答案< ', keyin)
            print('已猜次數:', ct)

        elif keyin < ans:
            Min = keyin
            print('再大一點: 答案> ', keyin)
            print('已猜次數:', ct)

        else:
            print('猜對了, 答案是: ', ans)
            print('已猜次數:', ct)
            break
        
    else:
        print('超出範圍,', Min, '<答案<,', Max, ',請重新輸入數字:')
        print('已猜次數:', ct)
