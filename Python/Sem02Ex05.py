# numb = int(input('Введите число: '))
# res = 1
# i = 0
# while i < numb:
#     res = res * (i + 1)
#     i += 1;
# print(res)
#
#
# print("Введите число: ")
# n = int(input())
# i = 1
# sum = 1
# while i < n:
#     i = i + 1
#     sum = sum * i
#     print(sum)
#
#
# n = int(input('Введите число N '))
# fact = 1
# while n>0:
#     fact=fact*n
#     n=n-1
# print('Факториал введенного числа ', fact)
#
#
# number = int(input("Введите целое число >= 0: "))
# factorial = 1
# while number > 1:
#     factorial *= number
#     number -= 1
#
# print(factorial)
# ----------------------------
#
# n = int(input("Введите натуральное число N "))
# index = 3
# fib_1 = 0
# fib_2 = 1
# fib_current = 1
# temp = 1
# while fib_current < n:
#     temp = fib_current
#     fib_current = fib_1 + fib_current
#     fib_2 = fib_1
#     fib_1 = temp
#     index += 1
#
# if fib_current == n:
#     print(f"Это {index-1} число Фибоначчи")
# else:
#     print(f"Такого числа Фибоначчи не существует")


# fibo = [0, 1]
# i = 0
# j = 1
# index = 2
#
# num = int(input("Введите число: "))
#
# while j < num:
#     next_el = i + j
#     fibo.append(next_el)
#     i = j
#     j = next_el
#     index += 1
# print(fibo)
#
# if j == num:
#     print(index)
# else:
#     print(-1)
# ----------------------
# Даны натуральные числа от 35 до 87. Найти и напечатать те из них, которые при делении на 7 дают остаток 1, 2 или 5.
#
# for i in range(35, 88):
#     if i % 7 == 1 or i % 7 == 2 or i % 7 == 5:
#         print(i)

# for i in range(35, 88):
#     if i % 7 in (1, 2, 5):
#         print(f"{i} {i % 7}")
# ----------------
# Составьте программу, которая вычисляет сумму квадратов чисел от 1 до введенного вами целого числа N.
# ------------------

# Валентина прогуляла лекцию по математике. Преподаватель решил подшутить над нерадивой студенткой и попросил ее на
# практическом занятии перечислить все положительные делители некоторых целых чисел. Для несложных примеров студентка
# быстро нашла решения (для числа 6 это: 1, 2, 3, 6; а для числа 16 это: 1, 2, 4, 8, 16), но этим все не закончилось.
# На домашнее задание ей дали варианты посложнее: 23436, 190187200, 380457890232.
#
# Решить такое вручную, как вы понимаете, практически нереально. Вот Валентина и обратилась к вам за помощью.
# Помогите ей (при помощи функции all_divisors(number)).
#
# n = int(input('Введите число:\n'))
#
# for num in range(2, n + 1):
#     if n % num != 0:
#         continue
#     flag = True
#     for spam in range(num - 1, 1, -1):
#         if num % spam == 0:
#             flag = False
#             break
#     if flag:
#         print(num, end=' ')
# _____________________
# Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые
# годы. Их интересует, сколько дней длилась самая длинная оттепель. Оттепелью они называют период, в который
# среднесуточная температура ежедневно превышала 0 градусов Цельсия. Напишите программу, помогающую синоптикам в работе.
# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках располагается
# N целых чисел.
# Каждое число – среднесуточная температура в соответствующий день. Температуры – целые числа и лежат в диапазоне
# от –50 до 50
# Input:    6 -> -20 30 -40 50 10 -10
# Output: 2
#
# analyzed_period = int(input('Укажите анализируемый период, дней:\n>>> '))
# observation_history = [randint(-50, 50) for _ in range(analyzed_period)]
# longest_thaw = 0
# current_length = 0
# for day in observation_history:
#     if 0 < day:
#         current_length += 1
#         if longest_thaw < current_length:
#             longest_thaw = current_length
#     else:
#         current_length = 0
# pretty_text = "\t;\n".join([f"{x[0]}\t|\t{x[1]}" for x in enumerate(observation_history, 1)])
# print('Анализируемый период, день | температура:\n'
#       f'{pretty_text}\t.\n'
#       f'Самая длительная оттепель, дней -> {longest_thaw}')
# _________________________
# 5. Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи. Понятно, что для себя
# нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача: арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, записанных на новой строчке
# каждое. Здесь каждое число – это масса соответствующего арбуза
# Input:	5 -> 5 1 6 5 9
# Output:	1 9
# n = int(input("Введите количество арбузов в сетке: "))
# watermellons = [0] * n
# index = 0
# while index < n:
#     watermellons[index] = int(input("Введите массу арбуза в сетке: "))
#     index +=1
#
# print(f"Массы арбузов в сетке {watermellons}")
#
# max = watermellons[0]
# min = watermellons[0]
# for i in watermellons:
#     if i > max:
#         max = i
#     if i < min:
#         min = i
#
# print(f"Масса самого тяжелого арбуза равна {max} кг")
# print(f"Масса самого легкого арбуза равна {min} кг")
# ___________________________________________
# У вас есть девять цифр: 1, 2, …, 9. Именно в таком порядке. Вы можете вставлять между ними знаки «+», «-» или ничего.
# У вас будут получаться выражения вида 123+45-6+7+89. Найдите все из них, которые равны 100.