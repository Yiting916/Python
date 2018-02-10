f = open('../app/sim.txt','r', encoding='gb2312')
for line in f.readlines():
    line = line.strip()
    print(line)
f.close()
