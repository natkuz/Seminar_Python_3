# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

my_list = []
n = int(input('Enter size of list: '))

for _ in range(n):
    my_list.append(random.randint(1, 20))

print(my_list)
sum = 0

for i in range(len(my_list)):
    if i % 2 != 0:
        sum += my_list[i]
    else:
        i += 1

print(f'The sum of elements with odd indices = {sum}')