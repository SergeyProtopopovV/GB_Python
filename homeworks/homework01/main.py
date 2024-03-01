# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

# user_number = int(input("Введите 3-х значное число: "))
#
# first_digit = user_number // 100
# second_digit = user_number // 10 - first_digit * 10
# third_digit = user_number % 10
#
# digits_summ = first_digit + second_digit + third_digit
# print(f'сумма цифр числа {user_number} равна {digits_summ}')
#
# user_number = input("Введите 3-х значное число: ")
# print(f'сумма цифр числа {user_number} равна {int(user_number[0]) + int(user_number[1]) + int(user_number[2])}')


# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10

# cranes = int(input("Введите общее количество журавликов: "))
#
# if cranes % 6 == 0:
#     print(f'сделали журавликов: Петя - {cranes // 6}, Катя - {cranes // 6 * 4}, Сережа - {cranes // 6}')
# else:
#     print('Ребята не могли сделать такое количество журавликов вместе')


# Задача 6: Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 ->

# user_number = int(input("Введите номер билета: "))
#
# first_part = user_number // 1000
# second_part = user_number % 1000
# first_digit_first_part = first_part // 100
# second_digit_first_part = first_part // 10 - first_digit_first_part * 10
# third_digit_first_part = first_part % 10
# first_digit_second_part = second_part // 100
# second_digit_second_part = second_part // 10 - first_digit_second_part * 10
# third_digit_second_part = second_part % 10
#
# digit_summ_first = first_digit_first_part + second_digit_first_part + third_digit_first_part
# digit_summ_second = first_digit_second_part + second_digit_second_part + third_digit_second_part
# print(f'Билет {user_number} счастливый') if digit_summ_first == digit_summ_second else print("Билет не счастливый")
#
# user_number = input("Введите номер билета: ")
#
# first_half_summ = int(user_number[0]) + int(user_number[1]) + int(user_number[2])
# second_half_summ = int(user_number[0]) + int(user_number[1]) + int(user_number[2])
# print(f'Билет {user_number} счастливый') if first_half_summ == second_half_summ else print("Билет не счастливый")


# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

choco_length = int(input("Введите длину шоколадки в дольках: "))
choco_width = int(input("Введите ширину шоколадки в дольках: "))
user_choco = int(input("Введите количество долек, которые вы хотите отломить: "))

if user_choco == choco_length or user_choco == choco_width:
    print('yes')
elif user_choco % choco_length == 0 and user_choco // choco_length <= choco_width:
    print('yes')
elif user_choco % choco_width == 0 and user_choco // choco_width <= choco_length:
    print('yes')
else:
    print('no')
