# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите
# минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
# 5 -> 1 0 1 1 0
# 2

n = int(input('Введите число монеток, лежащих на столе: '))

heads = 0
tails = 0
for _ in range(n):
    coin = int(input('Какой стороной лежит монетка? 1 - орёл, 2 -решка : '))
    if coin == 1:
        heads += 1
    if coin == 2:
        tails += 1

if heads > tails:
    print(f'Количество монет, которые нужно перевернуть, чтобы все стали орлами: {tails}')
elif heads < tails:
    print(f'Количество монет, которые нужно перевернуть, чтобы все стали решками: {heads}')
else:
    print(f'Количество орлов и решек одинаковое, нужно перевернуть: {heads}')