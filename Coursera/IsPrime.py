from math import sqrt

n = int(input())


def IsPrime(n):
    k = 2
    if n == 2:
        return n
    while n % k != 0:
        k += 1
        if k > sqrt(n):
            return n
    return 0


if IsPrime(n):
    print('YES')
else:
    print('NO')

