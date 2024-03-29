# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B
# с помощью рекурсии. *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

num1 = int(input('Введите число: '))
num2 = int(input('Введите степень для числа: '))

def degree(number, nStep):
    if nStep == 0:
        return 1
    return number * degree(number, nStep - 1)

print(degree(num1, num2))