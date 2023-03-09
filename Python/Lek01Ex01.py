# print(5)

# print(5, 8, 7 )

# n = 5
# print(n)

# n = None
# print(n)

# n = 1.89
# print(n)
# n = 'dvsvva'
# print(n)
# n = "fvsdvadv"
# print(n)

# n = 5
# print(type(n))
# n = 'dvsvva'
# print(type(n))

# n = 'fd\'df'
# print(n)

# """
# n = 'fd"gbuz"df'
# print(n)
# """
# print('"""')

# a = 5
# b = 1.28
# c = 'bit'
# print(a, b, c)
# print(a, '-', b, '-', c)
# print(f'{a} - {b} - {c}')
# print('{} - {} - {}'.format(a, b, c))

# input()

# a = input()
# print(a)

# print('Введите первую строку: ')
# a = input()
# print(a)
# b = input('Ведите вторую строку: ')
# print(b)
# print(a, '+', b, '=', a + b) # Сложит как строки

# c = 5.89
# print(c)
# n = int(c)
# print(n)

# c = 5.89
# print(c)
# print(type(c))
# c = int(c)
# print(c)
# print(type(c))

# c = 5.89
# print(c)
# print(type(c))
# c = str(c)
# print(c + '89')
# print(type(c))

# c = 0 # 1 - True
# print(c)
# print(type(c))
# c = bool(c)
# print(c)
# print(type(c))

# print('Введите первую строку: ')
# a = int(input())
# print(a)
# b = int(input('Ведите вторую строку: '))
# print(b)
# print(a, '+', b, '=', a + b) # Сложит как строки

# a = 5.89956
# b = 6.556551
# print(a * b)
# print(round(a * b, 3))

# a = 1 > 4
# print(a) #False

# a = 1 < 4 and 5 > 2
# print(a) #True

# a = 1 == 2
# print(a) #False

# a = 1 != 2
# print(a) #True

# a = 'qwe'
# b = 'qwe'
# print(a == b) #True

# a = 1 < 3 < 5 < 10
# print(a) #True

# a = 1 < 3 < 3 < 10
# print(a) #False

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же МАША!')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ)')
# else:
#     print('Привет, ', username)

# n = 423  # программа считает сумму цифр
# summa = 0
# while n > 0:
#     x = n % 10
#     summa = summa + x
#     n = n // 10
# print(summa) # 9

# i = 0
# while i < 5:
#     # if i == 3:
#     #     break
#     i = i + 1
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(i)

# n = int(input()) # Программа находит минимальный делитель данного числа
# flag = True
# i = 2
# while flag:
#     if n % i == 0: # если остаток при делении числа n на i равен 0
#         flag = False
#         print(i)
#     elif i > n // 2: # делить числа не может превышать введенное число, деленное на 2
#         print(n)
#         flag = False
#     i += 1

# for i in 1, -2, 3, 14, 5:
#     print(i)

# r = range(5) # 0 1 2 3 4
# r = range(2, 5) # 2 3 4
# r = range(0, -5) # ----
# r = range(1, 10, 2) # 1 3 5 7 и 9
# r = range(100, 0, -20) # 100 80 60 40 20
# r = range(100, 0, -20) # range(100, 0, -20)
# for i in r: # Вместо r можно сразу писать range
#     print(i) # 100 80 60 40 20
# for i in range(100, 0, -20):
#     print(i)

# a = 'qwerty'
# # print(a[0])
# # print(a[2])
# for i in a:
#     print(i)

# line = ""
# for i in range(5): # Вложенные циклы
#     line = ""
#     for j in range(5):
#         line += "*"
#     print(line)

# text = 'СъЕШЬ ещё этих МяГкИх французских булок'
# print(len(text)) # 39
# print('ещё' in text) # True
# print(text.lower()) # съешь ещё этих мягких французских булок
# print(text.upper()) # СЪЕШЬ ЕЩЁ ЭТИХ МЯГКИХ ФРАНЦУЗСКИХ БУЛОК
# print(text.replace('ещё','ЕЩЁ')) # СъЕШЬ ЕЩЁ этих МяГкИх французских булок

# text = 'съешь ещё этих мягких французских булок'
# print(text[0]) # c
# print(text[1]) # ъ
# print(text[len(text)-1]) # к
# print(text[-5]) # б
# print(text[:]) # съешь ещё этих мягких французских булок
# print(text[20:]) # с 20 эл до конца
# print(text[:2]) # съ
# print(text[len(text)-2:]) # ок
# print(text[2:9]) # ешь ещё
# print(text[6:-18]) # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ...
# print(text)