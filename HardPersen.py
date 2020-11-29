p = float(input())
x = float(input())
y = float(input())
k = float(input())
if k == 0:
    print('{0:.0f}'.format(x), '{0:.0f}'.format(y))
elif k > 0:
    k = k - 1
    m = x + y / 100
    z = (m / 100 * p + m)
    b = z // 1
    v = (z * 100 - z // 1 * 100) // 1 / 100
    i = b + v
    while k != 0:
        if k < 1:
            break
        z = (z / 100 * p + z)
        b = z // 1
        v = (z * 100 - z // 1 * 100) // 1 / 100
        z = b + v
        k = k - 1
    print('{0:.0f}'.format(z // 1), '{0:.0f}'.format(z % 1 * 100))
