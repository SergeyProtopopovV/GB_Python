# Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество элементов во втором массиве. Затем элементы второго массива
# Ввод:
# 7
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1
# Вывод:
# 3 3 2 12
# (каждое число вводится с новой строки)

first_array = '3 1 3 4 2 4 12'
second_array = '4 15 43 1 15 1'

first_array = first_array.split()
second_array = second_array.split()


def print_intersection(first_array, second_array):
    for i in first_array:
        if i not in second_array:
            print(i, end=" ")


print_intersection(first_array, second_array)

# def add_in_the_end(array1: list[int], array2: list[int]) -> list[int]:
#     result = []
#     for i in array1:
#         if i not in array2:
#             result.append(i)
#     return result
#
#
# array1 = [1, 2, 3, 4, 5]
# array2 = [6, 2, 8, 5, 0]
# print(add_in_the_end(array1, array2))


def zamena(array1: list[int], array2: list[int]) -> list[int]:
    set_list = set(array2)
    return [num for num in array1 if num not in set_list]


array1 = [1, 2, 3, 4, 5]
array2 = [6, 2, 8, 5, 0]
print(zamena(array1, array2))


# def para(array: list[int]) -> int:
#     return len(array) - len(set(array))
#
#
# list_1 = [2, 2, 2]
# print(sum([list_1.count(i)//2 for i in set(list_1)]))

