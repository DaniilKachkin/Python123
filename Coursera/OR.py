def xor(x, y):
    s = x + y
    return s == 1


x = float(input())
y = float(input())
if xor(x, y):
    print('1')
else:
    print('0')
