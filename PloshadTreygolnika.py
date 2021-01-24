a = float(input())
b = float(input())
c = float(input())
p = (a + b + c) * 0.5
S = pow(p * (p - a) * (p - b) * (p - c), 0.5)
print(S)
