# На столе лежат n монеток. Некоторые из монеток лежат вверх решкой, а некоторые – гербом.
# Ваша задача - определить минимальное количество монеток, которые нужно перевернуть,
# чтобы все монетки лежали одной и той же стороной вверх.
#
# Входные данные:
# На вход программе подается список coins, где coins[i] равно 0, если i-я монетка лежит гербом вверх, и равно 1,
# если i-я монетка лежит решкой вверх. Размер списка не превышает 1000 элементов.
#
# Выходные данные:
# Программа должна вывести одно целое число - минимальное количество монеток, которые нужно перевернуть.
#
# Пример использования На входе:
# coins = [0, 1, 0, 1, 1, 0]
# На выходе:
# 3

# coins = [0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0]
#
# zero_amount = 0
# one_amount = 0
#
# for i in coins:
#     if i == 0:
#         zero_amount += 1
#     if i == 1:
#         one_amount += 1
#
# print(zero_amount) if zero_amount <= one_amount else print(one_amount)

# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
# Примечание: числа S и P задавать не нужно, они будут передаваться в тестах.
# В результате вы должны вывести все возможные пары чисел X и Y через пробел, такие что X <= Y.
# Пример
# На входе:
# s = 12
# p = 27
# На выходе:
# 3 9

# s = 12
# p = 36
#
# for i in range(s // 2):
#     x, y = i + 1, s - i - 1
#     if x * y == p:
#         print(x, y)

# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числаN.
# Пример
# n=16
# #Вывод
# 1
# 2
# 4
# 8
# 16

n = 7

count = 0
result = 0
while result < n:
    result = 2 ** count
    if result <= n:
        print(result)
    count += 1
