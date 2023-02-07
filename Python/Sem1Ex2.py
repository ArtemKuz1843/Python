# 1. Меньшее из двух
# Пользователь вводит два целых числа. Выведите меньшее из них.
#
# 2. Четырехзначное?
# Пользователь вводит целое число. Выведите YES, если это число является четырехзначным, и NO в противном случае.

# a = int(input())
# b = int(input())
# if a < b:
#     print(a)
# elif a == b:
#     print('Числа равны')
# else:
#     print(b)

# a = int(input())
# if 1000 <= a <= 9999 or -9999 <= a <= -1000:
#     print('Yes')
# else:
#     print('No')

# a = input()
# if '-' in a:
#     if len(a) == 5:
#         print('Yes')
#     else:
#         print('No')
# else:
#     if len(a) == 4:
#         print('Yes')
#     else:
#         print('No')

# a = input()
# print(len(a) == 4)

# a = input()
# if a.isdigit(): # функция проверит, что в строке число
#     print('число')
#
# Пользователь вводит строки пока не введёт пустую, гарантируется, что в строках лежат только цифры
# Найти сумму введённых чисел, которые кратны 4

# summa = 0 # не использовать SUM так как на неё в питоне есть зарезервированная функция
# while True:
#     a = input()
#     if a == '':
#         break
#     if int(a) % 4 == 0:
#         # summa = summa + int(a)
#         summa += int(a)
# print(summa)

summa = 0 # не использовать SUM так как на неё в питоне есть зарезервированная функция
flag = True
while flag:
    a = input()
    if a == '':
        flag = False
        continue
    if int(a) % 4 == 0:
        summa += int(a)
print(summa)