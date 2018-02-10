f1 = open('./stores_old.csv','r', encoding='big5')
lst1 = f1.readlines()
f1.close()

f2 = open('./stores_new.csv', 'w', encoding='utf-8')
stable = (0, 3, 5, 6)
for i in range(len(lst1)):
    lst1[i] = lst1[i].split(',')
    for j in stable:
        f2.write(lst1[i][j]+',')
        #print(lst1[i][j]+',', end='')
    f2.write('\n')
    #print()

f2.close()

