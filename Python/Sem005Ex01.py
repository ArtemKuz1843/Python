# 31. Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где a0 = 0, a1 = 1,
# ak = ak-1 + ak-2 (k > 1).Требуется найти N-е число Фибоначчи
# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n-1) + fib(n-2)
#
# num = int(input('Введите порядковый номер числа Фибоначи: '))
# print(f'{num}ое число Фибоначи есть: {fib(num)}')
# ---
# def fibonacci(num):
#     if num == 0:
#         return 0
#     elif num ==1:
#         return 1
#     else:
#         return fibonacci(num - 1) + fibonacci(num - 2)
# num = int(input("Введите порядковый номер числа Фибоначи: "))
# print(f'{num}ое число Фибоначи есть: {fibonacci(num)}')
#---
# def fibo(number: int) -> int:
#     if number in [0, 1]:
#         return number
#     return fibo(number - 1) + fibo(number - 2)
# print(fibo(8))
# ______________________
# 33. Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# 54321 - 14321
# mark = [5, 5, 4, 5, 3, 2, 1, 4]
# print(mark)
# maximal = max(mark)
# minimal = min(mark)
# for i in range(len(mark)):
#     if mark[i] == maximal:
#         mark[i] = minimal
# print(mark)
# НО! Нужно понимать:
# mark = [5, 5, 4, 5, 3, 2, 1, 4]
# print(mark)
# for i in range(len(mark)):
#     if mark[i] == max(mark): # так список будет преобразовываться в режиме реального времени, не только 5, но и 4 и
# # далее, до прохождения, до конца длины списка
#         mark[i] = min(mark)
# print(mark)
# # [5, 5, 4, 5, 3, 2, 1, 4]
# # [1, 1, 4, 1, 3, 2, 1, 1]
# _______________
# 35. Напишите функцию, которая принимает одно число и проверяет, является ли оно простым? Напоминание: Простое число
# - это число, которое имеет 2 делителя: 1  и n(само число)*
# def issimple_number(num):
#     kol = 0
#     for i in range(1, num+1):
#         if num % i == 0:
#             kol += 1
#         if kol == 2:
#             return (f'Число {num} простое')
#         else:
#             return (f'Число {num} составное')
# print(issimple_number(51))
#---
def is_simple(number: int) -> bool:
    if number in [1, 2]:
        return True
    if number % 2 == 0:
        return False
    for dev in range(3, number // 2 + 1, 2): # идём от 3ки, т.к. 1 и 2 прошли, идём до половины числа, т.к. выше не
# будет делителей, +1 т.к. может быть нечётное число, все чётные числа отброшени и берём шаг 2, чтобы их отбросить
# уже тут и цикл сокращается в 4 раза повышается про-ть
        if number % dev == 0:
            return False
    return True
print(is_simple(51))
# ___________
# 37. Дано натуральное число *N* и последовательность из *N* элементов. Требуется вывести эту последовательность в
# обратном порядке. ***Примечание.*** В программе запрещается объявлять массивы и использовать циклы (даже для ввода
# и вывода).
# def posl(lenght):
#     if lenght == 0:
#         return ''
#     perem = input('Введите двнные: ')
#     return posl(lenght - 1) + perem #  Через составление строки
#     # posl(lenght-1)
#     # return print(perem)
# print(posl(4))
# ---
# def reverse(n: int) -> None:
#     """Переворот строки рекурсией"""
#     if n == 0:
#         return print('')
#     k = int(input())
#     reverse(n - 1)
#     return print(k)
# n = int(input())
# reverse(n)
#---
 # Через составление строки
def f(n):
    if n == 0:
        return ''
    k = int(input())
    return f(n - 1) + f' {k}'

n = int(input())
print(f(n))