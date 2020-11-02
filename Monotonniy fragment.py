n = int(input())
m = n
i = 0
a = 0
while n != 0:
    if n > m:
        i = i + 1
    elif n < m:
        a = a + 1
    m = n
    n = int(input())
if i > a:
    print(i)
else:
    print(a + 1)
