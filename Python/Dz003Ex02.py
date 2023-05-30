# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в
# первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел
# Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

long = int(input('Введите количество элементов массива: '))
mass = []

from random import randint

for _ in range(long):
    num = randint(-15, 15)
    mass.append(int(num))

print(f'Ваш массив: {mass}')
numSearch = int(input('Введите искомое целое число: '))

count = 0
for i in mass:
    if i == numSearch:
        count += 1
print(f'Заданное число встречается в массиве {count} раз(а)')

ost = []
for j in mass:
    if j > numSearch:
        ost.append(int(j - numSearch))
    if numSearch > j:
        ost.append(int(numSearch - j))
    if numSearch == j:
        ost.append(int(numSearch - j))

print(f'Массив остатков: {ost}')

min = ost[0]
# print(f'мин: {min}')
for i in range(len(ost)):
    if ost[i] < min:
        min = ost[i]
print(f'мин: {min}')

for i in range(len(ost)):
    if ost[i] == min:
        print(f'Cамый близкий по величине к {numSearch} элемент: {mass[i]}')