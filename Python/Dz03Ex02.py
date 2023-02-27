# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в
# первой строке вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N целых
# чисел Ai. Последняя строка содержит число X. Пример:
# 5
# 1 2 3 4 5
# 6
# -> 5

long = int(input('Введите количество элементов массива: '))
mass = []

for _ in range(long):
    num = int(input('Введите элемент, целое число: '))
    mass.append(int(num))

print(f'Ваш массив: {mass}')
x = int(input('Введите искомое целое число: '))

count = 0
for i in mass:
    if i == x:
        count += 1
print(f'Заданное число встречается в массиве {count} раз(а)')

ost = []
for i in mass:
    if i > x:
        ost.append(int(i - x))
    if x > i:
        ost.append(int(x - i))

print(f'Ваш массив ост: {ost}')

min = ost[0]
print(f'мин: {min}')
count = 0
position = -1

g = 0
for g in ost:
    if min == g:
        count = count + 1
        position = ost.index(g, end)
        print(f'позиция: {position}')
    if g < min:
        min = g
        count = 1
        position = ost.index(g, start)
        print(f'позиция: {position}')

print(f'Приближенное числа: {mass[position]}, встречается {count} раз(а)')