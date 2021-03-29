n = input()
s = len(n)
z = 0
m = n[0]
while s != 1:
    s = s - 1
    z = z + 1
    if z % 3 == 0:
        continue
    m = n[z]
    print(m, end='')
