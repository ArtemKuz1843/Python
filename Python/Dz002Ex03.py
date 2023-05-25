# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

num = int(input('Введите число: '))
count = 0
number = 2 ** count

print('Целые степени числа 2 не превышающие вашего числа: ')
while num >= number:
    print(f'{number} - это 2 в степени {count}')
    count += 1
    number = 2 ** count

# Пример идеального решения
#
# Задача
# 14
#
# n = int(input())
# i = 0
# while 2 ** i <= n:
#     print(2 ** i)
#     i += 1

