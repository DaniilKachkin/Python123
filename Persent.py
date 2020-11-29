p = float(input())
x = float(input())
y = float(input())
m = (x / 100 * p + x) + ((y / 100 * p + y) // 1) / 100
print('{0:.0f}'.format(m // 1), '{0:.0f}'.format(m % 1 * 100))
