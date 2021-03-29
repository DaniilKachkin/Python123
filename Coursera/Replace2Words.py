n = input()
first = n.find(' ')
last = n.rfind(' ')
print(n[last + 1:], n[0:first + 1])
