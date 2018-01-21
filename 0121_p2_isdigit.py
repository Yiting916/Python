s1 = ''

while True:
    s1 = input()
    if s1.isdigit():
        print('n=%s'%(s1))
        break
    else:
        print('is not a number')
