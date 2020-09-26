n = int(input())        #   порядковый номер числа
f =                   #   искомое число
i =                 # предыдущее число
m = 2                # первое число
while n > 1:
    f =             # здесь должен быть норм код
    n = n - 1
print(f)


n = int(input())

f0 = 0
f1 = 1

if n < 0:
    print('Error, n must be greater then 0')
elif n == 0:
    print('Fibonacci is {f}'.format(f=f0))
elif n == 1:
    print('Fibonacci is {f}'.format(f=f1))
else:
    f_prev_prev = f0
    f_prev = f1
    f_result = 0
    while n > 1:
        f_result = f_prev + f_prev_prev
        f_prev_prev = f_prev
        f_prev = f_result
        n = n - 1

    print('Fibonacci is {f}'.format(f=f_result))
