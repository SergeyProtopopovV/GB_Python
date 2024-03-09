# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический)
# на K элементов вправо, K – положительное число.

start_list = [1, 3, 5, 6, 2, 4]

k = 3

# for _ in range(k):
#     new_list = start_list.pop(len(start_list) - 1)
#     start_list.insert(0, new_list)
#
# print(start_list)

shift = k % len(start_list)
new_list = start_list[len(start_list) - shift:len(start_list)] + start_list[0:len(start_list) - shift]
print(new_list)
