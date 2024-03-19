# Задача №37. Решение в группах 15 минут
# Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

def print_following(number):
    if number == 0:
        return
    print(number, end=" ")
    print_following(number - 1)


print_following(4)