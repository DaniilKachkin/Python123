n = input()
s = len(n)
z = 0
m = n[0]
if s == 1:
    print(n)
else:
    while s != 1:
        s = s - 1
        m = n[z]
        z = z + 1
        print(m, end='*')
    print(n[-1], end='')
