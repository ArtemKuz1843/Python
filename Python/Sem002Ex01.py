# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число
# n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.

# first_el = 0
# second_el = 1
#
# num = int(input('Введите число ,ольше 1: '))
#
# next_el = first_el + second_el
# position = 3
#
# while next_el < num:
#     first_el = second_el
#     second_el = next_el
#     next_el = first_el + second_el
#     position += 1
#
# if next_el == num:
#     print(position)
# else:
#     print(-1)
# ________________________
#
# number = int(input())
#
# n1=0
# n2=1
# position=2
# while n2<number:
#     n1,n2 = n2, n1+n2
#     position+=1
# if n2!=number:
#     print("-1")
# else:
#     print(position)
# ______________________

# Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи. Понятно, что для себя
# нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача: арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, записанных на новой строчке
# каждое. Здесь каждое число – это масса соответствующего арбуза. Все числа натуральные и не превышают 30000
#
# from random import randint
#
# count = int(input('Введите количество арбузов: '))
#
# for i in range(count):
#     print(randint(0, 30000))

# kol = int(input('Количество арбузов = '))
# n = []
# for _ in range(kol):
#     melon = int(input('Введите вес арбуза '))
#     n.append(int(melon))
#
# max = n[0]
# min = n[0]
# for i in n:
#     if i > max:
#         max = i
#     if i < min:
#         min = i
#
# print(f'Больший арбуз себе, весом: {max}')
# print(f'Меньший арбуз тёще, весом: {min}')
# _________________________________________

# Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые
# годы. Их интересует, сколько дней длилась самая длинная оттепель. Оттепелью они называют период, в который
# среднесуточная температура ежедневно превышала 0 градусов Цельсия. Напишите программу, помогающую синоптикам в работе.
#
# from random import randint
#
# days = int(input('Введите количество дней:\n'))
# temp = 1
# count = 0
# total_days = 0
#
# for i in range(days):
#     temp += randint(-3, 3)
#     print(temp)
#
#     if temp > 0:
#         count += 1
#     else:
#         count = 0
#
#     if total_days < count:
#         total_days = count
#
# print(f'Оттепель длилась {total_days}')
# __________________________
# from random import randint
# days = 90
# max = -1
# k = 0
# for i in range(days):
#     temp = randint(-30,10)
#     print(temp)
#     if temp > 0:
#         k+=1
#         if max < k:
#             max = k
#     else :
#         k = 0
# print(max)
