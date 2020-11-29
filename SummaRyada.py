n = int(input())
s = 0
while n > 0:
    s = (1 / n ** 2) + s
    n = n - 1
    n = int(input())
print('{0:.4f}'.format(s))
