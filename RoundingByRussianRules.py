n = float(input())
if n % 1 * 10 < 5:
    print('{0:.0f}'.format(n // 1))
else:
    print('{0:.0f}'.format((n + 1) // 1))
