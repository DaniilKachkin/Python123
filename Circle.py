def IsPointInCircle(x, y, xc, yc, r):
    s = (x - xc) ** 2 + (y - yc) ** 2
    return s <= r ** 2


x = float(input())
y = float(input())
xc = float(input())
yc = float(input())
r = float(input())
if IsPointInCircle(x, y, xc, yc, r):
    print('YES')
else:
    print('NO')
