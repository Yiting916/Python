def avg(lst):
    num = sum(lst)/len(lst)
    return num

score = [[76,73,85], [88,84,76],[92,82,92],[82,91,85],[72,74,73]]

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

