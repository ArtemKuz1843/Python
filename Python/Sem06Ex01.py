# n = int(input("Введите количество элементов в первом массиве: "))
# array1 = [0]*n
# for i in range(n):
#     array1[i] = int(input("Введите элемент первого массива: "))
#
# m = int(input("Введите количество элементов во втором массиве: "))
# array2 = [0]*m
# for i in range(m):
#     array2[i] = int(input("Введите элемент второго массива: "))
#
# print(f"Первый массив: {array1}")
# print(f"Второй массив: {array2}")
#
# def new_func(array1, array2):
#     array_combo = []
#     for i in array1:
#         if i not in array2:
#             array_combo.append(i)
#     return array_combo
#
# array_combo = new_func(array1, array2)
#
# print(f"Массив непересечений: {array_combo}")



# n = int(input("Введите кол-во элементов первого множества: "))
# m = int(input("Введите кол-во элементов второго множества: "))
#
# array1 = []
# print("Введите элементы первого множества: ")
# for i in range(n):
#     n1 = input()
#     array1.append(n1)
# print(f"Первое множество: ", *array1)
#
# array2 = []
# print("Введите элементы второго множества: ")
# for i in range(m):
#     n2 = input()
#     array2.append(n2)
# print(f"Второе множество: ", *array2)
#
# array3 = []
# count1 = 0
# for i in array1:
#     if i not in array2:
#         array3.append(i)
#         count1 += 1
#
# print(*(array3))
# print(count1)
#
# array4 = []
# count2 = 0
# for i in array2:
#     if i not in array1:
#         array4.append(i)
#         count2 += 1
#
# print(*(array4))
# print(count2)



# n = int(input())  # количество элементов в первом массиве
# a = list(map(int, input().split()))  # первый массив
# if len(a) != n:
#     print("Некорректный ввод первого массива")
#     exit()
# m = int(input())  # количество элементов во втором массиве
# b = set(map(int, input().split()))  # второй массив
# if len(b) != m:
#     print("Некорректный ввод второго массива")
#     exit()
#
# for x in a:
#     if x not in b:
#         print(x, end=' ')



# n = input_number("Введите кол-во элементов первого множества")
#     m = input_number("Введите кол-во элементов второго множества")
#     arr1 = [input_number("Введите " + str(i+1) + " элемент 1го мн-ва" ) for i in range(n)]
#     arr2 = [input_number("Введите " + str(i+1) + " элемент 2го мн-ва" ) for i in range(m)]
#     print(set(arr1).difference(set(arr2)))



# def input_num(message: str) -> int:
#     input_error: bool = True
#     while input_error:
#         try:
#             temp = int(input(message))
#         except ValueError:
#             print("Вы ввели не число!")
#         else:
#             input_error = False
#             return temp
#
# def input_list(message: str) -> list:
#     temp_list = []
#     for i in range(input_num('Please input size of ' + message + ': ')):
#         temp_list.append(input_num(f'{i + 1} element of {message}: '))
#     print('-' * 20)
#     return temp_list
#
#
# def n_minus_m(n_local: list, m_local: list) -> list:
#     n_edit = []
#     m_local = set(m_local)
#     for i in n_local:
#         if i in m_local:
#             n_edit.append(i)
#     return n_edit
#
# n, m = [input_list(x) for x in ('list N', ' list M')]
# print(n, m)
# n_m = [i for i in n if i not in m]
# print(*n_m)
# print(*n_minus_m(n, m))



# Дано натуральное число n>1. Выведите все простые множители этого числа в порядке неубывания с учетом кратности.
# Алгоритм должен иметь сложность O(logn).
#
# def PrimeNumbers1(Number):
#     primelist = []
#     k=0
#     for i in range(2, Number):
#         for j in range(2, i):
#             if i%j==0:
#                 k=k+1
#         if k==0:
#             primelist.append(i)
#         else:
#             k=0
#     return primelist
#
#
#
# def prime_factors(n, divisor=2):
#     if n == 1:
#         return
#     if n % divisor == 0:
#         print(divisor, end=" ")
#         prime_factors(n//divisor, divisor)
#     else:
#         prime_factors(n, divisor+1)



# def prime_factors(n, divisor=2):
#     if n == 1:
#         return
#     if n % divisor == 0:
#         print(divisor, end=" ")
#         prime_factors(n//divisor, divisor)
#     else:
#         prime_factors(n, divisor+1)
# EugeneN 20:38



# def wer(n):
#     for i in range(2, n+1):
#         if n%i == 0:
#             if i == n:
#                 return [i]
#             else:
#                 return [i] + wer(n//i)
#
#
# print(wer(12))



# Задача №41. Общее обсуждение
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод: Ввод:
# 5 5
# 1 2 3 4 5 1 5 1 5 1
# Вывод: Вывод:
# 0 2
# (каждое число вводится с новой строки)
#
# def find_num(tmp_list):
#     count = 0
#     for i in range(1, len(tmp_list) - 1):
#         if tmp_list[i - 1] < tmp_list[i] > tmp_list[i + 1]:
#             count += 1
#     return count
#
# list_1 = [1, 5, 1, 5, 1, 3, 2]
# #list_1 = [1, 2, 3, 4, 5, 6]
#
# print(find_num(list_1))



# import random
#
#
# def input_num(message: str) -> int:
#     input_error: bool = True
#     while input_error:
#         try:
#             temp = int(input(message))
#         except ValueError:
#             print("Вы ввели не число!")
#         else:
#             input_error = False
#             return temp
#
#
# n = [random.randint(1, 6) for i in range(input_num('Please input size of N list: '))]
# print(n)
# l_set = set(n)
# for x in l_set:
#     if n.count(x)-1:
#         print(f' digit {x}, count - {(n.count(x) - 1)*(n.count(x)) / 2}', end=" //  ")



# Задача №45. Общее обсуждение
# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 10 5 . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод: Вывод:
# 300 220 284
#
# def sum_dividers(n):
#     return sum(x for x in range(1, n//2+1) if not n % x)
#
#
# k = int(input('input k: '))
#
# for i in range(1, k+1):
#     potentially_friendly = sum_dividers(i)
#     if i < potentially_friendly and i == sum_dividers(potentially_friendly):
#         print(i, potentially_friendly)