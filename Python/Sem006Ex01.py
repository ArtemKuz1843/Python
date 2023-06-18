# # Тернаррные операторы
# a = 15
# b = 10
# print(a if a < b else b) # печатаем а если а меньше б инче печатаем б
#
# (print(a)) if a < b else (b := 80)
# print(b)
#------------------------
# Задача №39.Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве
# Ввод:           Вывод:
# 7               3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 (каждое число вводится с новой строки)

# import random # или from random import randit тогда потом вызываем randit
#
# lenMas1 = int(input("Задайте длину первого массива: "))
# # mass1 = []
# # for i in range (lenMas1):
# #     mass1.append(random.randint(0, 10))
# mass1 = [random.randint(0,10) for i in range(lenMas1)]
# print(f'Первый массив: {mass1}')
#
# lenMas2 = int(input("Задайте длину второго массива: "))
# mass2 = []
# for i in range (lenMas2):
#     mass2.append(random.randint(0, 10))
# print(f'Второй массив: {mass2}')
#
# mass3 = []
# for i in mass1:
#     if i not in mass2:
#         mass3.append(i)
# print(f'Элементы 1го, которых нет во 2ом, в порядке 1го: {mass3}')
#---
# import random
# # f_list = [random.randint(0,10) for _ in range(10)]
# # s_list = [random.randint(0,10) for _ in range(10)]
# print(f_list := [random.randint(0,10) for _ in range(10)]) # если мы что-то хотим присвоить в принте - это называется
# # Маржовый оператор :=
# print(s_list := [random.randint(0,10) for _ in range(10)])
#
# # print(f_list, s_list, sep='\n') # sep='\n c новой строки
#
# print([item for item in f_list if item not in s_list]) # комплихэйшен
#-------------------------------
# Задача №41. Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество
# элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного. Сначала вводится число
# N — количество элементов в массиве. Далее записаны N чисел — элементы массива. Массив состоит из целых чисел.
# Ввод: 5    1 2 3 4 5
# Вывод:    0

# Ввод: 5    1 5 1 5 1
# Вывод:    2

# rMass1 = int(input('Введите количество элементов массива: '))
# from random import randint
# mass1 = [randint(1,10) for i in range(rMass1)]
# # mass1 = []
# # for _ in range(rMass1):
# #     num = randint(1, 10)
# #     mass1.append(int(num))
# print(mass1)
#
# # count1 = 0
# # for i in range(1, len(mass1)-1):
# #     if mass1[i-1] < mass1[i] > mass1[i+1]:
# #         count1 =+ 1
# # print(count1)
# def neigborhs(any_list: list) -> int:
#     count = 0
#     for i in range(1, len(any_list)-1):
#         if any_list[i-1] < any_list[i] and any_list[i+1] < any_list[i]:
#             count += 1
#     return count
#
# print(neigborhs(mass1))
#---
# rMass1 = int(input('Введите количество элементов массива: ')) #капец у парня решение!
# from random import randint
# print(firstList := [randint(1,10) for i in range(rMass1)])
# secondList = [1 for i in range(1, (len(firstList)-1)) if firstList[i-1] < firstList[i] > firstList[i+1]]
# print(secondList)
# print(sum(secondList))
#---то как зациклить список и бегать по нему сколько угодно - 100 раз
# import random
# print(my_list := [random.randint(0,10) for _ in range(10)])
# for i in range(100):
#     print(my_list[i % len(my_list)])
#---сложнаа
# import random
# print(my_list := [random.randint(0,10) for _ in range(10)])
# count = 0
# for i in range(len(my_list)):
#     index = i % len(my_list)
#     if my_list[(i - 1) % len(my_list)] < my_list[i % len(my_list)] > my_list[(i + 1) % len(my_list)]:
#         count += 1
# print(count)
#-----------------------------------------
# Задача №43. Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые два
# элемента, равные друг другу образуют одну пару, которую необходимо посчитать. Вводится список чисел. Все числа списка
# находятся на разных строках.
# Ввод: 1 2 3 2 3    Вывод: 2
# from random import randint
# mini = int(input('Введимте минимальное число: '))
# maxi = int(input('Введимте мвксимальное число: '))
# print(my_list := [randint(mini, maxi) for _ in range(10)])
# kol = 0
# for i in set(my_list):
#     kol = kol + my_list.count(i) // 2
# # for i in range(mini, maxi + 1): # интересное решение, но может быть до мирд и все перебирать
# # # будет не оптимально, поэтому имеет смысл перевести во множество
# #      kol = kol + my_list.count(i) // 2
# print(kol)
#----------------------------------------
# Задача №45. Общее обсуждение Два различных натуральных числа n и m называются дружественными, если сумма делителей
# числа n (включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа. По
# данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. Программа получает на вход
# одно натуральное число k, не превосходящее 10*5. Программа должна вывести все пары дружественных чисел, каждое из
# которых не превосходит k. Пары необходимо выводить по одной в строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую пару не дает).
# Ввод:     300
# Вывод:    220 284
#
# def sumdelofnum (num): # ищем делители числа
#     sum = 0
#     for i in range (1,num//2+1):
#         if num % i == 0:
#             sum += i
#     return sum
#
#
# for i in range (1500): # для каждого числа ищем дружественное от 1 до заданного
#     for j in range (i, 1500):
#         if sumdelofnum(i) == j and sumdelofnum(j) == i and i != j:
#             print(i, j)
# ---
# num = int(input('Введите число до которого будут искаться дружественные числа: '))
# dict_ = dict()
# for i in range(1, num + 1):
#     sum_ = 0
#     for j in range(1, i // 2 + 1):
#         if not i % j:
#             sum_ += j
#     dict_[i] = sum_     # записываем в словарь число-ключ, сумма делителей-ответ
# print(dict_)
# dict_2 = dict()
# for k, v in dict_.items():
#     for k1, v1 in dict_.items():
#         if k == v1 and k1 == v and k != k1 and k1 not in dict_2.keys():
#             dict_2[k] = k1
# print(dict_2)
# ___ разбор решения см рисунок
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