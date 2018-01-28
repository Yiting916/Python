st = 'this is an apple'
sp = st.split()
for i in range(len(sp)):
    sp[i] = sp[i].capitalize()
ans = ''.join(sp)
print(sp)

#' '.join([i.capitalize() for i in st.split()])     #生成式
#print(sp)
