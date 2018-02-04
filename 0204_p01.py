def inputList(lst):
    while True:
        n = eval(input())
        if n == -1:
            break
        lst.append(n)
        
def max3(lst):
    lst.sort()
    print('sorted =', lst)
    return lst[-3]

data = []
inputList(data)
print('input =', data)
print('max 3rd =', max3(data.copy()))
print('list =', data)
