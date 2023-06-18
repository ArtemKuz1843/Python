# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов
# нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d. Каждое число вводится
# с новой строки. Ввод: 7 2 5 . Вывод: 7 9 11 13 15

firstEl = int(input('Введите первый элемент прогрессии: '))
dif = int(input('Введите разность элементов: '))
countEl = int(input('Введите количество элементов в прогрессии: '))
def progression(el1, step, long):
    listProgres = []
    for i in range(1, long + 1):
        listProgres.append(el1 + (i - 1) * step)
    return listProgres

print(progression(firstEl, dif, countEl))