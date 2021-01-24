from math import sqrt

a = float(input())
b = float(input())
c = float(input())
D = b ** 2 - 4 * a * c
if D > 0:
    x1 = (- b + sqrt(D)) / (2 * a)
    x2 = (- b - sqrt(D)) / (2 * a)
    if a < 0:
        print('{0:.6f}'.format(x1), '{0:.6f}'.format(x2))
    if a > 0:
        print('{0:.6f}'.format(x2), '{0:.6f}'.format(x1))
elif D == 0:
    x = - b / (2 * a)
    if x != 0:
        print('{0:.6f}'.format(x))
    if x == - 0:
        print(0)
else:
    print('')
