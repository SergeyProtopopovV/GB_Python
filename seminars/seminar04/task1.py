# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()

input_string = 'a a a b c a a d c d d'
separated_string = input_string.split()

chars_dict = {}
output_string = ''
for char in separated_string:
    if char in chars_dict:
        chars_dict[char] += 1
    else:
        chars_dict[char] = 1
    if chars_dict[char] > 1:
        output_string += f'{char}_{chars_dict[char] - 1} '
    else:
        output_string += f'{char} '

print(output_string)

# a = 'aaabcaadcdd'
# b = ''
# slovar = {}
#
# for i in a:
#     if i not in slovar:
#         slovar[i] = 0
#         b += i
#     else:
#         slovar[i] += 1
#         b += f'{i}_{slovar[i]}'
# print(b)
