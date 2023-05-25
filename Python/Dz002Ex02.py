# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он
# задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

import math

sumNums = int(input('X + Y = '))
multiplicationNums = int(input('X * Y = '))

# x + y = s  ->  y = s - x
# x * y = p  ->  x*(s-x) = p  ->  sx - x^2 - p = 0  ->  x^2 - sx + p = 0 /квадратное уравнение

num1 = (sumNums + math.sqrt(sumNums * sumNums - 4 * multiplicationNums)) / 2
print(f'X =', num1)

num2 = (sumNums - math.sqrt(sumNums * sumNums - 4 * multiplicationNums)) / 2
print(f'Y =', num2)