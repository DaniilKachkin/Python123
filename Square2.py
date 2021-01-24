def IsPointInSquare(x, y):
    s = abs(x) + abs(y)
    return 0 <= s <= 1


x = float(input())
y = float(input())
if IsPointInSquare(x, y):
    print('YES')
else:
    print('NO')
