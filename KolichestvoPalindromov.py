n = int(input())
m = 0 # Палиндром
z = n
i = 0 # искомый порядковый номер
while n > 0:
    while z > 0:
        m = m * 10 + z % 10
        z = z // 10
    if m == n:
        i = i + 1
    m = 0
    z = n
    n = n - 1
print(i)
