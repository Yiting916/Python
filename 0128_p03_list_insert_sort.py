st = []

while True:
    n= eval(input())
    if n == -1:
        break
    st.append(n)

st.sort()
print(st)
st.insert(3, 10)
print(st)
print(st.count(10))
st.sort()
st.reverse()
print(st)

