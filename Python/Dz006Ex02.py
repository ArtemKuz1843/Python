# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]  Вывод: [1, 9, 13, 14, 19]

long = int(input('Задайте длинну списка: '))
mini = int(input('Задайте минимальное значение отбора: '))
maxi = int(input('Задайте максимальное значение отбора: '))

from random import randint
my_list = []
for i in range(long):
    my_list.append(randint(-10, 10))
print(my_list)

listSearch = []
for i in range(mini, maxi + 1):
    for j in range(long):
        if i == my_list[j]:
            listSearch.append(my_list[j])

print(listSearch)