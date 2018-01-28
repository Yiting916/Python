Keys = 'P', 'M', 'H'
values = 'Pikachu', 'Mickey Mouse', 'Hello kitty'
dc = dict(zip(Keys, values))


while True:
    qkey = input()
    if qkey == '-1':
        break
    elif qkey == '-2':
        print(dc)
    else:
        if qkey not in dc:
            
            print(qkey,'does not exist. Enter a new one:')
            dc[qkey] = input()
        else:
            print(dc[qkey])        


