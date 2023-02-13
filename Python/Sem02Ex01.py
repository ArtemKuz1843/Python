# a = 'hello'
# for i in a:
#     print (i)

# for e in range(10):    #в range правая граница всегда НЕ включается
#     print (e)

# for e in range(2, 10):
#     print (e)

# for e in range(2, 10, 2):
#      print (e)

# for ind in range(len(a)):
#      print (ind)

# for ind in range(len(a)):
#      print (a[ind])

# for ind in range(len(a)):
#      print (a[ind], end=' ') # конструкция с (, end=' ') выведет в строчку

# for i in range (3): # 1, 2, 3
#      print ('hello')

# for _ in range (3): # для разработчика переменная не важна
#      print ('hello')

# Задача №9. Решение в группах По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N
# # (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# # while
# # Input: 5
# # Output: 120

n = int(input('Введите неотрицательное число: '))
while n < 0:
    print('Ошибка ввода ')
    n = int(input('Введите неотрицательное число: '))

count = 2
fact = 1
while count <= n:
    fact = fact * count
    count = count + 1

print(f'{n}! = {fact}')