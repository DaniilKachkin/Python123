def min4(a, b, c, d):
    one = min(a, b)
    two = min(c, d)
    last = min(one, two)
    return last


a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(min4(a, b, c, d))
