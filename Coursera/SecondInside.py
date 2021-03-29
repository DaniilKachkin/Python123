n = input()
first = n.find('f')
last = n.rfind('f')
second = n[(first + 1):]
if first != -1 and last != - 1:
    if first == last:
        print('-1')
    else:
        print(second.find('f') + first + 1)
else:
    print('-2')
