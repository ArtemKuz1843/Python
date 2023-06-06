# Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве

# import random
#
# len_of_massiv_1 = int(input("Задайте длину первого массива: "))
# len_of_massiv_2 = int(input("Задайте длину второго массива: "))
#
# massiv_1 = []
# for i in range(len_of_massiv_1):
#     massiv_1.append(random.randint(0,10))
# print(f'Первый массив: {massiv_1}')
#
# massiv_2 = []
# for i in range(len(massiv_1)):
#     massiv_2.append(random.randint(0,10))
# print(f'Второй массив: {massiv_2}')
#
# massiv_3 = []
#
# for i in massiv_1:
#     if i not in massiv_2:
#         massiv_3.append(i)
#
#
# print(massiv_3)

# Задача №41. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод:
# Ввод:
# 5
# 5
# 1 2 3 4 5
# 1 5 1 5 1
# Вывод:
# Вывод:
# 0
# 2
# (каждое число вводится с новой строки

rMass1 = int(input('Введите количество элементов массива: '))
mass1 = []

from random import randint

for _ in range(rMass1):
    num = randint(1, 10)
    mass1.append(int(num))
print(mass1)

rMass2 = int(input('Введите количество элементов массива: '))
mass2 = []

for _ in range(rMass2):
    num = randint(1, 10)
    mass2.append(int(num))
print(mass2)

count1 = 0
for i in range(1, len(mass1)-1):
    if mass1[i-1] < mass1[i] and mass1[i+1] < mass1[i]:
        count1 =+ 1
print(count1)

count2 = 0
for i in range(1, len(mass2)-1):
    if mass2[i-1] < mass2[i] and mass2[i+1] < mass2[i]:
        count =+ 1
print(count2)

# def neigborhs(any_list: list) -> int:
#     count = 0
#     for i in range(1, len(any_list)-1):
#         if any_list[i-1] < any_list[i] and any_list[i+1] < any_list[i]:
#             count += 1
#     return count

# Задача №45. Общее обсуждение
# Два различных натуральных числа n и m называются
# дружественными,
# если
# сумма
# делителей
# числа
# n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105. Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод:
# Вывод:
# 300
# 220 284

def sumdelofnum (num):
    sum = 0
    for i in range (1,num//2+1):
        if num%i == 0:
            sum+=i
    return sum


for i in range (10000):
    for j in range (i,10000):
        if sumdelofnum(i) == j and sumdelofnum(j) == i and i!=j:
            print(i,j)
__________________________________

num = int(input('Введите число: '))
dict_ = dict()
for i in range(1, num + 1):
    sum_ = 0
    for j in range(1, i // 2 + 1):
        if not i % j:
            sum_ += j
    dict_[i] = sum_
print(dict_)
dict_2 = dict()
for k, v in dict_.items():
    for k1, v1 in dict_.items():
        if k == v1 and k1 == v and k != k1 and k1 not in dict_2.keys():
            dict_2[k] = k1

print(dict_2)
____________________________
sum_div_num = {}

for number in range(1, 10000):
    sum_ = 0
    for i in range(1, number // 2 + 1):
        if number % i == 0:
            sum_ += i
    sum_div_num[number] = sum_


for num in sum_div_num:
    if num == sum_div_num.get(sum_div_num.get(num)) and num > sum_div_num.get(num):
        print(num, sum_div_num.get(num))
___________________________________________