# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу,
# которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

# luckyTicket = int(input('Введите 6ти значный номер вашего билета, проверим счастливый ли он: '))
#
# mum1 = luckyTicket // 100000 % 10
# mum2 = luckyTicket // 10000 % 10
# mum3 = luckyTicket // 1000 % 10
# mum4 = luckyTicket // 100 % 10
# mum5 = luckyTicket // 10 % 10
# mum6 = luckyTicket % 10
#
# print(f'Числа вашего билета: 1е - {mum1}, 2е - {mum2}, 3е - {mum3}, 4е - {mum4}, 5е - {mum5}, 6е - {mum6}.')
#
# leftPartTicket = mum1 + mum2 + mum3
# rightPartTicket = mum4 + mum5 + mum6
#
# if leftPartTicket == rightPartTicket:
#     print('Ваш билет счастливый!')
# else:
#     print('Попробуйте ещё раз.')


# luckyTicket = int(input('Введите 6ти значный номер вашего билета, проверим счастливый ли он: '))
# while luckyTicket < 100000 or luckyTicket > 999999:
#     print('некорректный ввод')
#     luckyTicket = int(input('Введите 6ти значный номер вашего билета, проверим счастливый ли он: '))
# mum1 = luckyTicket // 100000 % 10
# mum2 = luckyTicket // 10000 % 10
# mum3 = luckyTicket // 1000 % 10
# mum4 = luckyTicket // 100 % 10
# mum5 = luckyTicket // 10 % 10
# mum6 = luckyTicket % 10
#
# print(mum1 + mum2 + mum3 == mum4 + mum5 + mum6)

luckyTicket = input()
print (int(luckyTicket[0]) + int(luckyTicket[1]) + int(luckyTicket[2]) == int(luckyTicket[3]) + int(luckyTicket[4]) + int(luckyTicket[5]))