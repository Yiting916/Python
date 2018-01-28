st = []
n= eval(input())
for i in range(n, 0, -1):
    print('data',i)
    st.append(i)
print('')
for j in range(len(st)):
    print('data', st.pop())
