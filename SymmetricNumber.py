n = int(input())
m = 0
v = n
while n > 0:
    m = m * 10 + n % 10
    n = n // 10
if v / 100 < 1:
    print(v)
elif m // 100 - m % 100 == 0:
    print('1')
elif m - v == 0:
    print('1')
else:
    print(m)
