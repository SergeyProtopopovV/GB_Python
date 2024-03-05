# По данному целому неотрицательному n вычислите значение n!.
# N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1

# n = int(input("Введите n: "))
#
# factorial = 1
# for i in range(1, n + 1):
#     factorial *= i
#
# print(factorial)

# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является,
# то есть выведите такое число n,
# что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.

# fib1 = 0
# fib2 = 1
#
# A = 13
#
# fib_number = 2
# while fib1 < A:
#     temp = fib1 + fib2
#     fib1 = fib2
#     fib2 = temp
#     fib_number += 1
#
# print(fib_number) if fib1 == A else print(-1)

# Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю наблюдений за погодой.
# Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые годы.
# Их интересует, сколько дней длилась самая длинная оттепель.
# Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 0 градусов Цельсия.
# Напишите программу, помогающую синоптикам в работе.
# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100).
# В следующих строках располагается N целых чисел.
# Каждое число – среднесуточная температура в соответствующий день.
# Температуры – целые числа и лежат в диапазоне от –50 до 50

# days = int(input("Введите количество наблюдаемых дней: "))
#
# warm_days = 0
# max_warm_days = 0
#
# for i in range(1, days + 1):
#     current_temp = int(input("Введите температуру: "))
#     if current_temp > 0:
#         warm_days += 1
#         if max_warm_days < warm_days:
#             max_warm_days = warm_days
#     else:
#         warm_days = 0
#
# print(max_warm_days)

# Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче.
# Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза.
# Все числа натуральные и не превышают 30000.

minimum = 30001
maximum = 0

N = int(input("Введите число арбузов: "))

for _ in range(N):
    mellon_weight = int(input("Введите вес арбуза: "))
    if mellon_weight > maximum:
        maximum = mellon_weight
    if mellon_weight < minimum:
        minimum = mellon_weight

print(minimum, maximum)
