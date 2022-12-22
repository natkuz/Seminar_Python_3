# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

my_list = []

n = int(input('Enter size of list: '))

for _ in range(n):
    my_list.append(round(random.uniform(1, 10), 2))

print(f'Generated list: {my_list}')

for i in range(len(my_list)):
    my_list[i] = int(my_list[i] * 100 % 100)

max_el = my_list[0]
i = 0
for i in range(len(my_list)):
    if my_list[i] > max_el:
        max_el = my_list[i]
    i += 1

min_el = my_list[0]
i = 0
for i in range(len(my_list)):
    if my_list[i] < min_el and my_list[i] != 0:
        min_el = my_list[i]
    i += 1

print(f'Difference between max and min value of the fractional part of the elements other than 0 = {(max_el - min_el) / 100}')