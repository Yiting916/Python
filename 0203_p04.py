def return2num(n):
    sum1 = 0
    total = 1
    for i in range(1, n+1):
        total *= i
        sum1 += i
    return total, sum1

x = eval(input())
a,b = return2num(x)
print(a)
print(b)

