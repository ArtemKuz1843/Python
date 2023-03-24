# Задача №31. Общее обсуждение
# Последовательностью Фибоначчи называется
# последовательность чисел a 0 , a 1 , ..., a n , ..., где
# a 0 = 0, a 1 = 1, a k = a k-1 + a k-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию

# num = int(input('Please input number: '))
# def fibonachy(n: int):
#     if n == 0 or n == 1:
#         return n
#     return fibonachy(n - 1) + fibonachy(n - 2)
#
# print(fibonachy(num))


# n1 = int(input("Введите искомый элемент: "))
# def fib(n):
#     if n in [0, 1]:
#         return 1
#     return fib(n - 1) + fib(n - 2)
#
# list_1 = []
# for i in range(0, n1 + 1):
#     list_1.append(fib(i))
# print(*list_1)
#
# print(list_1[n1])

#
# def vasya_bad_hacker(array):
#     array_new = [0]*len(array)
#     for i in range(len(array)):
#         if array[i] == max(array):
#             array_new[i] = min(array)
#         else:
#             array_new[i] = array[i]
#     return array_new
#
# array = [1, 3, 4, 5, 2, 5, 2, 3, 5, 4]
# print(f"Первоначальные оценки {array}")
# print(f"Итоговые оценки {vasya_bad_hacker(array)}")


# import random
#
# def get_new_rating(rating, n, count=0, new_rating=None):
#     if new_rating is None:
#         new_rating = []
#     if count == n:
#         return new_rating
#     else:
#         new_rating.append(1) if rating[count] > 4 else new_rating.append(rating[count])
#     return get_new_rating(rating, n, count + 1, new_rating)
#
# n = int(input('Введите общее количество оценок: '))
# rating = [random.randint(1, 5) for _ in range(n)]
# print(rating)
# print(get_new_rating(rating, n))


# def is_prime(n, i=2):
#     if n == 2 or i > int(n ** 0.5):
#         return True
#     if n % i == 0:
#         return False
#     return is_prime(n, i+1)
##
# n = int(input("Введите число: "))
# if is_prime(n):
#     print(n, "является простым числом")
# else:
#     print(n, "не является простым числом")



# def recursive_input2(size_n: int):
#     x = input('please input: ')
#     if size_n == 1:
#         print(x, end=' ')
#     else:
#         recursive_input2(size_n - 1)
#         print(x, end=' ')
#
#
# n = int(input('Please input number: '))
#
# recursive_input2(n)


# Дана последовательность натуральных чисел (одно число в строке), завершающаяся числом 0. Определите значение второго по величине элемента в этой последовательности, то есть элемента, который будет наибольшим, если из последовательности удалить наибольший элемент.
# В этой задаче нельзя использовать глобальные переменные. Функция получает данные, считывая их с клавиатуры, а не получая их в виде параметра. В программе на языке Python функция возвращает результат в виде кортежа из нескольких чисел и функция вообще не получает никаких параметров. В программе на языке C++ результат записывается в переменные, которые передаются в функцию по ссылке. Других параметров, кроме как используемых для возврата значения, функция не получает.
# Гарантируется, что последовательность содержит хотя бы два числа (кроме нуля).


# Даны натуральные числа k и s. Определите, сколько существует k-значных натуральных чисел, сумма цифр которых равна d. Запись натурального числа не может начинаться с цифры 0.
# В этой задаче можно использовать цикл для перебора всех цифр, стоящих на какой-либо позиции.