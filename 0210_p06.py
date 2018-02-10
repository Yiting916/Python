f1 = open('../app/stores_old.csv','r', encoding='big5')
lst = f1.readlines()
f1.close()

stable = (0, 3, 5, 6)
for i in range(len(lst)):
    lst[i] = lst[i].split(',')
    for j in stable:
        print(lst[i][j]+',', end='')
    print()
