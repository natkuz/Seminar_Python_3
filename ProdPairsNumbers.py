# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import random

my_list = []
n = int(input('Enter size of list: '))

for _ in range(n):
    my_list.append(random.randint(1, 10))

print(f'Generated list: {my_list}')

prod_my_list = []

if len(my_list) % 2 == 0:
    i = 0
    while i < len(my_list) / 2:
        prod_my_list.append(my_list[i] * my_list[len(my_list) - i - 1])
        i += 1
else:
    i = 0
    while i <= len(my_list) / 2:
        prod_my_list.append(my_list[i] * my_list[len(my_list) - i - 1])
        i += 1

print(f'The roducts of pairs numbers of generated list: {prod_my_list}')
