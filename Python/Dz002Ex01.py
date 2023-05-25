# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное
# число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите
# минимальное количество монет, которые нужно перевернуть.

coinS = int(input('Введите число монеток, лежащих на столе: '))

heads = 0
tails = 0

from random import randint

for _ in range(coinS):
    coin = randint(1, 2)
    if coin == 1:
        heads += 1
    if coin == 2:
        tails += 1

print(f'Количество орлов: {heads}')
print(f'Количество решек: {tails}')

if heads > tails:
    print(f'Количество монет, которые нужно перевернуть, чтобы все стали орлами: {tails}')
elif heads < tails:
    print(f'Количество монет, которые нужно перевернуть, чтобы все стали решками: {heads}')
else:
    print(f'Количество орлов и решек одинаковое, нужно перевернуть: {heads}')

# Пример идеального решения
#
# Задача 10
#
# n = int(input())
# count_zero = 0
# count_one = 0
# for i in range(n):
# x = int(input())
# if x == 0:
# count_zero += 1
# else:
# count_one += 1
# if count_one > count_zero:
# print(count_zero)
# else:
# print(count_one)

