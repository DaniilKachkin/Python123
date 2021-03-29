n = input()
first = n.find('h')
last = n.rfind('h')
print(n[0:last], n[(first + 1):], sep='')
