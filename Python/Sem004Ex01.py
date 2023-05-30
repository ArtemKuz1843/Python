# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.

# stroka = input("Введите строку: ")
#
# print(stroka)
#
# spisok = []
# for i in stroka:
#     spisok.append(i)
# print(spisok)
#
# mnog = set(spisok)
#
# print(mnog)
#
# spisokSravn = list(mnog)
#
# print(spisokSravn)
#
#
# for i in spisokSravn:
#     count = 0
#     for j in spisok:
#         if i == j:
#             count += 1
#             count = str(count)
#             j = j + count
#             count = int(count)
# print(spisok)


# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

# stroka = input("Введите строку: ")
# print(stroka)
#
# spisok = stroka.split()
# print(spisok)
#
# mnog = set(spisok)
# print(mnog)
#
# spisokDlin = list(mnog)
# print(len(spisokDlin))
# ________________________________
Ваня и Петя поспорили, кто быстрее решит следующую задачу: “Задана последовательность неотрицательных целых чисел.
Требуется определить значение наибольшего элемента последовательности, которая завершается первым встретившимся нулем
(число 0 не входит в последовательность)”. Однако 2 друга оказались не такими смышлеными. Никто из ребят не смог до
конца сделать это задание. Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор. За помощью товарищи
обратились к Вам, студентам.

n = int(input())
max_number = 1000
while n != 0:
n = int(input())
if max_number > n:
max_number = n
print(max_number)

n = int(input())
max_number = -1
while n < 0:
n = int(input())
if max_number < n:
n = max_number
print(n)