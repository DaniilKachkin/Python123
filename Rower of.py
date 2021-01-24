a = float(input())
n = int(input())


def power(a, n):
    if n == 0:
        return 1
    elif n > 0:
        return a * power(a, n - 1)
    else:
        return power(a, n + 1) / a


print(power(a, n))
