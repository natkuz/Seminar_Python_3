# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

# for k > 0: f(k) = f(k-1)+f(k-2)
# for k < 0: if k is even: f(-k)=f(abs(k))*-1 or if k is odd: f(-k)=f(abs(k))

k = int (input('Enter number: '))
fib_list = []

def Fib(k):
    fib1 = 1
    fib2 = 1
    i = 2
    while i < k:
        temp = fib1 + fib2
        fib1 = fib2
        fib2 = temp
        i += 1
    return fib2

for i in range(-k, k + 1):
    if i < 0:
        if i % 2 == 0:
            fib = Fib(abs(i)) * (-1)
        else:
            fib = Fib(abs(i))
    elif i > 0:
        fib = Fib(i)
    else:
        fib = 0
    fib_list.append(fib)

print(fib_list)

