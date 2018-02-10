f1 = open('./stores_old.csv','r', encoding='big5')
lst1 = f1.readlines()
f1.close()

for i in range(len(lst1)):
    lst1[i] = lst1[i].split(',')

    if lst1[i][6] == 'Y':
        for j in range(len(lst1[i])):
            print(lst1[i][j]+',', end='')
    

