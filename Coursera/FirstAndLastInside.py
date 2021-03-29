n = input()
first = n.find('f')
last = n.rfind('f')
if first != -1 and last != - 1:
    if first == last:
        print(first)
    else:
        print(first, last)
