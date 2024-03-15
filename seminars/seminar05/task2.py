# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1
# [1, 3, 4, 1, 5, 1, 5] -> [1, 3, 4, 1, 1, 1 , 1]

input_list = [1, 3, 4, 1, 5, 1, 5]


def change_skills(user_list: list[int]):
    maximum, minimum = max(user_list), min(user_list)
    for i in range(len(user_list)):
        if user_list[i] == maximum:
            user_list[i] = minimum


change_skills(input_list)
print(input_list)
