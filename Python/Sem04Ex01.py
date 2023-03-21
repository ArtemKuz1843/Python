# def find_expressions(total, digits, expression=""):
#     # если все цифры использованы, проверяем выражение на равенство 100
#     if not digits:
#         if eval(expression) == total:
#             print(expression + " = " + str(total))
#         return
#
#     # добавляем текущую цифру и вызываем функцию для следующей цифры
#     current = str(digits[0])
#     find_expressions(total, digits[1:], expression + current)
#
#     # добавляем знак + и вызываем функцию для следующей цифры
#     find_expressions(total, digits[1:], expression + "+" + current)
#
#     # добавляем знак - и вызываем функцию для следующей цифры
#     find_expressions(total, digits[1:], expression + "-" + current)
#
#
# # вызываем функцию для цифр от 1 до 9 и искомого значения 100
# find_expressions(100, [1, 2, 3, 4, 5, 6, 7, 8, 9])

# найти в группе задачу с if ами

# """ Задача со звёздочкой №1:
# У вас есть девять цифр: 1, 2, …, 9. Именно в таком порядке.
# Вы можете вставлять между ними знаки '+', '-' или ничего. У вас будут получаться выражения вида 123+45-6+7+89.
# Найдите все из них, которые равны 100.
#
# """
#
#
# def solve_expression(sequence: tuple, expression: str = '') -> None:
#     if len(sequence) == 1:
#         expression += f'{sequence[0]}'
#         if eval(expression) == 100:
#             print(f'{expression} == 100')
#     else:
#         solve_expression(sequence[1:], expression + f'{sequence[0]}')
#         solve_expression(sequence[1:], expression + f'{sequence[0]} + ')
#         solve_expression(sequence[1:], expression + f'{sequence[0]} - ')
#
#
# def main():
#     sequence_of_digits = (1, 2, 3, 4, 5, 6, 7, 8, 9)
#     solve_expression(sequence_of_digits)
#
#
# if __name__ == '__main__':
#     main()


# """ Задача №25:
# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый
# символ уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.
#
# Input:
# - a a a b c a a d c d d
# Output:
# - a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
#
# Для решения данной задачи используйте функцию .split()
# """
#
#
# def using_dict(source: str) -> None:
#
#     count_dict = {}
#     stack = []
#     for index in range(len(source)):
#         el = source[index]
#         if el.isalnum():
#             count_dict[el] = source[:index].count(el)
#             stack.append(el if not count_dict[el] else f'{el}_{count_dict[el]}')
#
#     print('From using_dict\t->', ' '.join(stack))
#
#
# def using_str(sequence: str):
#
#     stack = []
#     for index in range(len(sequence)):
#         char = sequence[index]
#         if not char.isalnum():
#             continue
#         counter = sequence[:index].count(char)
#         stack.append(char if not counter else f'{char}_{counter}')
#     print('From using_str\t->', ' '.join(stack))
#
#
# def main() -> None:
#     queue = 'a a a b c a a d c d d'
#     using_str(queue)
#     using_dict(queue)
#
#
# if __name__ == '__main__':
#     main()


# str_list = input().split()
#
# set_str = set(str_list)
#
# for i in set_str:
#     count = 0
#     for s in range(len(str_list)):
#         if i == str_list[s]:
#             if count >= 1:
#                 str_list[s] = str_list[s] + "_" + str(count)
#             count += 1
#
# print (str_list)


# text = ['a', 'a', 'a', 'b', 'c', 'a', 'a', 'd', 'c', 'd', 'd']
#     # input('Введите строку: ').split()
# print(text)
# for i in range(len(text))[::-1]:
#     count = text[:i].count(text[i])
#     print(count)
#     if count > 0:
#         text[i] = text[i] + '_' + str(count)
#         # print(count)
# print(text)



# Задача №27. Общее обсуждение
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов или символами конца строки.Определите,
# сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore;The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore,I'm sure that the shells are sea
# shore shells.
# Output: 19

# text = "She sells sea shells on the sea shore " \
#        "The shells that she sells are sea shells I'm sure." \
#        "So if she sells sea shells on the sea shore " \
#        "I'm sure that the shells are sea shore shells"
#
# print('Получено выражение: '"\t", text)
#
# text = set(text.lower().split())
# print(f'В представленном тексте содержится {len(text)} уникальных слов')


# text = input("Введите текст: ")
#
# # разбиваем текст на слова
# words = text.split()
#
# # создаем множество для хранения уникальных слов
# unique_words = set()
#
# # проходимся по каждому слову и добавляем его в множество уникальных слов
# for word in words:
#     unique_words.add(word)
#
# # выводим количество уникальных слов в тексте
# print("Количество различных слов в тексте:", len(unique_words))


# https://github.com/Alhafat/Python/tree/main/seminars/seminar_4/lesson