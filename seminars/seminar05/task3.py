# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

def is_prime(number: int) -> bool:
    for i in range(2, number // 2):
        if number % i == 0:
            return False
    return True


print('yes') if is_prime(15) else print('no')
