n = int(input())
m = n
i = 0
a = 0
while n != 0:
    if n == m:
        i = i + 1
    else:
        if i > a:
            a = i
        i = 1
    m = n
    n = int(input())
print(a)
