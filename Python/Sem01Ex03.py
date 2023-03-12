# 1. За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров?
# При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
# **Input:**
# n = 700
# m = 750
# **Output:**  2

# n = int(input('Сколько киллометров машина проезжает за день: '))
# m = int(input('Сколько киллометров нужно проехать: '))
#
# print((n + m - 1) // n)
# или деление с округлением в большю сторону
# import math
# print('Необходимо', math.ceil(m/n),'дн.')


# 3. В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами.
# За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов.
# Выведите наименьшее число парт, которое нужно приобрести для них.
# **Input:**
# 20
# 21
# 22
# **Output:**
# 32

# a = int(input())
# b = int(input())
# c = int(input())

# print(a // 2 + a % 2 + b // 2 + b % 2 + c // 2 + c % 2)
# print(a % 2, b % 2, c % 2)
# или
# import math
# print('Нужно', math.ceil(a/2) + math.ceil(b/2) + math.ceil(c/2),'парт(ы)')


# 5.Вагоны в электричке пронумерованы натуральными числами, начиная с 1 (при этом иногда вагоны нумеруются от
# «головы» поезда, а иногда – с «хвоста»; это зависит от того, в какую сторону едет электричка). В каждом вагоне
# написан его номер. Витя сел в i-й вагон от головы поезда и обнаружил, что его вагон имеет номер j. Он хочет
# определить, сколько всего вагонов в электричке. Напишите программу, которая будет это делать или сообщать, что без
# дополнительной информации это сделать невозможно.
# Input: 3 4(ввод на разных строках)
# Output: 6

# i = int(input())
# j = int(input())
# if i != j:
#     print(i + j -1)
# else:
#     print('Рассчитать не получится')


# 7. Дано натуральное число. Требуется определить, является ли год с данным номером високосным.
# Если год является високосным, то выведите YES, иначе выведите NO. Напомним, что в соответствии с григорианским
# календарем, год является високосным, если его номер кратен 4, но не кратен 100, а также если он кратен 400.
# **Input:**
# 2016
# **Output:**
# YES

year = int(input())
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('Весокосный')
else:
    print('Не весокосный')