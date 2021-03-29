n = input()
first = n.find('h')
last = n.rfind('h')
print(n[0:first], n[(last + 1):], sep='')
