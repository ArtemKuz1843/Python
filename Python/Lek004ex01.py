# def f(x):
#     return x ** 2
#
# # print(f(4)) # 16
# # print(type(f)) # <class 'function'>
#
# g = f
# print(g(4)) # 16
# print(type(g)) # <class 'function'>

#------------------------------------
#
# def calk1(a):
#     return  a + a
#
# def calk2(a):
#     return  a * a
#
# def math(op, x):
#     print(op(x))
#
# math(calk1, 5)
#---
# def calk1(a, b):
#     return  a + b
#
# def calk2(a, b):
#     return  a * b
#
# def math(op, x, y):
#     print(op(x, y))
#
# math(calk2, 5, 100)
#---
# # calk1 = lambda a,b: a + b
# # def calk1(a, b):
# #     return  a + b
# def math(op, x, y):
#     print(op(x, y))
#
# # math(calk1, 5, 100)
# math(lambda a,b: a + b, 5, 100)
#------------------------------------
# Задача для самостоятельного решения 1. В списке хранятся числа. Нужно выбрать только чётные числа и составить список
# пар (число; квадрат числа). Пример: 1 2 3 5 8 15 23 38 Получить: [(2, 4), (8, 64), (38, 1444)]
# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = list()
# for i in data:
#     if i % 2 == 0:
#         res.append((i, i**2))
# print(res)
#---
# def select (f, col):
#     return [f(x) for x in col] #зачем-то список преобразуем методом в такойже список из чисел
# def where (f, col):
#     return [x for x in col if f(x)] #будет проверка на чётность
#
# res = select(int, data)
# print(res)
#
# res = where(lambda x: x % 2 == 0, res)
# print(res)
#
# res = select(lambda x: (x, x**2), res) # а, вот зачем...
# print(res)
# ----------------
# list_1 = [x for x in range(1, 20)]
# print(list_1)
#
# list_1 = list(map(lambda  x: x + 10, list_1))
# print(list_1)
#---
# Задача: C клавиатуры вводится некий набор чисел, в качестве разделителя используется пробел. Этот набор чисел будет
# считан в качестве строки. Как превратить list строк в list чисел
# data = '15 156 96 3 5 8 52 5'
# print(data)
#
# data = list(map(int, data.split()))
# print(data)
#---------------- к предыдущей задаче через MAP
# data = [1, 2, 3, 5, 8, 15, 23, 38]
# def where (f, col):
#     return [x for x in col if f(x)] #будет проверка на чётность
#
# res = map(int, data)
# print(res)
#
# res = where(lambda x: x % 2 == 0, res)
# print(res)
#
# res = list(map(lambda x: (x, x**2), res))
# print(res)
#-------------------------
# data = [15, 65, 9, 36, 175]
# print(data)
#
# res = list(filter(lambda  x: x % 10 == 5, data))
# print(res)
#---------------- к предпредыдущей задаче через FILTER
# data = [1, 2, 3, 5, 8, 15, 23, 38]
#
# res = map(int, data)
# res = filter(lambda x: x % 2 == 0, res)
#
# res = list(map(lambda x: (x, x**2), res))
# print(res)
#----------------------------------------- ZIP
# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# data = list(zip(users, ids))
# print(data)
#---
# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]
# data = list(zip(users, ids, salary)) # пройдёт по количеству в минимальном списке salary !
# print(data)
#------------------------------------- ENUMERATE
# users = ['user1', 'user2', 'user3']
# data = list(enumerate(users))
# print(data)
#------------------------------ файлы
# colors = ['red', '8888', 'blue'] # 8888 - всё пишется подряд
# data = open('file.txt', 'a') # здесь указываем режим, в котором будем работать
# data.writelines(colors) # разделителей не будет
# data.close() # в file.txt redgreenblue
#---
# with open('file.txt', 'w') as data: # в данном режиме перезапис, не допис
#     data.write('line 1\n') # \n -  перенос
#     data.write('line 2\n')
# print(56) # как только заверш работа with закроется файл
#---
path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()