# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

number = int(input('Enter number to convert to binary: '))
decimal_number = number
bin_list = []

while number > 0:
    bin_digit = number - int(number / 2) * 2
    bin_list.append(bin_digit)
    number = int(number / 2)

i = 0

while i < len(bin_list) / 2:
    temp = bin_list[i]
    bin_list[i] = bin_list[len(bin_list) - i - 1]
    bin_list[len(bin_list) - i - 1] = temp
    i +=1

bin_number = str()

for item in bin_list:
    bin_number = bin_number + str(item)

print(f'decimal number {decimal_number} in binary = {bin_number}')