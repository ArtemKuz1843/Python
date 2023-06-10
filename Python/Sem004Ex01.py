# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.
# stroka = input("Введите строку: ")
#
# spisok = []
# for i in stroka:
#     spisok.append(i)
# print(spisok)
#
# mnog = set(spisok)
# spisokSravn = list(mnog)
# print(spisokSravn)
#
# for i in spisokSravn:
#     count = 0
#     for j in range(len(spisok)):
#         if i == spisok[j]:
#             count += 1
#             count = str(count)
#             spisok[j] = i + '_' + count
#             count = int(count)
#
# print(spisok)
# _________________
# import random
#
# my_list = [random.randint(0,10) for _ in range(20)]
# print(my_list)
#
# counter = {}

# # for item in my_list:
# #     counter[item] = counter.get(item, 0) + 1
# # print(counter)
#
# for item in my_list:
#     counter[item] = counter.get(item, 0) + 1
#     print(item if counter.get(item) < 2 else (str(item) + '_' + str(counter.get(item) - 1)), end = ' ') # end = ' ' чтобы было в 1 строчку
#
# #набираем список в столбик
# # for item in my_list:
# #     counter[item] = counter.get(item, 0) + 1
# #     print(counter)
# # _______________

# for i in my_list:
#     if counter.get(i, None): # if counter.get(i)
#         counter[i] += 1
#     else:
#         counter[i] = 1
#
# # for i in my_list: # попытка переписать в 1 строку
# #     print(counter[i] += 1 if counter.get(i) else counter[i] = 1)
# #
# print(counter)
# _________________________

# Задача №27. Решение в группах. Пользователь вводит текст(строка). Словом считается последовательность непробельных
# символов идущих подряд, слова разделены одним или большим числом пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells
# Output: 13

stroka = '''She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells 
sea shells on the sea shore I'm sure that the shells are sea shore shells'''
# print(stroka)
#
spisok = stroka.split()
print(spisok)

mnog = set(spisok)
print(mnog)

spisokDlin = list(mnog)
print(len(spisokDlin))
# ________________________________
# Ваня и Петя поспорили, кто быстрее решит следующую задачу: “Задана последовательность неотрицательных целых чисел.
# Требуется определить значение наибольшего элемента последовательности, которая завершается первым встретившимся нулем
# (число 0 не входит в последовательность)”. Однако 2 друга оказались не такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор. За помощью товарищи
# обратились к Вам, студентам.
#
# n = int(input())
# max_number = 1000
# while n != 0:
# n = int(input())
# if max_number > n:
# max_number = n
# print(max_number)
#
# n = int(input())
# max_number = -1
# while n < 0:
# n = int(input())
# if max_number < n:
# n = max_number
# print(n)