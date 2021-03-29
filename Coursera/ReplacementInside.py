n = input()
first = n.find('h')
last = n.rfind('h')
middle = n[first + 1:last]
print(n[:first + 1], middle.replace('h', 'H'), n[last:], sep='')
