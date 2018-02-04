def avg(lst):
    num = sum(lst)/len(lst)
    return num

score = []
# 輸入5位學生的三科成績
for i in range(5):
    n = [eval(i) for i in input().split()]
    score.append(n)

sum1 = []
avg1 = []
for i in range(len(score)):
    print('student', i+1)
    for j in range(len(score[i])):
        print(' %d: %d'%(j+1, score[i][j]))

        sum1.append(score[i][j])
  
    print(' sum: %d'%(sum(score[i])))
    print(' avg: %.2f'%(avg(score[i])))

    avg1.append(avg(score[i]))  

maxAvg = avg1.index(max(avg1))

print('total: %d, avg: %.2f'%(sum(sum1), avg(sum1)))
print('highest avg: student %d: %.2f'%(maxAvg+1, max(avg1)))


