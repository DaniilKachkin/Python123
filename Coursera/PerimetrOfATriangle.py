from math import sqrt


def distance(x1, y1, x2, y2, x3, y3):
    dist1 = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    dist2 = sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
    dist3 = sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
    sum = dist1 + dist2 + dist3
    return sum


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
print(distance(x1, y1, x2, y2, x3, y3))
