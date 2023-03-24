# *****(3)Напишите программу, которая принимает на вход две строки и определяет, являются ли они анаграммами.
# Знаки препинания, пробелы и регистр при этом игнорируются.
#
# Пример ввода:
# Цари, вино и сало.
# Лисица и ворона.
#
# Пример вывода:
# YES

str1 = input('Введите первую строку: ')
str1 = str1.lower ()
str2 = input('Введите вторую строку: ')
str2 = str2.lower ()

punctuation = ['.',',',':',';','?','!','...','-','"','(',')','/',' ']

for i in str1:
    if punctuation.count(i):
        str1 = str1.replace(i, '')

for i in str2:
    if punctuation.count(i):
        str2 = str2.replace(i, '')

str1 = list(str1)
for i in range(len(str1)):
    j = i + 1
    counter = '1'
    while j < len(str1):
        if str1[i] == str1[j]:
            counter = str(counter)
            str1[j] = str1[i] + counter
            counter = int(counter)
            counter = counter + 1
        j = j + 1
str1 = set(str1)

str2 = list(str2)
for i in range(len(str2)):
    j = i + 1
    counter = '1'
    while j < len(str2):
        if str2[i] == str2[j]:
            counter = str(counter)
            str2[j] = str2[i] + counter
            counter = int(counter)
            counter = counter + 1
        j = j + 1
str2 = set(str2)

if str1 == str2:
    print('Являются анограммами')
else:
    print('Не являются анагаммами')
