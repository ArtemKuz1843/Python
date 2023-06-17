# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке
# возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем
# пользователь вводит сами элементы множеств.

size1 = int(input('Введите раазмер первого набора n: '))
kit1 = []

from random import randint
for i in range(size1):
    i = randint(-10, 10)
    kit1.append(i)
print(kit1)
kit1 = set(kit1)

size2 = int(input('Введите раазмер второго набора m: '))
kit2 = []

for i in range(size2):
    i = randint(-10, 10)
    kit2.append(i)
print(kit2)
kit2 = set(kit2)

kit3 = kit1.intersection(kit2)
kit3 = sorted(list(kit3))
print(f'Пересечение наборов и сортировка: {kit3}')

# ___ проверочный код не работает!!! ___
# mol = [int(x) for x in input().split()]
# # print(mol)
# n = mol[0]
# m = mol[1]
# # print(n)
# # print(m)
# set_1 = set()
# set_2 = set()
# list_1 = list()
# a = [int(x) for x in input().split()]
# k = set(a)
# for i in k:
#     set_1.add(i)
# b = [int(x) for x in input().split()]
# k1 = set(b)
# for i in k1:
#     set_2.add(i)
# lok = set_1 & set_2
# kool = list(lok)
# kool.sort()
# for i in kool:
#     print(i, end=' ')