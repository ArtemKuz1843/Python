# k = int(input('Укажите сдвиг'))
# values = [1, 2, 3, 4, 5]
# length = len(values)
# k = k % length
# print(values)
# print(values[-k:] + values[:-k])


# dictionary = [{"V": "S001"}, {"V":"S002"}, {"VI":"S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]
# unique = {''}
# unique.clear()
# for item in dictionary:
#     print(item)
#     for temp in item:
#         unique.add(f'{item[temp]}')
# print(unique)


# source = [0, -1, 5, 2, 3, 5]
#
# count = 0
# idx = 0
# while idx < len(source) - 1:
#     idx += 1
#     if source[idx - 1] < source[idx]:
#         count += 1
#
# print(count)

# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.
# Пример ввода:
# a a a b c a a d c d d
#
# Пример вывода:
# a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
#


# str1 = "a a a b c a a d c d d"
#
# def twin_counter(str1):
#     str1 = str1.split(" ")
#     temp = []
#
#     for i in range(len(str1)):
#         counter = 0
#         for j in str1[:i]:
#             if str1[i] == j:
#                 counter += 1
#         if counter > 0:
#             counter = f'_{counter}'
#         else:
#             counter = ''
#
#         temp.append(f"{str1[i]}{counter}")
#
#     print(temp)

# twin_counter(str1)


# source = 'a a a b c a a d c d d'.split()
# count_dict = {}
#
# def transfer(source_list: list):
#     # for idx, el in enumerate(source_list, start=1):
#     for el in source_list:
#         if el not in count_dict:
#             count_dict[el] = 0
#             yield el
#             continue
#         count_dict[el] += 1
#         yield f'{el}_{count_dict[el]}'
#
# [print(_, end=' ') for _ in transfer(source)]