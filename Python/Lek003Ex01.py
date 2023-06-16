# Задание: Необходимо создать функцию sumNumbers(n), которая будет считать
# сумму всех элементов от 1 до n.
# def sumNumbers(n):
#     summa = 0
#     for i in range(1, n + 1):
#         summa += i
#     print(summa)
#
# sumNumbers(5)
#
# # n = int(input()) # 5
# # sumNumbers(n) # 15
# ___
# def sumNumbers(n):
#     summa = 0
#     for i in range(1, n + 1):
#         summa += i
#     return summa
#
# n = int(input()) # 5
# print(sumNumbers(n)) # 15
#-----------------------
# def sum_str(*args): # с помощью * можно передавать неограниченное ко-во аргументов
#     res = 0
#     # res = ''
#     for i in args:
#         res += i
#     return res
# # print(sum_str('q', 'e', 'l'))
# # print(sum_str('q', 'e', 'l', 'r', 'f'))
# # print(sum_str('1', '2', '3', '4', '5'))
# print(sum_str(1, 2, 3, 4, 5))
#--------------------
# def new_string(symbol, count): #  есть два аргумента: symbol (символ или число) и count (число, на которое умножается
# # первый аргумент). Если введены оба аргумента, функция работает без ошибок. Если только символ — функция выдает ошибку.
#     return symbol * count
# # print(new_string('!', 5)) # !!!!!
# print(new_string('!')) # TypeError missing 1 required ...
#---
# Можно указать значение переменной count по умолчанию. Например, если значение явно не указано (нет второго аргумента),
# по умолчанию значение переменной count равно трем.
def new_string(symbol, count=3):
    return symbol * count
print(new_string('!', 5)) # !!!!!
print(new_string('!')) # !!!
print(new_string(4)) # 12
#--------------------
# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n-1) + fib(n-2)
#
# list_1 = []
# for i in range(1, 10):
#     list_1.append(fib(i))
# print(list_1)

# ----------------
# def merge_sort(nums):
#     if len(nums) > 1:
#         mid = len(nums) // 2
#         left = nums[:mid]
#         right = nums[mid:]
#         print(f'Лево: {left} . Право: {right}')
#         merge_sort(left)
#         merge_sort(right)
#         i = j = k = 0
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 nums[k] = left[i]
#                 i += 1
#             else:
#                 nums[k] = right[j]
#                 j += 1
#             k += 1
#             print(k)
#         while i < len(left):
#             nums[k] = left[i]
#             i += 1
#             k += 1
#             print(k)
#         while j < len(right):
#             nums[k] = right[j]
#             j += 1
#             k += 1
#             print(k)
#         print(nums)
#
# nums = [38, 27, 43, 3, 9, 82, 10]
# merge_sort(nums)
# print(nums)