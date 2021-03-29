def IsPointInSquare(x, y):
    s = x ** 2 + y ** 2
    return s <= 2


x = float(input())
y = float(input())
if IsPointInSquare(x, y):
    print('YES')
else:
    print('NO')
