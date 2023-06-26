# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]
# data = list(zip(users, ids, salary)) # пройдёт по количеству в минимальном списке salary !
# print(data)
# --- в дополнение к zip если нам требуется сзиповать даже отсутствующие значения можно:
# from itertools import zip_longest
#
# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]
# data = list(zip_longest(users, ids, salary)) # подставляет значения None
# print(data)
# data = list(zip_longest(users, ids, salary, fillvalue='Нету')) # подставляет значения Нету
# print(data)
# data = list(zip_longest(users, ids, salary, fillvalue=0)) # подставляет нули
# print(data)
#------------
# lambda x,y: x + y #имени у неё нет, никак не мож к ней обратиться. Передаём аргументы Х, У. И что она нам
# # возвращает: Х+У.
# func = lambda x,y: x + y # Её можно присвоить
# аналогично
# def func(x, y):
#     return x + y
# print(func(3, 70))
#------------ пример нужности lambda
# def fire(target):
#     pass
#
# # button = (text = 'vkjdhvk;s', size = 'fbjkdfhb', on_click = fire)# нужн передать без скобок,  со скобками будет
# # # выполнятся, нужно как-то передать аргумент:
# # button = (text = 'vkjdhvk;s', size = 'fbjkdfhb', on_click = fire(enemy)) # так нам нельзя сделать поэтому:
# button = (text = 'vkjdhvk;s', size = 'fbjkdfhb', on_click = lambda : fire(enemy))
#--------------
my_list = '1213354646'